#!/usr/bin/env python3
"""
Add a paper to papers.yaml given an arXiv ID.

Usage:
    python scripts/add_paper.py 2605.08942 --category self-knowledge
    python scripts/add_paper.py 2605.08942 -c agentic --note "Belief/action gap" --sections 2.2,4.1
    python scripts/add_paper.py https://arxiv.org/abs/2605.08942v1 -c safety --dry-run

Category matches by case-insensitive substring (e.g. "self-knowledge" matches
"Self-Knowledge, Introspection, and Metacognition"). Ambiguous matches list
the candidates and exit.

Re-runs `generate_readme.py` after writing unless --no-readme is passed.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

import arxiv

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_PATH = REPO_ROOT / "papers.yaml"


def fetch_arxiv_metadata(arxiv_id: str) -> dict:
    arxiv_id = re.sub(r"^(https?://)?arxiv\.org/abs/", "", arxiv_id.strip())
    arxiv_id = re.sub(r"v\d+$", "", arxiv_id)

    client = arxiv.Client()
    paper = next(client.results(arxiv.Search(id_list=[arxiv_id])))
    return {
        "id": arxiv_id,
        "title": paper.title.replace("\n", " ").strip(),
        "authors": [a.name for a in paper.authors],
        "year": paper.published.year,
    }


def format_author(full: str) -> str:
    parts = full.strip().split()
    if len(parts) == 1:
        return parts[0]
    last = parts[-1]
    initials = " ".join(p[0] + "." for p in parts[:-1])
    return f"{last}, {initials}"


def format_authors(names: list) -> str:
    if not names:
        return ""
    if len(names) == 1:
        return format_author(names[0])
    if len(names) > 5:
        return f"{format_author(names[0])}, et al."
    head = ", ".join(format_author(n) for n in names[:-1])
    return f"{head}, & {format_author(names[-1])}"


def find_category(text: str, query: str) -> str:
    cats = re.findall(r"^- name: (.+)$", text, re.MULTILINE)
    norm = lambda s: re.sub(r"[\s\-,]", "", s.lower())
    q = norm(query)
    matches = [c for c in cats if q in norm(c)]
    if not matches:
        raise SystemExit(
            f"No category matches '{query}'. Available:\n  - " + "\n  - ".join(cats)
        )
    if len(matches) > 1:
        raise SystemExit(
            f"Ambiguous category '{query}'. Matches:\n  - " + "\n  - ".join(matches)
        )
    return matches[0]


def quote_yaml_string(s: str) -> str:
    """Single-quote a string for YAML if it contains chars that need it."""
    needs_quoting = ":" in s or s[:1] in "[{*&!|>'\"%@`#-?"
    if not needs_quoting:
        return s
    return "'" + s.replace("'", "''") + "'"


def render_entry(meta: dict, note: str = None, sections: list = None) -> str:
    lines = [
        f"  - authors: {format_authors(meta['authors'])}",
        f"    year: {meta['year']}",
        f"    title: {quote_yaml_string(meta['title'])}",
        f"    citation_tail: '*arXiv preprint arXiv:{meta['id']}*'",
        f"    arxiv_id: '{meta['id']}'",
    ]
    if note:
        lines.append("    notes:")
        lines.append(f"    - {note}")
    if sections:
        lines.append("    sections:")
        for s in sections:
            lines.append(f"    - '{s}'")
    lines.append(f"    url: https://arxiv.org/abs/{meta['id']}")
    lines.append("    link_source: manual")
    return "\n".join(lines) + "\n"


def append_to_category(text: str, category: str, entry: str) -> str:
    pattern = re.compile(
        rf"(^- name: {re.escape(category)}\n  papers:\n)(.*?)(?=^- name: |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(text)
    if not m:
        raise SystemExit(f"Couldn't find category '{category}' in papers.yaml")
    header, body = m.group(1), m.group(2)
    body = body.rstrip() + "\n" + entry
    return text[: m.start()] + header + body + text[m.end() :]


def main():
    p = argparse.ArgumentParser(description="Add a paper to papers.yaml")
    p.add_argument("arxiv_id", help="arXiv ID (e.g. 2605.08942) or URL")
    p.add_argument("--category", "-c", required=True,
                   help="Category name or unique substring (e.g. 'self-knowledge')")
    p.add_argument("--note", "-n", help="Optional short note")
    p.add_argument("--sections", "-s",
                   help="Comma-separated section tags (e.g. 2.2,4.1)")
    p.add_argument("--no-readme", action="store_true",
                   help="Skip running generate_readme.py")
    p.add_argument("--dry-run", action="store_true",
                   help="Print the entry but don't write")
    args = p.parse_args()

    print(f"Fetching {args.arxiv_id} from arXiv...")
    meta = fetch_arxiv_metadata(args.arxiv_id)
    print(f"  Title:   {meta['title']}")
    print(f"  Authors: {len(meta['authors'])} ({meta['authors'][0]}"
          f"{', et al.' if len(meta['authors']) > 1 else ''})")
    print(f"  Year:    {meta['year']}")

    text = PAPERS_PATH.read_text()
    category = find_category(text, args.category)
    print(f"  Target:  {category}")

    sections = [s.strip() for s in args.sections.split(",")] if args.sections else None
    entry = render_entry(meta, args.note, sections)

    print("\nEntry:\n" + entry)

    if args.dry_run:
        print("(dry run — no changes written)")
        return

    if meta["id"] in text:
        print(f"  {meta['id']} already in papers.yaml — skipping")
        return

    PAPERS_PATH.write_text(append_to_category(text, category, entry))
    print(f"Wrote {PAPERS_PATH.name}")

    if not args.no_readme:
        subprocess.run(
            [sys.executable, str(Path(__file__).parent / "generate_readme.py")],
            cwd=REPO_ROOT,
            check=True,
        )


if __name__ == "__main__":
    main()
