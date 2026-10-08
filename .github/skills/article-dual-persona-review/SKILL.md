---
name: article-dual-persona-review
description: Review an article draft in this series against two reader personas — a decision-making manager and a hands-on technical practitioner — score its editorial publishability, check its separate proofreading gate, assess platform fit when editorially ready, and insert a short review block at the top of the file. Use when asked to review, rate, or assess an article, check whether a draft lands for its intended audience, set the intended audience, assess Medium, LinkedIn, dbt, or Reddit suitability, or add/refresh the review block on an article draft.
---

# Dual-persona article review

Reviews one article draft against two reader personas, scores its editorial
readiness independently from proofreading quality, assesses platform fit once the
article is editorially ready, and writes a compact review block at the top of the
file.

## When to use

- "review this article"
- "does this land for both audiences?"
- "rate article 03"
- "is this ready for Medium and LinkedIn?"
- "which platforms should this article go to?"
- "refresh the review block"

## Inputs

Always read these before reviewing:

- `01_project_summary.md` — series premise and track structure
- `02_core_principles.md` — the positions the series argues
- `05_style_and_voice.md` — tone rules and banned constructions
- `06_content_boundaries.md` — what must never appear
- `series1/article-outlines.md` — the intended scope of this specific article

## Intended audience

Every article declares its primary audience at the top of the file:

```markdown
**Intended audience:** Manager | Technical | Both
```

This line sits directly under the article title, above the body. It is part of the
article, so it stays in place between reviews.

If the line is missing, derive it and add it:

| Track | Default audience |
|---|---|
| Track 0 — Introduction | Both |
| Track 1 — Architecture | Both, leaning Manager |
| Track 2 — Model & Toolchain | Technical |
| Track 3 — AI in Practice | Both, leaning Manager |
| Track 4 — dbt with Fabric | Technical |

The default is a starting point. If the draft itself clearly aims elsewhere, use
what the draft does and say so in the review.

The ambition is that every article carries something for both readers. The
intended audience records which reader the article must serve. Articles that serve
one audience well and the other only partly are acceptable and normal.

## The two personas

### Persona M — the decision maker

A manager or director who decides whether the organisation invests in AI-enabled
data platform work. Reads to answer:

- What problem does this solve, in business terms?
- What does it cost me — effort, discipline, change to how the team works?
- What do I get that I do not have today?
- Is this a real experience report or a sales pitch?
- Can I repeat the core argument to my own stakeholders in two sentences?

Loses interest when: the article opens with implementation detail, the payoff is
implied rather than stated, jargon arrives before its motivation, or claims come
without a cost attached.

### Persona T — the technical practitioner

A senior data engineer or architect who might build the same thing. Reads to answer:

- Can I see enough of the mechanism to judge whether it works?
- Are there concrete artefacts — YAML, SQL, schema fragments, real tool output?
- What broke, and what did they do about it?
- Which decisions were forced, and which were preference?
- What would I have to figure out myself after reading this?

Loses interest when: the article stays at slogan level, examples are sanitised
into meaninglessness, difficulty is glossed over, or the same idea is restated
three times without new detail.

## Rating scale

Rate each persona on a 1–5 scale:

| Score | Meaning |
|---|---|
| 5 | Fully lands. This reader finishes it and acts on it. |
| 4 | Lands, with one gap worth closing. |
| 3 | Partly lands. This reader gets value but skims. |
| 2 | Weak. This reader stops partway. |
| 1 | Misses. Nothing here for this reader. |

Score both personas on every article, whatever the intended audience. The score for
the non-intended persona is information about reach, and a low one is acceptable.

## Editorial publishability rating

A separate 1–5 score for the article's argument, structure, audience fit, and
evidence. Do not lower this score for spelling, grammar, punctuation, or local
copy-editing errors; those are handled by the proofreading gate.

| Score | Meaning |
|---|---|
| 5 | Publish now. |
| 4 | Publish after light edits. No missing content. |
| 3 | One substantial gap to close first. |
| 2 | Several gaps, or the argument does not yet hold together. |
| 1 | Draft or stub. Not close. |

How the persona scores feed into it:

- The **intended** audience score sets the ceiling. Publishable can never exceed the
  score for the audience the article is written for. An article aimed at Technical
  that scores T:3 cannot be rated above 3, whatever its manager score.
- The **other** audience score does not cap anything. It can raise the rating by at
  most one point when it is unexpectedly strong, and it never lowers it. A Technical
  article scoring M:2 is fine.
- Audience **Both** means the lower of the two scores sets the ceiling.
- A breach of `06_content_boundaries.md` forces the publishable rating to 1,
  regardless of everything else.

Write one sentence explaining the rating, naming the single editorial issue that
holds it back.

## Proofreading gate

Proofreading is a separate release gate. Before reviewing, look for the current
report at `series1/proofreading/<ArticleStem>-proofreading.md`, where
`<ArticleStem>` is the target article filename without `.md`.

Use one of these values in the review block:

| Status | Meaning |
|---|---|
| `Pass` | A current proofreading report found no blocking or significant errors. The article may proceed to publication once editorially ready. |
| `Required` | No current proofread report exists, or the report predates a substantive article change. The article must be proofread before publication. |
| `Fail` | The current proofreading report identifies blocking or significant errors that have not been corrected. The article must not be published. |

Editorial publishability and the proofreading gate answer different questions. An
article can score 4/5 for editorial publishability while its release is blocked by
`Required` or `Fail`.

## Platform fit

Assess platform suitability only when **Editorial publishability is 4 or 5**.
Drafts rated 1–3 need article work before channel strategy is useful. Platform fit
does not override a `Required` or `Fail` proofreading gate.

Use this scale for each platform:

| Score | Meaning |
|---|---|
| 5 | Strong fit. Publish here as-is or with only platform formatting. |
| 4 | Good fit. Publish here after a small platform-specific adjustment. |
| 3 | Conditional fit. Use only if the hook, framing, or excerpt is adapted. |
| 2 | Weak fit. The article is too broad, too narrow, or too context-dependent. |
| 1 | Do not publish here. Wrong audience or likely to underperform. |

Platform guidance:

| Platform | Fit criteria |
|---|---|
| Medium | Default long-form anchor for all publishable articles. Best when the argument stands alone, has a clear title, and gives both strategic and implementation context. |
| LinkedIn Newsletter | Default network channel for all publishable articles. Best when the opening states the professional relevance quickly and the ending gives readers a clear reason to follow the series. |
| dbt Slack / Blog | Selective channel. Best for Track 2 and Track 4 pieces, and for Track 1 anti-patterns only when there is concrete dbt, modeling, testing, contract, or implementation value. |
| r/dataengineering | Selective discussion channel. Best for architecture debates, AI payoff, lessons learned, and practical trade-offs that can stand without series context. Avoid pure tool walkthroughs unless they raise a broader engineering question. |

For platform fit, score the article as it stands. Do not assume a separate rewrite.
Mention the single adjustment that would improve each channel only when the score
is below 5.

## Output

Insert the block below at the very top of the article file, above the title.
If a review block already exists, replace it rather than adding a second one.

```markdown
<!-- REVIEW:START -->
> ## Review
>
> **Editorial publishability: _n_/5** — one sentence naming what holds it back.
> **Proofreading gate: Pass | Required | Fail** — one sentence naming the report status.
>
> **Intended audience: Manager | Technical | Both**
>
> **Manager (M): _n_/5** — one sentence on why.
> **Technical (T): _n_/5** — one sentence on why.
>
> **What to change**
>
> 1. ...
> 2. ...
> 3. ...
>
> **Platform fit**
>
> Medium: _n_/5 — one sentence.
> LinkedIn Newsletter: _n_/5 — one sentence.
> dbt Slack / Blog: _n_/5 — one sentence.
> r/dataengineering: _n_/5 — one sentence.
>
> _Reviewed against: 01_project_summary, 02_core_principles, 05_style_and_voice, 06_content_boundaries. Date: YYYY-MM-DD._
<!-- REVIEW:END -->
```

Rules for the block:

- **Maximum five sentences total** across the "What to change" list. Fewer is better.
- Each item names one change: a topic to add, a section to cut, a claim to support,
  or a structural move. Give the change, not a description of the problem.
- Order by impact, highest first.
- Point at concrete locations in the draft ("the section on hash keys", "the closing
  paragraph") so the writer knows where to work.
- If Editorial publishability is 1–3, omit the "Platform fit" section and add one
  sentence after "What to change": `Platform fit will be assessed once editorial
  publishability reaches 4/5.`
- Do not rewrite the article. The block is a work list.
- Flag any breach of `06_content_boundaries.md` as item 1, always.
- Flag any use of the banned negation-contrast pattern from `05_style_and_voice.md`
  if it appears more than twice.

## Procedure

1. Read the four series context files and the relevant outline entry.
2. Read the article draft in full.
3. Find the `**Intended audience:**` line, or derive it from the track and add it
   under the title.
4. Score persona M and persona T, with one supporting sentence each.
5. Derive the editorial publishability rating from the intended audience and the
  persona scores, without considering proofreading errors.
6. Read the current proofreading report, if present, and set the proofreading gate.
7. Collect candidate editorial changes, then cut them down to at most five sentences. Aim the
   changes at the intended audience first.
8. If Editorial publishability is 4 or 5, score Medium, LinkedIn Newsletter, dbt Slack / Blog,
  and r/dataengineering using the platform fit criteria.
9. Insert or replace the `REVIEW:START`/`REVIEW:END` block at the top of the file.
10. Report the editorial publishability rating, proofreading gate, two persona scores,
  and any platform scores in
  the chat reply. Do not repeat the full block.

## Constraints

- Change nothing in the article body. Only the review block and, when it is missing,
  the `**Intended audience:**` line are written.
- Never run a proofread during a review. Use `article-proofreading` to create or
  refresh the separate proofreading report.
- Never change an intended audience that the author has already set. Question it in
  the review instead.
- Never soften a score to be encouraging. The scores are the value of this skill.
- If the draft is a stub or outline rather than prose, rate publishable 1 and score
  what is there.
