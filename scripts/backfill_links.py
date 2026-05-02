"""Backfill missing URLs in papers.yaml using the Semantic Scholar API.

For each entry without a `url`, queries S2 by title and assesses the match
on three signals: title similarity, year (within +/- 1), and author surname
overlap. Entries scoring 3/3 are written back to papers.yaml automatically;
2/3 matches are flagged for manual review in the report; <2 are skipped.

Usage:
    python scripts/backfill_links.py            # writes papers.yaml + report
    python scripts/backfill_links.py --dry-run  # report only, no yaml changes
"""

import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml


S2_BASE = "https://api.semanticscholar.org/graph/v1"
FIELDS = "title,year,authors,externalIds,openAccessPdf,url"
USER_AGENT = (
    "llm-sa-paper-list-backfill/0.1 "
    "(+https://github.com/Dusto-AI/llm-situational-awareness-paper-list)"
)


def s2_query(title: str, cache: dict, delay: float) -> dict:
    if title in cache:
        return cache[title]

    q = urllib.parse.quote(title)
    url = f"{S2_BASE}/paper/search/match?query={q}&fields={FIELDS}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.load(resp)
            break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                data = {"data": []}
                break
            if e.code == 429:
                wait = 5 * (attempt + 1)
                print(f"    rate limited; sleeping {wait}s")
                time.sleep(wait)
                continue
            raise
        except urllib.error.URLError:
            time.sleep(2)
            continue
    else:
        data = {"data": []}

    cache[title] = data
    time.sleep(delay)
    return data


def best_url(paper: dict) -> str | None:
    ext = paper.get("externalIds") or {}
    if ext.get("ArXiv"):
        return f"https://arxiv.org/abs/{ext['ArXiv']}"
    if ext.get("DOI"):
        return f"https://doi.org/{ext['DOI']}"
    oa = paper.get("openAccessPdf") or {}
    if oa.get("url"):
        return oa["url"]
    return paper.get("url")


def normalize_words(s: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", s.lower()))


def title_similarity(a: str, b: str) -> float:
    aw, bw = normalize_words(a), normalize_words(b)
    if not aw or not bw:
        return 0.0
    return len(aw & bw) / max(len(aw), len(bw))


def author_surnames(authors: str) -> set[str]:
    surnames = set(re.findall(r"\b([A-Z][a-zA-Z'\-]+),", authors))
    if not surnames:
        m = re.match(r"([A-Z][a-zA-Z'\-]+)", authors)
        if m:
            surnames.add(m.group(1))
    return surnames


def author_match(entry_authors: str, s2_authors: list[dict]) -> bool:
    surnames = author_surnames(entry_authors)
    s2_text = " ".join((a.get("name") or "") for a in s2_authors)
    return any(sn in s2_text for sn in surnames)


def assess(entry: dict, s2_paper: dict) -> tuple[int, dict]:
    sim = title_similarity(entry.get("title", ""), s2_paper.get("title", ""))
    s2_year = s2_paper.get("year")
    entry_year = entry.get("year")
    year_ok = (
        isinstance(entry_year, int)
        and isinstance(s2_year, int)
        and abs(s2_year - entry_year) <= 1
    )
    auth_ok = author_match(
        entry.get("authors", ""), s2_paper.get("authors") or []
    )

    score = sum([sim >= 0.6, year_ok, auth_ok])
    return score, {
        "title_similarity": round(sim, 2),
        "year_match": year_ok,
        "author_match": auth_ok,
    }


def write_report(
    path: Path,
    matched: list,
    uncertain: list,
    skipped: list,
) -> None:
    lines = [
        f"# Link Backfill Report — {dt.date.today().isoformat()}",
        "",
        f"- **Auto-matched** (3/3, written to papers.yaml): {len(matched)}",
        f"- **Uncertain** (2/3, NOT written — review manually): {len(uncertain)}",
        f"- **Skipped** (<2/3 or not found): {len(skipped)}",
        "",
        "---",
        "",
        f"## Auto-matched ({len(matched)})",
        "",
        "Spot-check a few of these on GitHub before pushing.",
        "",
    ]

    by_cat: dict[str, list] = {}
    for cat, entry, s2, url in matched:
        by_cat.setdefault(cat, []).append((entry, s2, url))
    for cat, items in by_cat.items():
        lines.append(f"### {cat}")
        for entry, s2, url in items:
            lines.append(
                f"- **{entry['authors']} ({entry['year']})** — *{entry['title']}*"
            )
            lines.append(f"  - matched: \"{s2.get('title')}\" ({s2.get('year')})")
            lines.append(f"  - url added: <{url}>")
        lines.append("")

    lines += [
        f"## Uncertain — review manually ({len(uncertain)})",
        "",
        "Add the URL to `papers.yaml` if the match is correct, then re-run "
        "`generate_readme.py`.",
        "",
    ]
    by_cat = {}
    for cat, entry, s2, url, signals in uncertain:
        by_cat.setdefault(cat, []).append((entry, s2, url, signals))
    for cat, items in by_cat.items():
        lines.append(f"### {cat}")
        for entry, s2, url, signals in items:
            lines.append(
                f"- **{entry['authors']} ({entry['year']})** — *{entry['title']}*"
            )
            lines.append(
                f"  - candidate: \"{s2.get('title')}\" ({s2.get('year')})"
            )
            authors_str = ", ".join(
                (a.get("name") or "") for a in (s2.get("authors") or [])[:5]
            )
            if authors_str:
                lines.append(f"  - candidate authors: {authors_str}")
            if url:
                lines.append(f"  - candidate url: <{url}>")
            lines.append(f"  - signals: {signals}")
        lines.append("")

    lines += [
        f"## Skipped — no good match ({len(skipped)})",
        "",
        "These need manual search.",
        "",
    ]
    by_cat = {}
    for cat, entry, reason in skipped:
        by_cat.setdefault(cat, []).append((entry, reason))
    for cat, items in by_cat.items():
        lines.append(f"### {cat}")
        for entry, reason in items:
            lines.append(
                f"- **{entry['authors']} ({entry['year']})** — *{entry['title']}* "
                f"_({reason})_"
            )
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path, default=Path("papers.yaml"))
    ap.add_argument("--report", type=Path, default=Path("link_backfill_report.md"))
    ap.add_argument("--cache", type=Path, default=Path(".s2_cache.json"))
    ap.add_argument("--delay", type=float, default=1.2)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    data = yaml.safe_load(args.input.read_text(encoding="utf-8"))
    cache: dict = (
        json.loads(args.cache.read_text(encoding="utf-8"))
        if args.cache.exists()
        else {}
    )

    matched, uncertain, skipped = [], [], []
    pending = [
        (cat, p)
        for cat in data["categories"]
        for p in cat["papers"]
        if not p.get("unparsed") and not p.get("url") and p.get("title")
    ]
    print(f"backfilling {len(pending)} entries (delay={args.delay}s)...")

    for i, (cat, entry) in enumerate(pending, 1):
        title = entry["title"]
        if i % 10 == 0:
            print(f"  {i}/{len(pending)}...")

        resp = s2_query(title, cache, args.delay)
        results = resp.get("data") or []

        if not results:
            skipped.append((cat["name"], entry, "no_match_returned"))
            continue

        best = results[0]
        score, signals = assess(entry, best)
        url = best_url(best)

        if score >= 3 and url:
            if not args.dry_run:
                entry["url"] = url
                entry["link_source"] = "semantic_scholar"
            matched.append((cat["name"], entry, best, url))
        elif score >= 2 and url:
            uncertain.append((cat["name"], entry, best, url, signals))
        else:
            skipped.append((cat["name"], entry, f"low_score:{score}/3"))

    args.cache.write_text(json.dumps(cache, indent=2), encoding="utf-8")

    if not args.dry_run:
        with args.input.open("w", encoding="utf-8") as f:
            yaml.dump(
                data, f, sort_keys=False, allow_unicode=True,
                default_flow_style=False, width=200,
            )

    write_report(args.report, matched, uncertain, skipped)

    print()
    print(f"  matched (written): {len(matched)}")
    print(f"  uncertain (review): {len(uncertain)}")
    print(f"  skipped: {len(skipped)}")
    print(f"  cache: {args.cache}")
    print(f"  report: {args.report}")
    if args.dry_run:
        print("  (dry run — papers.yaml NOT modified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
