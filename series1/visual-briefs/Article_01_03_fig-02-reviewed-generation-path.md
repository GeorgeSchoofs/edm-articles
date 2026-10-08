# Article_01_03.fig-02-reviewed-generation-path

Article: Article_01_03
Figure: fig-02-reviewed-generation-path
Audience: Technical
Status: Generated

## Purpose

Clarify where human modelling decisions end and automated generation and validation begin as an approved logical contract flows into downstream artefacts.

## Source section

Sections: "From metadata to generated artefacts", "YAML, Draw.io, and validation", and "Synchronisation and drift".

The article already contains a Mermaid flow of the artefacts. This visual should retain that flow while making the review, approval, generation, and validation responsibilities explicit.

## Visual shape

A left-to-right workflow divided into two bands: human-reviewed modelling and generated outputs. Draw.io and conceptual YAML feed the logical model; modelers enrich and approve logical YAML as the semantic contract. From that approved contract, show generated physical YAML and core table contract, OKF documentation, and Silver ingestion templates. End with schema and cross-layer validation, with a restrained feedback path indicating that detected drift requires the affected artefacts to be brought back into alignment.

## Style and palette (copy with brief)

- Overall: light, uncluttered editorial infographic with hand-drawn character, soft shapes, and restrained accents.
- Background: plain white or very light neutral; leave clear space between human-reviewed and generated stages.
- Primary text and linework: warm dark brown `#402019`.
- Secondary text and dividers: neutral gray `#a3a3a3`.
- Accent palette: muted yellow `#cabe51`, muted orange `#db8c4c`, soft green `#7ec27c`, muted teal `#7eb7ad`, and muted blue `#829cbd`.
- Typography: Shantell Sans for short headings, as observed in the series SVG references. Use a highly legible sans-serif for longer labels if needed.
- Use muted accents to distinguish workflow stages or bands, not to imply unsupported entity classifications. Use neutral connectors and keep all explanatory text dark brown.
- Preserve strong contrast and readability at article display width. Keep the feedback path visually secondary to the forward flow.

Style references: `series1/assets/Article_00_01/fig-01-medallion-gap.svg`, `series1/assets/Article_00_01/fig-02-enhanced-medallion.svg`, and `series1/assets/Article_00_01/fig-03-transformation-journey.png`.

## Napkin input

Paste only this block into Napkin.ai:

```text
From reviewed model to generated artefacts

HUMAN-REVIEWED MODELLING
Draw.io review + conceptual YAML
↓
Logical YAML
- Modelers add attributes, keys, relationships, and history rules
- Approval establishes the semantic contract

AUTOMATED GENERATION
Approved logical contract
├─ Physical YAML → Core table contract
├─ OKF documentation
└─ Silver ingestion templates

VALIDATION
JSON Schema + cross-layer checks
Detect structural errors and drift; keep generated artefacts aligned
```

## Must include

- A visible human review and approval boundary at logical YAML
- The generated outputs named in the article: physical YAML, core table contract, OKF documentation, and Silver ingestion templates
- Validation after generation, including structural and cross-layer checks

## Must avoid

- Suggesting generated artefacts make new semantic decisions
- Inventing a fully automatic Draw.io-to-physical pipeline
- Client names, actual schema names, data volumes, timelines, internal politics, or proprietary algorithms
- Dense labels or unnecessary implementation detail

## Suggested caption

Figure 2. Human approval establishes the logical contract; generation and validation carry it into aligned implementation and documentation artefacts.

## Suggested alt text

A workflow separates human-reviewed modelling from automated generation. Modelers review the conceptual vocabulary and enrich and approve logical YAML. The approved contract generates physical YAML and a core table contract, OKF documentation, and Silver ingestion templates, which are then checked with schema and cross-layer validation.

## Export target

`series1/assets/Article_01_03/fig-02-reviewed-generation-path.png`

## Article figure reference

Article: [Article_01_03](../Article_01_03.md). Placement: after the introductory sentence in "From metadata to generated artefacts".

```html
<figure>
  <img src="assets/Article_01_03/fig-02-reviewed-generation-path.png" alt="A workflow separates human-reviewed modelling from automated generation. Modelers review the conceptual vocabulary and enrich and approve logical YAML. The approved contract generates physical YAML and a core table contract, OKF documentation, and Silver ingestion templates, which are then checked with schema and cross-layer validation." width="700" style="max-width: 100%; height: auto;">
  <figcaption>Figure 2. Human approval establishes the logical contract; generation and validation carry it into aligned implementation and documentation artefacts.</figcaption>
</figure>
```