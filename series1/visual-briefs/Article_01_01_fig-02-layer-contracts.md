# Article_01_01.fig-01-layer-contracts

Article: Article_01_01
Figure: fig-01-layer-contracts
Audience: Both
Status: Inserted

## Purpose

Make the responsibilities and handoffs of the five enhanced medallion layers easy to scan while preserving the article table's wording exactly.

## Source section

Section: "The enhanced medallion architecture"

The figure is a visual rendering of the table beginning "Each layer has a separate responsibility and a defined handoff to the next layer." It must retain all table text verbatim.

## Visual shape

A custom, vertically stacked five-row contract map. Each row has three aligned fields: Layer, Owns, and Guarantees to the next layer. Put a slim directional flow indicator between successive rows. Give the Core Data Model row restrained visual emphasis to signal that it owns canonical meaning, while keeping all five layers equally legible.

Use a tall canvas so the longest guarantee statements have room to wrap at readable size. The layer label can be narrower than the two text columns. Use consistent alignment, generous line spacing, and clear column headings. Use distinct but restrained layer accents; do not rely on bronze/brown shades alone to distinguish layers. Maintain strong contrast and a plain, accessible reading order from Bronze through Gold.

## Style and palette (copy with brief)

This specification is self-contained; the reference files are optional provenance.

- Overall: clean, light editorial infographic matching the hand-drawn character, soft shapes, rounded linework, and restrained color of the Article_00_01 references.
- Background: plain white or very light neutral with ample open space.
- Primary text and linework: warm dark brown `#402019`.
- Secondary text and neutral rules: gray `#a3a3a3`.
- Accent palette: muted yellow `#cabe51`, muted orange `#db8c4c`, soft green `#7ec27c`, muted teal `#7eb7ad`, and muted blue `#829cbd`.
- Typography: Shantell Sans, as used in the source exports. If unavailable or too informal for dense table text, use a highly legible sans-serif while retaining the same hierarchy and spacing.
- Use all five accents as small layer markers, in row order: Bronze `#cabe51`, Silver `#db8c4c`, Core Data Model `#7ec27c`, Gold Engineering `#7eb7ad`, and Gold `#829cbd`. This is a visual sequence only, not a business classification.
- Keep all long text in the primary text color and use gray for neutral dividers. Avoid large saturated fills behind copy; preserve the light, open treatment of the references.
- Preserve strong text/background contrast and legibility at article display size.

Style references:

- `series1/assets/Article_00_01/fig-01-medallion-gap.svg`
- `series1/assets/Article_00_01/fig-02-enhanced-medallion.svg`

## Exact figure copy

Reproduce the following table content exactly. Do not paraphrase, shorten, correct, or add labels inside the table.

| Layer | Owns | Guarantees to the next layer |
|---|---|---|
| Bronze | Source fidelity, ingestion metadata, history, and change capture | Complete and consistently typed source data that can be reprocessed without returning to the source system |
| Silver | The repeatable mapping from source structures to canonical business concepts | A transformation that supplies the attributes, keys, and relationships required by the Core Data Model |
| Core Data Model | Canonical entities, business meaning, relationships, keys, and definitions | A reusable and documented business structure that is independent of any single source or analytical use case |
| Gold Engineering | Consumption-specific joins, reshaping, history handling, and technical preparation | Stable inputs for dimensions, facts, semantic models, and other analytical structures |
| Gold | End-user dimensions, facts, metrics, KPIs, and semantic definitions | Structures that are ready for reporting, analysis, and AI-assisted querying |

![Layer contracts](../assets/Article_01_01/fig-01-layer-contracts.png)

## Production notes

- This is a designed graphic, not a Napkin.ai prompt. Build it in a layout or illustration tool that supports exact text placement.
- Preserve the three original column headings and all cell wording verbatim, including punctuation and capitalization.
- Keep the flow cue secondary to the text. It should clarify row order, not imply that every Gold output has another modeled layer after it.
- Apply the palette and row-marker mapping from the Style and palette section when recreating the graphic. The current PNG is a raster export; changing this brief does not restyle that existing file.
- Do not add icons, examples, implementation details, or explanatory copy that are absent from the source table.
- At the intended article display width, check that every cell is comfortably readable. Increase the image's vertical dimensions before reducing type size.
- Retain the Markdown table in the article as the accessible text equivalent if the image is inserted.

## Must include

- The five layers in their existing order: Bronze, Silver, Core Data Model, Gold Engineering, Gold
- The exact Layer, Owns, and Guarantees to the next layer headings
- Every table cell reproduced verbatim
- A clear directional relationship between successive layers

## Must avoid

- Paraphrasing or compressing the table wording
- Client names, source-system names, schema names, data volumes, timelines, internal politics, or proprietary algorithms
- Unsupported guarantees or invented implementation details
- Decorative imagery or dense visual ornament that competes with the text

## Suggested caption

Figure 1. Each layer owns a distinct responsibility and provides a defined guarantee to the next stage of the enhanced medallion architecture.

## Suggested alt text

A five-row architecture map reproducing the article's table verbatim. Bronze, Silver, Core Data Model, Gold Engineering, and Gold are listed in order, with each layer's responsibilities and guarantees shown in separate columns.

## Export target

`series1/assets/Article_01_01/fig-01-layer-contracts.png`

## Article figure reference

Measured PNG: 2400 x 2466 px. HTML display width: 1600. Retain the asset at its native resolution.

Article: [Article_01_01](../Article_01_01.md). Placement: immediately before the Layer / Owns / Guarantees table. Retain the Markdown table as the accessible text equivalent.

```html
<figure>
  <img src="assets/Article_01_01/fig-01-layer-contracts.png" alt="A five-row architecture map reproducing the article's table verbatim. Bronze, Silver, Core Data Model, Gold Engineering, and Gold are listed in order, with each layer's responsibilities and guarantees shown in separate columns." width="1600" style="max-width: 100%; height: auto;">
  <figcaption>Figure 1. Each layer owns a distinct responsibility and provides a defined guarantee to the next stage of the enhanced medallion architecture.</figcaption>
</figure>
```
