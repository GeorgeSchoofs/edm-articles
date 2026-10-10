# Article_01_03.fig-01-party-three-layers

Article: Article_01_03
Figure: fig-01-party-three-layers
Audience: Technical
Status: Generated

## Purpose

Show how one Party concept is expressed across conceptual, logical, and physical layers, with each layer owning a different set of decisions.

## Source section

Sections: "One example across the layers", "The conceptual layer: the business vocabulary", "The logical layer: the semantic contract", and "The physical layer: a target-specific projection".

The Party example appears throughout these sections. The graphic should summarize the distinctions without reproducing the YAML excerpts.

## Visual shape

A left-to-right, three-stage progression for the same Party concept. Each stage names the question it answers, its main modelling content, and one or two examples from the article. Show the business definition carried forward while implementation detail is introduced progressively.

## Style and palette (copy with brief)

- Overall: light, uncluttered editorial infographic with hand-drawn character, soft shapes, and restrained accents.
- Background: plain white or very light neutral; leave ample open space around the three stages.
- Primary text and linework: warm dark brown `#402019`.
- Secondary text and dividers: neutral gray `#a3a3a3`.
- Accent palette: muted yellow `#cabe51`, muted orange `#db8c4c`, soft green `#7ec27c`, muted teal `#7eb7ad`, and muted blue `#829cbd`.
- Typography: Shantell Sans for short headings, as observed in the series SVG references. Use a highly legible sans-serif for longer explanatory labels if needed.
- Use small accent markers to distinguish the three stages; the colors indicate sequence only, not a semantic classification. Keep long copy dark brown and dividers neutral gray.
- Preserve strong contrast and readability at article display width. Avoid large saturated fills and decorative illustration that competes with the layer distinctions.

Style references: `series1/assets/Article_00_01/fig-01-medallion-gap.svg`, `series1/assets/Article_00_01/fig-02-enhanced-medallion.svg`, and `series1/assets/Article_00_01/fig-03-transformation-journey.png`.

## Napkin input

Paste only this block into Napkin.ai:

```text
One Party, three modelling layers

CONCEPTUAL
Business vocabulary
- Party, types, subtypes, roles
- Relationships and cardinality

LOGICAL
Authoritative semantic contract
- Attributes, keys, relationship mappings
- Effective dates and history rules

PHYSICAL
Target-specific implementation
- Platform data types and table contract
- Hashes and ETL system columns

Business meaning flows into implementation; each layer owns distinct decisions
```

## Must include

- The same Party concept across all three layers
- The layer responsibilities and examples stated in the article
- A clear distinction between business meaning, semantic structure, and target implementation

## Must avoid

- Treating the layers as independent models with competing definitions
- Adding implementation details absent from the article
- Client names, actual schema names, data volumes, timelines, internal politics, or proprietary algorithms
- Dense labels that will not be readable at article width

## Suggested caption

Figure 1. The Party concept moves from business vocabulary to a complete semantic contract and then to a target-specific implementation.

## Suggested alt text

A three-stage diagram follows Party through the conceptual, logical, and physical layers. The conceptual layer defines business concepts and relationships, the logical layer adds attributes, keys, mappings, and history rules, and the physical layer adds target-specific types, hashes, tables, and ETL fields.

## Export target

`series1/assets/Article_01_03/fig-01-party-three-layers.png`

## Article figure reference

Measured PNG: 652 x 432 px. HTML display width: 1200. Flagged for re-export from the editable or vector source because the PNG is below 1200 px wide; do not upscale the bitmap.

Article: [Article_01_03](../Article_01_03.md). Placement: after the introductory explanation of the controlled generation path, before "One example across the layers: Party".

```html
<figure>
  <img src="assets/Article_01_03/fig-01-party-three-layers.png" alt="A three-stage diagram follows Party through the conceptual, logical, and physical layers. The conceptual layer defines business concepts and relationships, the logical layer adds attributes, keys, mappings, and history rules, and the physical layer adds target-specific types, hashes, tables, and ETL fields." width="1200" style="max-width: 100%; height: auto;">
  <figcaption>Figure 1. The Party concept moves from business vocabulary to a complete semantic contract and then to a target-specific implementation.</figcaption>
</figure>
```