---
name: article-proofreading
description: "Proofread article drafts for spelling, grammar, punctuation, terminology, and Markdown errors, then write a release-gate report. Use when asked to proofread an article, find typos, identify grammar errors, check copy editing, or clear an article for publication."
argument-hint: "Article file path or article name"
---

# Article proofreading

Proofreads one article draft and writes a separate report that acts as its
publication proofreading gate. This skill does not rewrite the article unless the
user explicitly asks to apply the reported corrections.

## When to use

- "proofread this article"
- "find grammar errors"
- "check for typos"
- "copy edit article 01"
- "is this article proofread?"
- "clear this article for publication"

## Inputs

Always read:

- `05_style_and_voice.md` — preferred terminology and voice
- `06_content_boundaries.md` — prohibited content
- `series1/glossary.md` when terminology or proper nouns need checking
- The target article draft in full

## Output location

Write or replace the report at:

```text
series1/proofreading/<ArticleStem>-proofreading.md
```

`<ArticleStem>` is the article filename without `.md`, for example
`Article_00_01`.

## What to check

Check only copy-editing and correctness of presentation:

- Spelling, capitalization, grammar, agreement, punctuation, and incomplete sentences
- Repeated words, missing words, inconsistent tense, and awkward wording that changes or obscures meaning
- Consistent use of approved technical terminology, product names, acronyms, and glossary terms
- Markdown structure: headings, lists, code fences, links, image alt text, and stray formatting characters
- Apparent contradictions or misleading statements introduced by wording, but do not redesign the argument

Do not score the article's strategy, architecture, evidence, audience fit, or
platform suitability. Those belong to `article-dual-persona-review`.

## Severity

| Severity | Definition |
|---|---|
| `Blocker` | Changes or obscures meaning, misnames a core concept or product, leaves broken Markdown, or creates an obvious publishing error. |
| `Significant` | Noticeable grammar, spelling, terminology, or consistency error that weakens professional credibility. |
| `Minor` | Local polish issue that does not impede meaning, such as an optional wording improvement or nonessential whitespace cleanup. |

The proofreading gate passes only when there are no `Blocker` or `Significant`
findings. Minor findings may remain and should be listed for the author.

## Report format

```markdown
# <ArticleStem> proofreading report

Article: <ArticleStem>
Reviewed: YYYY-MM-DD
Proofreading gate: Pass | Fail

## Summary

One sentence describing the result and the number of findings by severity.

## Findings

| Severity | Location | Current text | Recommended correction | Reason |
|---|---|---|---|---|
| Significant | The bronze-layer bullet | "..." | "..." | Subject-verb agreement. |

## Minor polish

- Optional improvement, if any.

## Gate decision

`Pass` or `Fail`, with one sentence explaining whether the article can proceed to
editorial review or publication.
```

Use section names, headings, or short unique excerpts for locations. Avoid raw
line numbers because the report must stay useful after small edits.

## Procedure

1. Read the required context and target article in full.
2. Identify all `Blocker` and `Significant` issues, then add useful `Minor` polish
   items without turning the report into a rewrite.
3. Create or replace the proofreading report under `series1/proofreading/`.
4. Set the gate to `Fail` when one or more Blocker or Significant findings exist;
   otherwise set it to `Pass`.
5. Report the gate and counts in chat. Do not alter the article body unless the user
   explicitly requested corrections.

## Constraints

- Preserve the author's voice. Recommend the smallest correction that resolves an issue.
- Do not introduce new claims, examples, mechanisms, or platform guidance.
- Do not reproduce long source passages in the report. Quote only enough text to
  locate each issue.
- Do not add review blocks to the article. The report is the source of truth for
  proofreading status.