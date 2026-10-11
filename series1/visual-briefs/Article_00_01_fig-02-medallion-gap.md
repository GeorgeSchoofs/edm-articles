# Article_00_01.fig-02-medallion-gap

Article: Article_00_01
Figure: fig-02-medallion-gap
Audience: Both
Status: Generated

## Purpose

Explain the three layers of a conventional medallion architecture and distinguish its transformation stages from the explicit information architecture needed to define data shape and meaning.

## Source section

Sections: "The medallion architecture" and "Lacking documentation."

The medallion architecture divides transformation into three phases. Bronze ingests data with minimal conversion. Silver translates source data into business structures and transforms it for BI and data science. Gold contains structures consumed by reporting, analytics, and other end-user tools. This process architecture defines where transformation occurs; explicit data shapes, rules, relationships, and documentation define the information architecture. Without those definitions, source names and measures can remain ambiguous.

## Visual shape

A simple three-layer vertical stack or left-to-right flow. Give each layer one concise responsibility. Add a small, separate note beneath the flow distinguishing transformation stages from the information architecture: defined data shape, rules, relationships, and documentation. Keep the medallion flow as the primary visual; do not turn this into a before-and-after comparison.

## Napkin input

Paste only the following fenced text block into Napkin.ai.

```text
The three layers of a medallion architecture

BRONZE
Source data ingested with minimal conversion
↓
SILVER
Business structures and transformations for BI and data science
↓
GOLD
Structures consumed by reporting, analytics, and end-user tools

INFORMATION ARCHITECTURE
- Defined data shapes and rules
- Explicit relationships
- Natural-language documentation
```

## Must include

- Bronze, Silver, and Gold as the three conventional layers, in order
- The distinct transformation responsibility described for each layer
- Information architecture as explicit data shapes, rules, relationships, and documentation

## Must avoid

- Client names, schema names, data volumes, timelines, internal politics, and proprietary algorithms
- Vendor logos, product branding, or claims that a medallion architecture is inherently wrong
- Invented implementation details or code
- Dense labels that will not be readable in an article-width image

## Suggested caption

Figure 1. Bronze, Silver, and Gold define transformation stages; explicit information architecture defines data shape, relationships, and meaning.

## Suggested alt text

A three-layer medallion flow showing Bronze ingestion, Silver business transformation, and Gold consumption, with a separate note identifying the data shapes, rules, relationships, and documentation that make information meaning explicit.

## Export target

`series1/assets/Article_00_01/fig-01-medallion-gap.png`

## Article figure reference

Measured PNG: 516 x 696 px. HTML display width: 1200. Flagged for re-export from the editable or vector source because the PNG is below 1200 px wide; do not upscale the bitmap.

Article: [Article_00_01](../Article_00_01.md). Placement: after the final paragraph of "The medallion architecture".

```html
<figure>
  <img src="assets/Article_00_01/fig-02-medallion-gap.png" alt="A three-layer medallion flow showing Bronze ingestion, Silver business transformation, and Gold consumption, with a separate note identifying the data shapes, rules, relationships, and documentation that make information meaning explicit." width="1200" style="max-width: 100%; height: auto;">
  <figcaption>Figure 2. Bronze, Silver, and Gold define transformation stages; explicit information architecture defines data shape, relationships, and meaning.</figcaption>
</figure>
```
