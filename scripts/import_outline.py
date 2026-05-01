"""Parse the situational-awareness thesis outline references section and the
companion paper_index.json into a structured papers.yaml.

Usage:
    python scripts/import_outline.py \\
        --outline /path/to/sa_paper_outline.md \\
        --index   /path/to/paper_index.json \\
        --output  papers.yaml
"""

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml


ENTRY_RE = re.compile(
    r"""^(?P<authors>.+?)
        \s*\((?P<year>\d{4}(?:/\d{4})?[a-z]?|n\.d\.|various|forthcoming|in\ press)\)
        \s*\.\s*
        (?P<rest>.+)$""",
    re.VERBOSE,
)
URL_RE = re.compile(r"https?://[^\s\)\]]+")
BRACKET_RE = re.compile(r"\[([^\]]+)\]")
ARXIV_RE = re.compile(r"arXiv:(\d{4}\.\d{4,5})", re.IGNORECASE)
SURNAME_RE = re.compile(r"^([A-Z][a-zA-Z'\-]+)")
SENTENCE_BREAK_RE = re.compile(r"[\.\?!]\s+")


def _split_title_tail(rest: str) -> tuple[str, str]:
    """Split 'Title. *Venue*, pages' (or '...?', '...!') into title and tail."""
    rest = rest.strip()

    star = rest.find("*")
    search_region = rest[:star] if star > 0 else rest

    matches = list(SENTENCE_BREAK_RE.finditer(search_region))
    if matches:
        m = matches[-1] if star > 0 else matches[0]
        title = rest[: m.start() + 1]
        tail = rest[m.end():].strip()
    else:
        title, tail = rest, ""

    title = title.rstrip()
    if title.endswith("."):
        title = title[:-1].rstrip()
    tail = tail.rstrip(". ").strip()
    return title, tail


def parse_entry(text: str) -> dict:
    raw = text
    urls = URL_RE.findall(text)
    text_no_urls = URL_RE.sub("", text).strip()

    notes = BRACKET_RE.findall(text_no_urls)
    text_no_brackets = BRACKET_RE.sub("", text_no_urls).strip()
    text_no_brackets = re.sub(r"\s{2,}", " ", text_no_brackets)

    m = ENTRY_RE.match(text_no_brackets)
    if not m:
        return {"unparsed": True, "raw": raw, "urls": urls, "notes": notes}

    authors = m.group("authors").strip().rstrip(",")
    year_str = m.group("year")
    if re.match(r"^\d{4}", year_str):
        year: object = int(year_str[:4])
    else:
        year = year_str
    rest = m.group("rest").strip()

    title, tail = _split_title_tail(rest)

    arxiv_m = ARXIV_RE.search(raw)
    arxiv_id = arxiv_m.group(1) if arxiv_m else None

    entry = {
        "authors": authors,
        "year": year,
        "title": title,
    }
    if tail:
        entry["citation_tail"] = tail
    if urls:
        entry["url"] = urls[0]
        if len(urls) > 1:
            entry["extra_urls"] = urls[1:]
    if arxiv_id:
        entry["arxiv_id"] = arxiv_id
    if notes:
        entry["notes"] = notes
    return entry


def parse_outline(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")

    in_refs = False
    current: dict | None = None
    categories: list[dict] = []
    skipped_todos = 0

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        if line.startswith("## References"):
            in_refs = True
            continue
        if not in_refs:
            continue
        if line.startswith("## ") and not line.startswith("## References"):
            in_refs = False
            break

        if line.startswith("### "):
            current = {"name": line[4:].strip(), "papers": []}
            categories.append(current)
            continue

        if line.startswith("- ") and current is not None:
            entry_text = line[2:].strip()
            if entry_text.startswith("[TODO"):
                skipped_todos += 1
                continue
            current["papers"].append(parse_entry(entry_text))

    print(f"  parsed {sum(len(c['papers']) for c in categories)} entries "
          f"across {len(categories)} categories "
          f"(skipped {skipped_todos} TODO lines)")
    return categories


def build_section_lookup(index_path: Path) -> dict:
    data = json.loads(index_path.read_text(encoding="utf-8"))
    lookup: dict = {}
    for paper in data["papers"]:
        if paper.get("triage") != "relevant":
            continue
        sections = paper.get("outline_sections") or []
        if not sections:
            continue

        fn = paper["filename"]
        m = re.match(r"^([A-Z]+)\s", fn)
        if not m:
            continue
        surname = m.group(1).title()

        m_year = re.search(r"(\d{4})\.\w+$", fn)
        if not m_year:
            continue
        year = int(m_year.group(1))

        lookup.setdefault((surname, year), [])
        for s in sections:
            if s not in lookup[(surname, year)]:
                lookup[(surname, year)].append(s)

    return lookup


def merge_section_tags(categories: list[dict], lookup: dict) -> int:
    matched = 0
    for cat in categories:
        for paper in cat["papers"]:
            if paper.get("unparsed"):
                continue
            authors = paper.get("authors", "")
            m = SURNAME_RE.match(authors)
            if not m:
                continue
            surname = m.group(1)
            year = paper.get("year")
            if not isinstance(year, int):
                continue
            sections = lookup.get((surname, year))
            if sections:
                paper["sections"] = sorted(sections)
                matched += 1
    return matched


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--outline", type=Path, required=True)
    ap.add_argument("--index", type=Path, default=None,
                    help="Optional paper_index.json for section tag merging")
    ap.add_argument("--output", type=Path, default=Path("papers.yaml"))
    args = ap.parse_args()

    if not args.outline.exists():
        print(f"error: outline not found at {args.outline}", file=sys.stderr)
        return 1

    print(f"reading outline: {args.outline}")
    categories = parse_outline(args.outline)

    if args.index and args.index.exists():
        print(f"reading index: {args.index}")
        lookup = build_section_lookup(args.index)
        matched = merge_section_tags(categories, lookup)
        print(f"  matched section tags for {matched} entries")

    payload = {
        "generated_at": dt.date.today().isoformat(),
        "source_outline": str(args.outline.name),
        "categories": categories,
    }

    with args.output.open("w", encoding="utf-8") as f:
        yaml.dump(payload, f, sort_keys=False, allow_unicode=True,
                  default_flow_style=False, width=200)
    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
