# Article_00_01.fig-04-transformation-journey

Article: Article_00_01
Figure: fig-01-ai-ready-data-warehouse
Audience: Both
Status: Generated

## Purpose

Show the transformation journey from a legacy warehouse to an AI-ready data foundation, including the modelling and automation practices that make the change sustainable.

## Source section

Sections: "The journey," "Adding a canonical (core) data model," "YAML structures used to model the core data model," and "Automation with Python and AI."


## Visual shape

A horizontal journey map with five deliberate stages: Legacy Warehouse, Canonical Core Data Model, YAML Model Layers, Generated Structures and Documentation, AI-Ready Analytics. Connect the stages with directional arrows. Put a small feedback loop between YAML Model Layers and Generated Structures and Documentation to show synchronisation. Keep the result-oriented final stage visible but restrained.

## Napkin input

Paste only the following fenced text block into Napkin.ai.

```text
From legacy warehouse to AI-ready data foundation

LEGACY WAREHOUSE
→
CANONICAL CORE DATA MODEL
→
YAML MODEL LAYERS
↔
GENERATED STRUCTURES AND DOCUMENTATION
→
AI-READY DATA WAREHOUSE

```

## Must include

- Legacy warehouse as the starting point
- Canonical Core Data Model as the central architectural change
- Conceptual, logical, and physical YAML-based model layers
- Generated physical structures, dbt models, Draw.io or Markdown documentation, and an OKF bundle
- AI-ready analytics based on authoritative business meaning

## Must avoid

- Client names, schema names, data volumes, timelines, internal politics, and proprietary algorithms
- A simplistic claim that the journey is automatic or effortless
- Vendor logos, product-specific icons, or code blocks
- Dense labels that will not be readable in an article-width image

## Suggested caption

Figure 3. The journey builds an AI-ready data foundation by making business meaning explicit and carrying it through modelling, generation, and documentation.

## Suggested alt text

A horizontal transformation journey from a legacy warehouse through a canonical core data model and YAML-based layers to generated data structures, documentation, and AI-ready analytics.

## Export target

`series1/assets/Article_00_01/fig-1-ai-ready-data-warehouse.png`

## Article figure reference

Measured PNG: 846 x 486 px. HTML display width: 1200. Flagged for re-export from the editable or vector source because the PNG is below 1200 px wide; do not upscale the bitmap.

Article: [Article_00_01](../Article_00_01.md). Placement: after the final paragraph of "Automation with Python and AI".

```html
<figure>
  <img src="assets/Article_00_01/fig-1-ai-ready-data-warehouse.png" alt="A horizontal  journey from a legacy warehouse through a canonical core data model and YAML-based layers to generated data structures, documentation, and AI-ready data warehouse." width="1200" style="max-width: 100%; height: auto;">
  <figcaption>Figure 1 The journey builds an AI-ready data foundation by making business meaning explicit and carrying it through modelling, generation, and documentation.</figcaption>
</figure>
```
