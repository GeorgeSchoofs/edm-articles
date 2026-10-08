# Article_00_01.fig-03-transformation-journey

Article: Article_00_01
Figure: fig-03-transformation-journey
Audience: Both
Status: Generated

## Purpose

Show the transformation journey from a legacy warehouse to an AI-ready data foundation, including the modelling and automation practices that make the change sustainable.

## Source section

Sections: "The journey," "Adding a canonical (core) data model," "YAML structures used to model the core data model," and "Automation with Python and AI."

The journey begins with a legacy warehouse. A canonical core data model is added, source ingestion routes into that model, and gold models use it as their source. The model is expressed through conceptual, logical, and physical YAML-based layers. Python and AI skills help generate physical structures and dbt models, while Draw.io and Markdown present the model. An OKF bundle serves as the authoritative description used to ground AI.

## Visual shape

A horizontal journey map with five deliberate stages: Legacy Warehouse, Canonical Core Data Model, YAML Model Layers, Generated Structures and Documentation, AI-Ready Analytics. Connect the stages with directional arrows. Put a small feedback loop between YAML Model Layers and Generated Structures and Documentation to show synchronisation. Keep the result-oriented final stage visible but restrained.

## Napkin input

Paste only the following fenced text block into Napkin.ai.

```text
From legacy warehouse to AI-ready data foundation

LEGACY WAREHOUSE
Existing source-shaped structures
→
CANONICAL CORE DATA MODEL
Shared business concepts and relationships
→
YAML MODEL LAYERS
- Conceptual
- Logical
- Physical
↔
GENERATED STRUCTURES AND DOCUMENTATION
- Physical structures
- dbt models
- Draw.io and Markdown
- Authoritative OKF bundle
→
AI-READY ANALYTICS
Analytics grounded in explicit business meaning

ENABLERS
Python automation + AI skills
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

`series1/assets/Article_00_01/fig-03-transformation-journey.png`

## Article figure reference

Article: [Article_00_01](../Article_00_01.md). Placement: after the final paragraph of "Automation with Python and AI".

```html
<figure>
  <img src="assets/Article_00_01/fig-03-transformation-journey.png" alt="A horizontal transformation journey from a legacy warehouse through a canonical core data model and YAML-based layers to generated data structures, documentation, and AI-ready analytics." width="700" style="max-width: 100%; height: auto;">
  <figcaption>Figure 3. The journey builds an AI-ready data foundation by making business meaning explicit and carrying it through modelling, generation, and documentation.</figcaption>
</figure>
```
