# Article_01_02.fig-01-source-to-udm

Article: Article_01_02
Figure: fig-01-source-to-udm
Audience: Both
Status: Generated

## Purpose

Show how one source-shaped invoice table can be interpreted as several reusable UDM entities and relationships, then support a Gold invoice dimension.

## Source section

From "From a source table to a UDM":

> Consider a source table called `billguides`. It contains invoice attributes, party identifiers, and references to related invoices. A UDM interprets the attributes as several related business concepts.

The mapping is:

- `invoice`, `invoicedate`, and `amount` -> to_sales_invoice   ->  `sales_invoice`
- `whopays` ->  to_party -> `party` 
- `legal_entity` -> to_party -> `party` 
- `whopays` ->  to_sales_invoice_party_roles -> `sales_invoice_party_roles` as invoice payer
- `legal_entity` -> to_sales_invoice_party_roles ->  `sales_invoice_party_roles` as invoice legal entity
- `credited` and `credit_id` -> `sales_invoice_relationship`

- The Core structures support a Gold invoice dimension.

only one line from attribute type to the silver layer. So one for invoice attributes, one for party_identifiers and one for related invoice references

can we show the roles in brackets , on a new lines (invoice_payer, invoice_legal_entity), but inside the silver layer, below the `to_sales_invoice_party_roles entity, rather than as part of the line from source to silver.




## Visual shape

A left-to-right source-to-Core-to-Gold flow. Place one Bronze/source table on the left, a fan-out of three Silver mapping paths in the middle, the related Core entities next, and one Gold invoice dimension on the right. Use grouped lanes or restrained colour bands to distinguish source, mapping, Core, and consumption.

## Napkin input

Paste only the following fenced text block into Napkin.ai.

```text
One source row, several reusable business concepts

SOURCE: billguides

Invoice attributes
invoice + invoicedate + amount
→
SILVER INTERPRETATION
→
CORE: sales_invoice

Party identifiers
whopays + legal_entity
→
SILVER INTERPRETATION
→
CORE: party + sales_invoice_party_roles
- Invoice payer
- Invoice legal entity

Related invoice references
credited + credit_id
→
SILVER INTERPRETATION
→
CORE: sales_invoice_relationship

DOCUMENTED CORE STRUCTURES
→
GOLD: Invoice dimension
```

## Must include

- The single `billguides` source table as the starting point.
- Separate paths for invoice attributes, party roles, and invoice relationships.
- The idea that one source row contributes to multiple canonical entities.
- A Gold invoice dimension as a downstream use of the documented Core structures.
- Labels that distinguish source attributes from business concepts.

## Must avoid

- Client names, schema names, data volumes, timelines, internal politics, and proprietary algorithms.
- Showing every physical column or hash-key implementation detail.
- Presenting Silver as a generic copy of Bronze; the visual should show interpretation and mapping.
- Dense SQL or unexplained technical abbreviations.
- Implying that every source table maps one-to-one to one Core entity.

## Suggested caption

Figure 1. A single invoice source can be mapped into several reusable UDM entities and relationships that support downstream Gold models.

## Suggested alt text

A flow diagram showing the billguides source table branching through Silver mappings into sales invoice, party roles, and invoice relationship entities, which then support a Gold invoice dimension.

## Export target

`series1/assets/Article_01_02/fig-01-source-to-udm.png`

## Article figure reference

Article: [Article_01_02](../Article_01_02.md). Placement: after the source-to-UDM mapping table in "From a source table to a UDM". Retain the existing Mermaid diagram and Markdown table.

```html
<figure>
  <img src="assets/Article_01_02/fig-01-source-to-udm.png" alt="A flow diagram showing the billguides source table branching through Silver mappings into sales invoice, party roles, and invoice relationship entities, which then support a Gold invoice dimension." width="700" style="max-width: 100%; height: auto;">
  <figcaption>Figure 1. A single invoice source can be mapped into several reusable UDM entities and relationships that support downstream Gold models.</figcaption>
</figure>
```
