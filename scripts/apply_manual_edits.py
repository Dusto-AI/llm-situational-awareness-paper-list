"""Parse manual_edits.md and apply changes to papers.yaml.

Edit-line conventions in manual_edits.md:
- `url     → <value>` : set url
- `url     → ok`      : accept S2 candidate url shown above
- `url     → skip`    : remove existing url (mark intentionally without link)
- `title   → ok`      : accept S2 candidate title
- `authors → ok`      : accept S2 candidate authors string
- empty after `→`     : keep current value

Year changes are detected implicitly: if the entry header `(YYYY)` differs
from the yaml year, the yaml year is updated.

Usage:
    python scripts/apply_manual_edits.py --dry-run    # preview
    python scripts/apply_manual_edits.py              # write papers.yaml
"""

import argparse
import re
import sys
from pathlib import Path

import yaml


ENTRY_RE = re.compile(r"^- \*\*(.+?) \((.+?)\)\*\* — (.+)$")
S2_CANDIDATE_RE = re.compile(
    r'^\s*- S2 candidate: "(.+?)" \((.+?)\)(?: — (.+))?\s*$'
)
S2_URL_RE = re.compile(r"^\s*- S2 url:\s*(\S+)\s*$")
URL_EDIT_RE = re.compile(r"^\s*url\s+→\s*(.*)$")
TITLE_EDIT_RE = re.compile(r"^\s*title\s+→\s*(.*)$")
AUTHORS_EDIT_RE = re.compile(r"^\s*authors\s+→\s*(.*)$")


def parse_year(y: str):
    m = re.match(r"^\d{4}", y)
    if m:
        return int(m.group(0))
    return y.strip()


def parse_edits(path: Path):
    edits, other_fixes = [], []
    current, current_cat = None, None
    in_other, in_code_block = False, False

    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("## Other fixes"):
            if current:
                edits.append(current)
                current = None
            in_other = True
            continue

        if in_other:
            stripped = raw.strip()
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block or not stripped:
                continue
            if stripped.startswith(("Use this", "Format is loose", "<!--")):
                continue
            other_fixes.append(stripped)
            continue

        if raw.startswith("### "):
            current_cat = raw[4:].strip()
            if current:
                edits.append(current)
                current = None
            continue

        m = ENTRY_RE.match(raw)
        if m:
            if current:
                edits.append(current)
            current = {
                "category": current_cat,
                "header_authors": m.group(1).strip(),
                "header_year_raw": m.group(2).strip(),
                "header_title": m.group(3).strip(),
                "s2_url": None,
                "s2_title": None,
                "s2_authors": None,
                "url_edit": "",
                "title_edit": "",
                "authors_edit": "",
            }
            continue

        if not current:
            continue

        if m := S2_CANDIDATE_RE.match(raw):
            current["s2_title"] = m.group(1)
            current["s2_authors"] = (m.group(3) or "").strip()
            continue
        if m := S2_URL_RE.match(raw):
            current["s2_url"] = m.group(1)
            continue
        if m := URL_EDIT_RE.match(raw):
            current["url_edit"] = m.group(1).strip()
            continue
        if m := TITLE_EDIT_RE.match(raw):
            current["title_edit"] = m.group(1).strip()
            continue
        if m := AUTHORS_EDIT_RE.match(raw):
            current["authors_edit"] = m.group(1).strip()
            continue

    if current:
        edits.append(current)
    return edits, other_fixes


def find_paper(yml: dict, edit: dict):
    target_cat = edit["category"]
    target_authors = edit["header_authors"]
    target_title = edit["header_title"]

    for cat in yml["categories"]:
        if cat["name"] != target_cat:
            continue
        for p in cat["papers"]:
            if p.get("unparsed"):
                continue
            if (p.get("authors") == target_authors
                    and p.get("title") == target_title):
                return cat, p

    sm = re.match(r"([A-Z][a-zA-Z'\-]+)", target_authors)
    target_sn = sm.group(1) if sm else None
    target_year = parse_year(edit["header_year_raw"])

    for cat in yml["categories"]:
        if cat["name"] != target_cat:
            continue
        for p in cat["papers"]:
            if p.get("unparsed"):
                continue
            psm = re.match(r"([A-Z][a-zA-Z'\-]+)", p.get("authors", ""))
            psn = psm.group(1) if psm else None
            if psn == target_sn and p.get("title") == target_title:
                return cat, p

    candidates = []
    for cat in yml["categories"]:
        if cat["name"] != target_cat:
            continue
        for p in cat["papers"]:
            if p.get("unparsed"):
                continue
            psm = re.match(r"([A-Z][a-zA-Z'\-]+)", p.get("authors", ""))
            psn = psm.group(1) if psm else None
            if psn != target_sn:
                continue
            p_year = p.get("year")
            if p_year == target_year or (isinstance(p_year, int)
                                         and p_year == target_year):
                candidates.append((cat, p))
            elif not isinstance(p_year, int) and not isinstance(target_year, int):
                if str(p_year) == str(target_year):
                    candidates.append((cat, p))
            elif isinstance(target_year, int) and not isinstance(p_year, int):
                candidates.append((cat, p))

    if len(candidates) == 1:
        return candidates[0]
    return None, None


def resolve_ok(edit: dict) -> tuple[str, str, str]:
    url_v = edit["url_edit"]
    ttl_v = edit["title_edit"]
    ath_v = edit["authors_edit"]
    if url_v.lower() == "ok":
        url_v = edit.get("s2_url") or ""
    if ttl_v.lower() == "ok":
        ttl_v = edit.get("s2_title") or ""
    if ath_v.lower() == "ok":
        ath_v = edit.get("s2_authors") or ""
    return url_v, ttl_v, ath_v


def apply_edits(yml: dict, edits: list, dry_run: bool):
    matched, unmatched, no_op = [], [], []
    for edit in edits:
        url_v, ttl_v, ath_v = resolve_ok(edit)
        header_year = parse_year(edit["header_year_raw"])

        if not url_v and not ttl_v and not ath_v:
            cat, p = find_paper(yml, edit)
            if cat and p and p.get("year") != header_year:
                if not dry_run:
                    p["year"] = header_year
                matched.append((edit, [f"year: {p.get('year')!r} → "
                                       f"{header_year!r}"], cat["name"]))
            else:
                no_op.append(edit)
            continue

        cat, p = find_paper(yml, edit)
        if not cat or not p:
            unmatched.append(edit)
            continue

        applied = []
        if p.get("year") != header_year:
            old = p.get("year")
            if not dry_run:
                p["year"] = header_year
            applied.append(f"year: {old!r} → {header_year!r}")

        if url_v:
            if url_v.lower() == "skip":
                if p.get("url"):
                    if not dry_run:
                        p.pop("url", None)
                        p.pop("link_source", None)
                    applied.append("url: removed (skip)")
            else:
                if p.get("url") != url_v:
                    if not dry_run:
                        p["url"] = url_v
                        p["link_source"] = "manual"
                    applied.append("url: set")
        if ttl_v and p.get("title") != ttl_v:
            if not dry_run:
                p["title"] = ttl_v
            applied.append("title: updated")
        if ath_v and p.get("authors") != ath_v:
            if not dry_run:
                p["authors"] = ath_v
            applied.append("authors: updated")

        if applied:
            matched.append((edit, applied, cat["name"]))
        else:
            no_op.append(edit)

    return matched, unmatched, no_op


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path, default=Path("papers.yaml"))
    ap.add_argument("--edits", type=Path, default=Path("manual_edits.md"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.edits.exists():
        print(f"error: {args.edits} not found", file=sys.stderr)
        return 1

    edits, other_fixes = parse_edits(args.edits)
    print(f"parsed {len(edits)} entry blocks from {args.edits}")
    if other_fixes:
        print(f"  + {len(other_fixes)} free-form fixes (will list at end)")

    yml = yaml.safe_load(args.input.read_text(encoding="utf-8"))
    matched, unmatched, no_op = apply_edits(yml, edits, dry_run=args.dry_run)

    print(f"\n  applied:   {len(matched)}")
    print(f"  no-op:     {len(no_op)}")
    print(f"  unmatched: {len(unmatched)}")

    if unmatched:
        print("\nUNMATCHED — couldn't find a paper for these:")
        for e in unmatched:
            print(f"  - [{e['category']}] {e['header_authors']} "
                  f"({e['header_year_raw']}) — {e['header_title'][:70]}")

    if matched:
        print("\nApplied edits:")
        for edit, applied, cat in matched:
            print(f"  [{cat}] {edit['header_authors']} ({edit['header_year_raw']})")
            for a in applied:
                print(f"      {a}")

    if not args.dry_run:
        with args.input.open("w", encoding="utf-8") as f:
            yaml.dump(yml, f, sort_keys=False, allow_unicode=True,
                      default_flow_style=False, width=200)
        print(f"\nwrote {args.input}")
    else:
        print("\n(dry run — papers.yaml NOT modified)")

    if other_fixes:
        print("\nFREE-FORM FIXES (handle manually):")
        for f in other_fixes:
            print(f"  - {f}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
