# Article_01_01.fig-02-source-to-core-mapping

Article: Article_01_01
Figure: fig-02-source-to-core-mapping
Audience: Both
Status: Generated

## Purpose

Show how selected attributes from one Bronze invoice row supply several Core entities and relationships while preserving the table's wording exactly.

## Source section

Section: "The silver example"

The figure represents the table introduced by "This one table feeds several canonical entities." It must retain all table text verbatim.

## Visual shape

A left-to-right mapping matrix with Bronze attributes on the left, Core targets in the centre, and business interpretation on the right. Repeated source attributes should remain separate rows because each row represents a distinct mapping outcome. Use restrained connectors or row alignment to make the one-to-many mapping pattern clear without adding entities or relationships.

## Style and palette (copy with brief)

- Overall: clean, light editorial infographic matching the hand-drawn character, soft shapes, rounded linework, and restrained colour of the Article_00_01 references.
- Background: plain white or very light neutral with ample open space.
- Primary text and linework: warm dark brown `#402019`.
- Secondary text and neutral rules: gray `#a3a3a3`.
- Accent palette: muted yellow `#cabe51`, muted orange `#db8c4c`, soft green `#7ec27c`, muted teal `#7eb7ad`, and muted blue `#829cbd`.
- Typography: Shantell Sans for short labels. Use a highly legible sans-serif for dense mapping text when needed.
- Use muted orange for Bronze attribute markers, soft green for Core target markers, and neutral rules for row alignment. Keep all long text in `#402019`.
- Avoid large saturated fills. Preserve strong contrast and readability at article display width.

Style references:

- `series1/assets/Article_00_01/fig-01-medallion-gap.svg`
- `series1/assets/Article_00_01/fig-02-enhanced-medallion.svg`
- `series1/assets/Article_01_01/fig-01-layer-contracts.png`

## Exact figure copy

Reproduce the following table content exactly. Do not paraphrase, shorten, correct, or add labels inside the table.

| Bronze attribute | Core target | Interpretation |
|---|---|---|
| `invoice`, `invoicedate`, `amount` | `sales_invoice` | Invoice identity, date, and amount |
| `whopays` | `party` | Identifies a party |
| `whopays` | `sales_invoice_party_roles` | Party is the invoice payer |
| `legal_entity` | `party` | Identifies a party |
| `legal_entity` | `sales_invoice_party_roles` | Party is the invoice legal entity |
| `credited`, `credit_id` | `sales_invoice_relationship` | Describes a relationship between invoices |

## Production notes

- Produce SVG or HTML/CSS first, then export a high-resolution PNG. Do not rely on direct bitmap generation for exact table copy.
- Preserve all code-style identifiers, underscores, punctuation, and repeated rows exactly.
- Keep the three original headings and use enough vertical space for comfortable reading at article width.
- Do not merge repeated `whopays` or `legal_entity` rows; their separate Core targets are the point of the figure.
- Retain the Markdown table in the article as the accessible text equivalent when the image is inserted.

## Must include

- All six source-to-Core mappings in their existing order
- The exact Bronze attribute, Core target, and Interpretation headings
- Every table cell reproduced verbatim
- A clear distinction between source attributes and canonical targets

## Must avoid

- Invented source attributes, Core entities, joins, or cardinalities
- Paraphrasing or compressing table wording
- Client names, actual schema names, data volumes, timelines, or proprietary logic
- Decorative elements that compete with the mapping text

## Suggested caption

Figure 2. One Bronze invoice row supplies invoice identity, party roles, and relationships to several Core targets.

## Suggested alt text

A six-row mapping from Bronze invoice attributes to Core targets. Invoice fields map to sales invoice, whopays and legal entity each map to party and sales invoice party roles, and credited fields map to a sales invoice relationship.

## Export target

`series1/assets/Article_01_01/fig-02-source-to-core-mapping.png`

## Article figure reference

Article: [Article_01_01](../Article_01_01.md). Placement: immediately before the Bronze attribute / Core target / Interpretation table in "The silver example". Retain the Markdown table as the accessible text equivalent.

```html
<figure>
  <img src="assets/Article_01_01/fig-02-source-to-core-mapping.png" alt="A six-row mapping from Bronze invoice attributes to Core targets. Invoice fields map to sales invoice, whopays and legal entity each map to party and sales invoice party roles, and credited fields map to a sales invoice relationship." width="700" style="max-width: 100%; height: auto;">
  <figcaption>Figure 2. One Bronze invoice row supplies invoice identity, party roles, and relationships to several Core targets.</figcaption>
</figure>
```
