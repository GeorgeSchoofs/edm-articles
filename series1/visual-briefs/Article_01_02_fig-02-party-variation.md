# Article_01_02.fig-02-party-variation

Article: Article_01_02
Figure: fig-02-party-variation
Audience: Both
Status: Draft

## Purpose

Explain how UDM uses one Party concept with types, subtypes, and roles to represent enduring forms and changing business context without duplicating identity.

## Source section

From "Types, subtypes, and roles" and "A small example":

> A party can be a customer in one relationship, a supplier in another, an employee during a period of employment, and a contact for an organisation at the same time.

> A sales system supplies a `Customer` table. An HR system supplies an `Employee` table. A UDM maps both source records into the same Party concept and attaches the relevant business relationship.

## Visual shape

A conceptual relationship map centred on `Party`. Show `Person` and `Organisation` as enduring types or subtypes branching from Party, with `Customer`, `Employee`, `Supplier`, and `Contact` represented as role or context links around the centre. Add small source labels on the left for Sales Customer and HR Employee, both mapping into Party. Keep the diagram relational and legible rather than ontology-like.

## Napkin input

Paste only the following fenced text block into Napkin.ai.

```text
One Party identity, many business contexts

SOURCE INPUTS
Sales Customer → Party
HR Employee → Party

PARTY
Shared identity

ENDURING FORMS
Party → Person
Party → Organisation

CONTEXTUAL ROLES
Party → Customer
Party → Employee
Party → Supplier
Party → Contact

STRUCTURE
Person or Organisation describes what the Party is

BUSINESS CONTEXT
Customer, Employee, Supplier, or Contact describes how the Party participates
```

## Must include

- `Party` as the shared identity and central business concept.
- `Person` and `Organisation` as different enduring forms of Party.
- `Customer`, `Employee`, `Supplier`, and `Contact` as contextual roles.
- The distinction between structural differences and business participation context.
- Two generalized source inputs mapping into the shared Party concept.

## Must avoid

- Client names, schema names, data volumes, timelines, internal politics, and proprietary algorithms.
- Treating Customer or Employee as universal subtypes; the article presents them as roles in the relevant context.
- Adding unsupported ontology notation, formal axioms, or inferred relationships.
- Dense attribute lists or implementation-specific keys.
- Suggesting that all source systems use the same labels or structures.

## Suggested caption

Figure 2. UDM keeps shared party identity in one concept while types, subtypes, and roles express the differences and contexts that matter.

## Suggested alt text

A relationship diagram centred on Party, with Person and Organisation as enduring forms, Customer, Employee, Supplier, and Contact as contextual roles, and Sales Customer and HR Employee source records mapping into the shared Party concept.

## Export target

`series1/assets/Article_01_02/fig-02-party-variation.png`

## Article figure reference

PNG pending. HTML display width: 1600 provisionally; reassess the actual PNG width after export.

Article: [Article_01_02](../Article_01_02.md). Placement: after the final paragraph of "Roles describe context and can change over time", before "A small example". The PNG is pending; do not create a placeholder image.

```html
<figure>
  <img src="assets/Article_01_02/fig-02-party-variation.png" alt="A relationship diagram centred on Party, with Person and Organisation as enduring forms, Customer, Employee, Supplier, and Contact as contextual roles, and Sales Customer and HR Employee source records mapping into the shared Party concept." width="1600" style="max-width: 100%; height: auto;">
  <figcaption>Figure 2. UDM keeps shared party identity in one concept while types, subtypes, and roles express the differences and contexts that matter.</figcaption>
</figure>
```
