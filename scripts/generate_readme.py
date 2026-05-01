"""Generate README.md from papers.yaml.

Usage:
    python scripts/generate_readme.py --input papers.yaml --output README.md
"""

import argparse
import datetime as dt
import re
from pathlib import Path

import yaml


HEADER = """\
# LLM Situational Awareness — Paper List

A curated bibliography of papers on **situational awareness in large language
models** — what models know about themselves, their context, and their place
in the world; how that knowledge is measured; and where it breaks down.

Maintained alongside ongoing thesis work. Updated as new papers land.

## About this list

- **Scope.** Situational awareness as understood in two traditions: classical
  SA from human factors (Endsley and successors) and the more recent AI safety
  framing (evaluation awareness, self-knowledge, scheming). Adjacent literatures
  — agentic memory, theory of mind, anthropomorphism, evaluation methodology —
  are included where they directly inform the SA question.
- **Curation.** Selections are working notes from a thesis-in-progress, not an
  exhaustive survey. Some entries are foundational, some are recent and
  unsettled. The list reflects what I've found load-bearing — others may
  reasonably disagree.
- **Categories.** Twelve topical groupings, ordered roughly from foundations
  toward open problems.

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

"""

FOOTER_TEMPLATE = """\

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Pull requests welcome for new papers,
corrections, or category suggestions.

## License

- Code (parsers, generators): [MIT](LICENSE)
- Curated list: [CC-BY-4.0](LIST_LICENSE)

---

*Last updated {date}. Generated from the maintainer's working bibliography.*
"""


def slugify(text: str) -> str:
    s = text.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s).strip("-")
    return s


def render_year(year) -> str:
    if isinstance(year, int):
        return str(year)
    return str(year)


def render_entry(p: dict) -> str:
    if p.get("unparsed"):
        return f"- *(reference note)* {p['raw']}"

    authors = p["authors"]
    year = render_year(p["year"])
    title = p["title"]
    url = p.get("url")
    tail = p.get("citation_tail", "")

    end_punct = "" if title.endswith(("?", "!")) else "."
    line = f"- **{authors} ({year}).** {title}{end_punct}"
    if tail:
        line += f" {tail}."
    if url:
        line += f" [[link]]({url})"
    return line


def _sort_key(p: dict) -> tuple:
    """Sort: real years (newest first) → non-int years → unparsed entries."""
    if p.get("unparsed"):
        return (2, 0, "")
    year = p.get("year")
    if isinstance(year, int):
        return (0, -year, p.get("authors", "").lower())
    return (1, 0, p.get("authors", "").lower())


def render_category(cat: dict) -> str:
    out = [f"## {cat['name']}", ""]
    papers = sorted(cat["papers"], key=_sort_key)
    for paper in papers:
        out.append(render_entry(paper))
    out.append("")
    return "\n".join(out)


def render_toc(categories: list[dict]) -> str:
    lines = ["## Contents", ""]
    for c in categories:
        n = len(c["papers"])
        lines.append(f"- [{c['name']}](#{slugify(c['name'])}) — {n}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path, default=Path("papers.yaml"))
    ap.add_argument("--output", type=Path, default=Path("README.md"))
    args = ap.parse_args()

    data = yaml.safe_load(args.input.read_text(encoding="utf-8"))
    categories = data["categories"]

    parts = [HEADER, render_toc(categories)]
    for cat in categories:
        parts.append(render_category(cat))

    total = sum(len(c["papers"]) for c in categories)
    parts.append(
        f"*This list contains {total} entries across {len(categories)} "
        f"categories.*\n"
    )

    parts.append(FOOTER_TEMPLATE.format(date=dt.date.today().isoformat()))
    args.output.write_text("\n".join(parts), encoding="utf-8")
    print(f"wrote {args.output} ({total} entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
