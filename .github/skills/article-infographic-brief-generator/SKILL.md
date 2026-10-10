---
name: article-infographic-brief-generator
description: "Generate Napkin.ai infographic briefs for article drafts, add article figure references, and update the visual inventory. Use when asked to create Napkin briefs, infographic briefs, visual candidates, visual summaries, diagrams, figures, or image prompts for articles in this series."
argument-hint: "Article file path or article name, plus optional number of infographic candidates"
---

# Article infographic brief generator

Creates focused infographic briefs from article drafts, including either a
Napkin-ready text payload or a designer-ready specification, and keeps a
lightweight inventory of proposed and exported visuals.

## When to use

- "create Napkin briefs for this article"
- "find infographic opportunities in article 01"
- "make visual briefs for Napkin.ai"
- "add infographic candidates"
- "create figure prompts for this draft"
- "update the infographic inventory"
- "create a brief for every table in an article"
- "convert article tables into infographic briefs"

## Inputs

Always read these before generating briefs:

- `01_project_summary.md` — series premise and track structure
- `02_core_principles.md` — the positions the series argues
- `05_style_and_voice.md` — tone rules and banned constructions
- `06_content_boundaries.md` — content that must never appear
- `series1/article-outlines.md` — intended scope of the specific article
- The target article draft in full
- Existing PNG or SVG exports for the article, when present, as visual-style references

## Output locations

Use these paths unless the user asks for a different structure:

```text
series1/
  assets/
    <ArticleStem>/
      fig-01-<short-name>.png
  visual-briefs/
    <ArticleStem>_fig-01-<short-name>.md
  infographic-inventory.md
```

`<ArticleStem>` is the article filename without `.md`, for example
`Article_01_01`.

## Series visual reference

The Napkin exports under `series1/assets/Article_00_01/` establish an initial
visual reference for this series:

- Dark text and linework: `#402019`
- Neutral gray: `#a3a3a3`
- Muted accents: `#cabe51`, `#db8c4c`, `#7ec27c`, `#7eb7ad`, and `#829cbd`
- Typeface observed in the SVG exports: Shantell Sans
- Overall treatment: light, uncluttered backgrounds and restrained color accents

Treat these as reference cues, not a mandatory template. Reuse them when they
suit the subject and remain readable. The source assets do not define a fixed
color-to-layer mapping; do not invent one. Review any closer, article-specific
visual references first, and identify the exact files used in each brief. Preserve
contrast and legibility if the reference font or colors are unsuitable for dense
copy.

## Sizing and readability for Medium

Medium controls the final displayed size. Production must provide sufficient
resolution and a layout that remains readable when scaled down. More pixels
improve sharpness, not the relative size of labels. Standardize export width
where the production tool supports it, not a fixed width and height for all figures.

### Designer-ready briefs (including Claude)

Include a self-contained `## Sizing and readability` section in every
designer-ready brief with these defaults, unless the user specifies otherwise:

- Intended placement: article-column width on Medium.
- Export: PNG, 1600 px wide, with proportional, content-driven height. This is
  the series production default, not a Medium requirement.
- Retain an editable or vector production source when available. Render the PNG
  from that source; do not upscale a small bitmap to meet the width target.
- Use an explicit white or consistent light background and crop unnecessary
  outer whitespace without crowding the content.
- Preview at approximately 700 px displayed width for desktop and 350 px for
  mobile. These are design test widths, not guaranteed Medium layout dimensions.
- Aim for body labels equivalent to at least 16 px at the 700 px preview width.
  Also check the mobile preview: essential labels and the main point must be
  readable without enlarging the image. Pixel dimensions alone do not pass this check.
- If readability fails, simplify nonessential copy, reflow vertically, or split
  the content into separately readable figures. For exact-copy tables, preserve
  every header and cell verbatim; reflow or split rather than shorten the wording.
  Increasing height is useful only when it enables readable wrapping or reflow.
- Do not depend on readers opening a larger version to understand the figure.

### Napkin manual export

Do not add a pixel-size specification or the designer sizing section to
Napkin briefs or their `## Napkin input` blocks. Napkin's resolution selection
is a manual 1x, 2x, or 3x export choice, not a canvas-size instruction.

When handing off a Napkin brief, remind the user to choose the export multiplier
manually and inspect the resulting PNG's dimensions and sharpness. A multiplier
does not guarantee a particular pixel width. Keep the content concise and check
the exported layout at article and mobile widths; a higher multiplier cannot
fix labels that become too small when displayed. Retain an SVG export when available.

Medium's [image guidance](https://help.medium.com/hc/en-us/articles/215679797-Using-images)
states that images must be at least 1192 px wide for all placement options to
appear. Treat this as a placement threshold, not a readability requirement or a
reason to enlarge existing bitmaps automatically.

## Candidate selection

Choose infographic candidates that support the article's argument. Prefer visuals
that clarify structure, flow, responsibility, trade-offs, or before/after states.

Good candidates:

- A layered architecture or data flow the reader must understand
- A sequence of decisions or transformations
- A conceptual distinction that appears repeatedly in the prose
- A manager-facing summary of value, cost, and discipline
- A technical workflow that benefits from visual ordering

Avoid candidates that are only decorative, repeat a paragraph, depend on client
specifics, or require details the article does not provide.

## Table mode

When the user requests briefs for article tables, inspect every Markdown table
outside fenced code blocks and process it in document order.

1. Associate each table with its nearest preceding section heading and introductory
  paragraph.
2. Search existing briefs for the same article and exact header/row content before
  creating anything. Reuse or update a matching brief and inventory row; never create
  a duplicate because its filename or caption differs.
3. Assign uncovered tables the next available figure number and a semantic slug based
  on the table's meaning, not `table-01`.
4. Generate a designer-ready brief with `## Exact figure copy`. Preserve every header
  and cell verbatim. Do not use Napkin input for dense or exact-copy tables.
5. Carry the full series visual specification into every brief. Prefer an SVG or
  HTML/CSS production source that can be exported to PNG; direct bitmap generation
  is unsuitable when exact wording matters.
6. Add or update the article's standard `<figure>` reference immediately before the
  Markdown table, even when its image asset is pending. Keep the Markdown table as
  the accessible text equivalent.
6. Add one inventory row per table brief. Do not create placeholder assets.
7. Report uncovered tables whose briefs or assets are still missing.

## Napkin brief format

When Napkin is the intended production tool, create one Markdown file per
candidate using this structure:

```markdown
# <ArticleStem>.fig-01-<short-name>

Article: <ArticleStem>
Figure: fig-01-<short-name>
Audience: Manager | Technical | Both
Status: Draft

## Purpose

One sentence explaining what the visual should help the reader understand.

## Source section

Name the article section and paste only the relevant paragraphs or a concise
excerpt. Do not paste the full article unless the article is very short.

## Visual shape

Describe the preferred infographic type, such as flow, layered stack, comparison,
cycle, maturity ladder, decision map, or responsibility split.

## Visual style reference

Make this section self-contained so the brief can be copied into another tool
without opening the referenced assets or this skill. Include the actual palette
values, font or font fallback, background, line/shape treatment, contrast guidance,
and how accents should be applied. Name reference files as optional provenance,
not as a substitute for the copied style specification. Distinguish observed
details from recommendations for this figure. Keep production guidance outside the
Napkin input block.

## Napkin input

Paste only the following fenced text block into Napkin.ai. Its contents are the
information to visualize, not instructions about how to make the visual.

```text
Concise visual title

FIRST CONCEPT
Short label
↓
SECOND CONCEPT
- Supporting point
- Supporting point
↓
OUTCOME
Short outcome
```

## Must include

- Specific concept, artifact, layer, role, or outcome from the article
- Another specific element
- Another specific element

## Must avoid

- Client names, schema names, data volumes, timelines, internal politics, and
  proprietary algorithms
- Vendor hype or tool worship
- Invented implementation details
- Dense labels that will not be readable in an article-width image

## Suggested caption

Figure 1. One concise caption in the article's voice.

## Suggested alt text

A plain-language description of the information conveyed by the infographic.

## Export target

`series1/assets/<ArticleStem>/fig-01-<short-name>.png`
```

The first-level heading is the stable article and figure identifier used to manage
the brief. It is not part of the Napkin input. Only the fenced text block under
`## Napkin input` should be pasted into Napkin.ai.

When the user requests exact table wording, precise typography, or a manually
composed layout that Napkin cannot reliably produce, write a designer-ready brief
instead. Include `## Style and palette (copy with brief)`, `## Exact figure copy`, and
`## Production notes`, plus `## Sizing and readability` with the designer defaults
above; omit `## Napkin input` because the exact copy and layout specification are
the production source.

The Napkin input must:

- Contain only concepts, labels, hierarchy, relationships, and outcomes that
  should appear in or be represented by the graphic
- Use short labels, line breaks, arrows, and simple grouping to make the intended
  information structure explicit
- Stand on its own without the Purpose, Source section, Visual shape, Must include,
  Must avoid, caption, alt text, or export metadata
- Avoid layout directions, production notes, prose addressed to the designer, and
  phrases such as "show," "place," "use," or "make"
- Remain concise enough for an article-width graphic

## Inventory format

Create `series1/infographic-inventory.md` if it does not exist. Preserve existing
rows when updating it.

```markdown
# Infographic Inventory

| Article | Figure | Status | Source section | Brief | Asset | Caption |
|---|---|---|---|---|---|---|
| Article_01_01 | fig-01-semantic-flow | Draft | Core idea | visual-briefs/Article_01_01_fig-01-semantic-flow.md | assets/Article_01_01/fig-01-semantic-flow.png | Figure 1. Metadata turns source variation into a reusable semantic contract. |
```

Allowed statuses:

- `Candidate` — useful visual opportunity identified, brief not written yet
- `Draft` — brief written and article figure reference added; image asset is pending
- `Generated` — image exported and placed in `assets/`; article reference resolves to it
- `Inserted` — exported image has been checked in the article at its intended position
- `Retired` — no longer needed

## Procedure

1. Read the required series context files and the target article.
2. Inspect existing article-specific PNG and SVG exports for visual style. Use the
  closest relevant exports as references, and extract exact colors and font names
  from SVG when available. Do not infer a semantic color mapping from color alone.
3. Identify the intended audience from the article, or infer it from the track if
   the line is missing. Do not modify the article unless the user explicitly asks.
4. Select two to five infographic candidates. Fewer is better when the article has
   one dominant idea.
5. For each candidate, name the figure with a stable slug:
   `fig-01-<short-name>`, `fig-02-<short-name>`, and so on.
6. Create or update one brief file per candidate under `series1/visual-briefs/`,
  using the Napkin-ready or designer-ready format appropriate to the request.
  Include a self-contained `## Style and palette (copy with brief)` section in
  every format. Repeat actual style values and application guidance in the brief;
  do not rely on links to the skill or reference assets. Keep style guidance
  outside `## Napkin input`. For designer-ready briefs, also include the
  self-contained sizing and readability specification above. Do not add
  pixel-size requirements to Napkin briefs.
7. Add or update a `<figure>` block in the target article for every brief created
  or refreshed. Use the brief's suggested alt text and caption, and the matching
  PNG path under `assets/<ArticleStem>/`. Add the reference even when the PNG has
  not been exported yet; do not create a placeholder image. Place the block
  immediately after the paragraph or section it supports. Preserve article prose,
  avoid duplicate blocks, and update an existing matching block when its brief
  changes.
8. Create the matching asset directory under `series1/assets/<ArticleStem>/` if it
   does not exist. Do not create placeholder image files.
9. Create or update `series1/infographic-inventory.md` with one row per brief.
10. Report the generated brief files, article figure references, and inventory
  update. For Napkin-ready briefs, remind the user to paste only the
  `## Napkin input` block into Napkin.ai and choose 1x, 2x, or 3x resolution
  manually during export. If checking existing assets, report actual dimensions
  and which preview widths were inspected; do not claim readability was verified
  when the asset is pending or has not been visually checked.

## Writing rules

- Use the article's precise, calm, architect-level voice.
- Keep the editorial brief complete. For Napkin-ready briefs, make only the
  `## Napkin input` block paste-ready for Napkin.ai.
- Carry forward relevant visual language from existing article exports: exact
  colors, typography, background, and recurring form cues. Put the full usable
  style specification in each brief, cite source files as optional provenance,
  and distinguish observed styling from recommendations.
- Write Napkin input as visualizable source content, not as a description of the
  desired graphic.
- Use terminology from the article and glossary. Do not introduce new branded
  language.
- Do not invent mechanisms, tools, schema names, data volumes, timelines, client
  details, or proprietary algorithms.
- Prefer concrete nouns over abstract slogans.
- Captions must explain the point of the visual, not merely name its shape.
- Alt text must describe the information in the image for readers who cannot see
  it.
- Keep all generated files in Markdown. The exported image itself is added later
  after Napkin generation.

## Article figure reference

Whenever a brief is created or refreshed, add or update its image reference in the
target article using the brief's suggested alt text and caption. This reference is
created before image export so the insertion point and accessible text are ready;
the referenced PNG may be pending. Do not create an empty or placeholder image.
Use this format for Markdown articles:

```markdown
<figure>
  <img src="assets/<ArticleStem>/<FigureId>.png" alt="<Suggested alt text from the brief>" width="1600" style="max-width: 100%; height: auto;">
  <figcaption><Suggested caption from the brief></figcaption>
</figure>
```

Select the HTML display width from the actual PNG pixel width for both Napkin
and designer-produced figures:

| Actual PNG width | HTML width attribute | Action |
|---|---|---|
| Below 1200 px | `width="1200"` | Flag for re-export from the editable or vector source; do not upscale the bitmap |
| 1200-1599 px | `width="1200"` | Retain the asset at its native resolution |
| 1600 px or more | `width="1600"` | Retain the asset at its native resolution |
| Asset pending | `width="1600"` | Provisional default; reassess actual width after export |

The cutoff between the two display widths is 1600 source pixels. The 1200 px
re-export threshold is a series production recommendation, distinct from Medium's
1192 px threshold for all placement options. Report dimensions and pending
re-exports; a small asset is not an export failure solely because of its width.

Always retain `style="max-width: 100%; height: auto;"`. The selected width is
the preferred CSS-pixel display width when space permits; narrower containers
shrink the image while preserving its aspect ratio. It does not increase bitmap
resolution, and displaying a small bitmap in a wider container can blur it.
Do not set a fixed height. Preserve an explicitly requested custom display size
when refreshing an existing figure. Keep the brief's reference block and the
article's matching block consistent.

These attributes control presentation, not PNG export resolution or Napkin's
manual resolution multiplier. They are retained in the exported HTML, but Medium
may replace or ignore them during import and apply its own image layout. Verify
the imported draft rather than promising an exact Medium display width. The
publication site's 680 px body maximum also limits displayed figure width; changing
the image width attribute alone does not make a figure span 1200 or 1600 px there.
Continue checking readability at approximately 700 px and 350 px preview widths.

Place each figure directly after the paragraph or section it supports. For a table
visual, place it immediately before the Markdown table and retain that table as the
accessible text equivalent. When matching markup already exists, update it rather
than adding a duplicate. Keep the article's prose unchanged.