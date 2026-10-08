# Article_00_01.fig-02-enhanced-medallion

Article: Article_00_01
Figure: fig-02-enhanced-medallion
Audience: Both
Status: Generated

## Purpose

Show the enhanced medallion architecture as five layers with distinct responsibilities and explicit handoffs, centered on the documented canonical Core Data Model.

## Source section

Sections: "The enhanced medallion architecture" and "What we end up with."

Bronze preserves source data in a defined, historised format. Silver maps source-system data to canonical business concepts. The Core Data Model holds the fully documented canonical business structure and its relationships. Gold Engineering prepares that model for BI and data science. Gold exposes fully described metrics and KPIs for end-user consumption. Explicit definitions and relationships give people and AI systems shared business meaning.

## Visual shape

A five-layer vertical stack or left-to-right flow in this order: Bronze, Silver, Core Data Model, Gold Engineering, Gold. Give each layer a short responsibility and show the handoff between adjacent layers. Emphasize the Core Data Model as the canonical business contract, including documented concepts and relationships. Connect AI to the shared meaning in the Core Data Model and BI/data-science consumption to Gold Engineering and Gold. Avoid implying that every layer has identical documentation requirements.

## Napkin input

Paste only the following fenced text block into Napkin.ai.

```text
Enhanced medallion architecture: five responsibility layers

BRONZE
Defined, historised source data
↓
SILVER
Source-to-canonical mapping
↓
CORE DATA MODEL
Documented canonical business concepts and relationships
↓
GOLD ENGINEERING
Core model reshaped for BI and data science
↓
GOLD
Fully described metrics and KPIs for end users

SHARED BUSINESS MEANING
Core Data Model definitions and relationships
↓
People and AI reason over canonical concepts
```

## Must include

- The five layers in this order: Bronze, Silver, Core Data Model, Gold Engineering, Gold
- Bronze preserves defined, historised source data
- Silver maps source data to canonical business concepts
- Core Data Model owns documented canonical concepts and relationships
- Gold Engineering reshapes the core model for BI and data science
- Gold exposes fully described metrics and KPIs to end users
- People and AI use the canonical business meaning

## Must avoid

- Client names, schema names, data volumes, timelines, internal politics, and proprietary algorithms
- Vendor logos or product-specific architecture icons
- A claim that every organisation needs the same number of layers
- Dense labels, implementation syntax, or YAML snippets

## Suggested caption

Figure 2. A documented Core Data Model separates source-to-canonical mapping from the preparation of data for BI, data science, and end-user metrics.

## Suggested alt text

A five-layer architecture showing defined, historised source data flowing through source-to-canonical mapping, a documented Core Data Model, Gold Engineering, and Gold, where end users consume described metrics and KPIs.

## Export target

`series1/assets/Article_00_01/fig-02-enhanced-medallion.png`

## Article figure reference

Article: [Article_00_01](../Article_00_01.md). Placement: after the paragraph explaining clearer responsibilities, reduced interdependencies, and parallel work in "The enhanced medallion architecture".

```html
<figure>
  <img src="assets/Article_00_01/fig-02-enhanced-medallion.png" alt="A five-layer architecture showing defined, historised source data flowing through source-to-canonical mapping, a documented Core Data Model, Gold Engineering, and Gold, where end users consume described metrics and KPIs." width="700" style="max-width: 100%; height: auto;">
  <figcaption>Figure 2. A documented Core Data Model separates source-to-canonical mapping from the preparation of data for BI, data science, and end-user metrics.</figcaption>
</figure>
```
