# Infographic Inventory

## Image sizing migration

Measured on 2026-10-08. Article and brief reference widths are 1200 for PNGs
below 1600 px wide, 1600 for PNGs at least 1600 px wide, and provisionally 1600
for pending PNGs. Existing image files and lifecycle statuses are unchanged.

The following PNGs are below the 1200 px production threshold and are flagged
for re-export from an editable or vector source; do not upscale the bitmaps:

- Article_00_01 / fig-01-medallion-gap: 516 x 696 px.
- Article_00_01 / fig-02-enhanced-medallion: 756 x 670 px.
- Article_00_01 / fig-03-transformation-journey: 846 x 486 px.
- Article_01_03 / fig-01-party-three-layers: 652 x 432 px.

Article_01_02 / fig-02-party-variation remains pending. Display attributes do
not increase image resolution. Readability at 700 px and 350 px preview widths
has not been visually checked in this migration.

| Article | Figure | Status | Source section | Brief | Asset | Caption |
|---|---|---|---|---|---|---|
| Article_00_01 | fig-01-medallion-gap | Generated | The medallion architecture; Lacking documentation | visual-briefs/Article_00_01_fig-01-medallion-gap.md | assets/Article_00_01/fig-01-medallion-gap.png | Figure 1. Bronze, Silver, and Gold define transformation stages; explicit information architecture defines data shape, relationships, and meaning. |
| Article_00_01 | fig-02-enhanced-medallion | Generated | The enhanced medallion architecture; What we end up with | visual-briefs/Article_00_01_fig-02-enhanced-medallion.md | assets/Article_00_01/fig-02-enhanced-medallion.png | Figure 2. A documented Core Data Model separates source-to-canonical mapping from the preparation of data for BI, data science, and end-user metrics. |
| Article_00_01 | fig-03-transformation-journey | Generated | The journey; YAML structures used to model the core data model; Automation with Python and AI | visual-briefs/Article_00_01_fig-03-transformation-journey.md | assets/Article_00_01/fig-03-transformation-journey.png | Figure 3. The journey builds an AI-ready data foundation by making business meaning explicit and carrying it through modelling, generation, and documentation. |
| Article_01_01 | fig-01-layer-contracts | Inserted | The enhanced medallion architecture | visual-briefs/Article_01_01_fig-01-layer-contracts.md | assets/Article_01_01/fig-01-layer-contracts.png | Figure 1. Each layer owns a distinct responsibility and provides a defined guarantee to the next stage of the enhanced medallion architecture. |
| Article_01_01 | fig-02-source-to-core-mapping | Generated | The silver example | visual-briefs/Article_01_01_fig-02-source-to-core-mapping.md | assets/Article_01_01/fig-02-source-to-core-mapping.png | Figure 2. One Bronze invoice row supplies invoice identity, party roles, and relationships to several Core targets. |
| Article_01_02 | fig-01-source-to-udm | Generated | From a source table to a UDM | visual-briefs/Article_01_02_fig-01-source-to-udm.md | assets/Article_01_02/fig-01-source-to-udm.png | Figure 1. A single invoice source can be mapped into several reusable UDM entities and relationships that support downstream Gold models. |
| Article_01_02 | fig-02-party-variation | Draft | Types, subtypes, and roles; A small example | visual-briefs/Article_01_02_fig-02-party-variation.md | assets/Article_01_02/fig-02-party-variation.png | Figure 2. UDM keeps shared party identity in one concept while types, subtypes, and roles express the differences and contexts that matter. |
| Article_01_03 | fig-01-party-three-layers | Generated | One example across the layers; The conceptual layer; The logical layer; The physical layer | visual-briefs/Article_01_03_fig-01-party-three-layers.md | assets/Article_01_03/fig-01-party-three-layers.png | Figure 1. The Party concept moves from business vocabulary to a complete semantic contract and then to a target-specific implementation. |
| Article_01_03 | fig-02-reviewed-generation-path | Generated | From metadata to generated artefacts; YAML, Draw.io, and validation; Synchronisation and drift | visual-briefs/Article_01_03_fig-02-reviewed-generation-path.md | assets/Article_01_03/fig-02-reviewed-generation-path.png | Figure 2. Human approval establishes the logical contract; generation and validation carry it into aligned implementation and documentation artefacts. |
