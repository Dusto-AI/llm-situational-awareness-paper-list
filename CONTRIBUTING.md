# Contributing

Suggestions, corrections, and additions are welcome.

## Suggesting a paper

Open a pull request that edits `papers.yaml`. Add your entry under the most
appropriate category, following the format of existing entries:

```yaml
- authors: "LastName, F. M., & Other, A."
  year: 2025
  title: "The exact paper title"
  citation_tail: "Journal or Conference Name, vol(issue), pages."
  url: "https://doi.org/..."
```

`citation_tail` is the trailing portion of the citation after authors/year/title
— typically the venue plus volume/issue/pages.

If you're unsure which category fits, open an issue instead and we'll discuss.

## Suggesting a correction

For typos, broken links, or miscategorised entries: open a PR or an issue.

## Suggesting a new category

Open an issue first. Categorisation is editorial and changes affect the whole
list, so it's worth discussing before a PR.

## Out of scope

This list focuses on **situational awareness in large language models**. Adjacent
areas (general agent memory, theory of mind generally, classical SA in human
factors without LLM relevance) are mostly out of scope, with a few foundational
exceptions where they directly inform the LLM literature.
