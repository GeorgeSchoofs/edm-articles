# Silverston UDM Decision Reference

This is an original, concise decision aid based on Len Silverston's *The Data Model Resource Book, Volume 1*. Use it for routine modeling work; consult [2001 Data_model Resource Book Volume 1.pdf](./2001 Data_model Resource Book Volume 1.pdf) when a decision needs deeper context or a page-cited rationale.

This reference is supplemental. NLOEDM's approved business decisions, source evidence, semantic documentation, and model YAML remain authoritative.

## Core Decision Rules

| Question | Default direction | Book reference |
| --- | --- | --- |
| Is this a distinct business thing? | Create an entity only for a meaningful, independently identifiable business concept. Use a meaningful singular noun. | Chapter 1, printed pp. 8-9; PDF pp. 19-20 |
| Is the difference only a category? | Use a type/classifier entity and governed values, rather than a new structural entity. | Chapter 1, printed p. 9; PDF p. 20 |
| Does the child share its parent's identity and common facts? | Use a subtype with the inherited parent key. Keep only specialized facts on the subtype. | Chapter 1, printed pp. 9-10; PDF pp. 20-21 |
| Can a concept apply in multiple contexts or change over time? | Prefer a typed association or role instead of duplicating the core entity. | Chapter 1, printed pp. 14-16; PDF pp. 25-27 |
| Does a relationship have attributes or represent many-to-many participation? | Model an association entity with its own business grain, keys, and effective dates where needed. | Chapter 1, printed pp. 14-15; PDF pp. 25-26 |
| Is a relationship understandable to a business reviewer? | Give both directions meaningful relationship names that read as business statements. | Chapter 1, printed p. 16; PDF p. 27 |

## Reusable Patterns

### Party, Roles, and Relationships

- Model people and organizations once as `party` when they share identity or common relationships.
- Use `party_role` for contextual roles that a party can hold concurrently or over time, such as applicant, customer, supplier, inventor, employee, or representative.
- Use a party subtype only when it has durable, subtype-specific attributes or relationships beyond the role itself.
- Model relationships between parties through a typed relationship/association, not repeated role-specific foreign keys.
- Keep contact mechanisms separate from a party so contact details can be typed, reused, and effective-dated where necessary.

**Use for NLOEDM:** customer/applicant/owner, agent, attorney, inventor, examiner, correspondent, organization, contact, and address decisions.  
**Book reference:** Chapter 2, *People and Organizations*, printed pp. 21-67; PDF pp. 32-78.

### Types, Classifications, and Controlled Vocabularies

- Distinguish an instance of a business thing from its classification.
- Use a type entity for stable, reusable categories such as status, relationship type, jurisdiction type, work-effort type, or role type.
- Treat type values as controlled business vocabulary. Source-system codes map to canonical business values; they are not automatically different enterprise concepts.
- Use a typed association when a classification can be repeated, effective-dated, qualified, or have facts of its own.

**Use for NLOEDM:** `*_type`, party categories, statuses, IP-right classifications, matter types, action/deadline types, and role types.  
**Book reference:** Chapter 1, printed p. 9; PDF p. 20. Party classifications and status examples: Chapter 2, printed pp. 31-47; PDF pp. 42-58.

### Identifiers and Codes

- Separate a business identifier value from a source-system record identifier.
- When an identifier can have a type, occur more than once, or be shared across systems, model the identifying business fact explicitly: owner, identifier type, identifier value, and any applicable dates or status.
- Do not make a technical source row ID the only business identity when the business value is known or must be reconciled across sources.

**Use for NLOEDM:** party identifiers, matter/application numbers, external registration numbers, document numbers, and source-system crosswalks.  
**Book reference:** Chapter 3, *Product Identification Codes*, printed pp. 75-76; PDF pages in the Chapter 3 section beginning at PDF p. 3. Apply the same typed-code principle to parties and work efforts.

### Work Effort, Event, and Assignment

- Use a generic work-effort structure when matters, tasks, time entries, and similar units of work share lifecycle, assignment, status, or dependency patterns.
- Differentiate a planned or required item from an event that occurred and a work item that must be performed.
- Use typed associations for work-effort dependencies, assignments, party roles, status history, results, and related artifacts.
- Use a subtype only for a distinct kind of work effort that shares work-effort identity and lifecycle.

**Use for NLOEDM:** matters, tasks, renewals, time entries, planned events, event history, responsibilities, and matter-party participation.  
**Book reference:** Chapter 6, *Work Effort*, printed pp. 185-246; PDF pp. 5-6 list the chapter topics.

### Financial Documents and Parties

- Separate the financial document/header, its lines/items, parties in document-specific roles, status/terms, and related transactions.
- Reuse party roles for debtor, creditor, bill-to, payee, processor, or other context-dependent participation rather than adding person/organization columns for each role.

**Use for NLOEDM:** sales invoices, purchase invoices, charges, costs, invoice roles, payment terms, and accounting relationships.  
**Book reference:** Chapters 4, 7, and 8; printed pp. 105-336; PDF pp. 4-6 list the chapter topics.

## Decision Checklist

Before proposing a new entity or relationship, answer these questions in the assessment:

1. What is the business grain, independent of the source table?
2. Is it already a `party`, `work_effort`, `event`, `document`, contact mechanism, type value, or association fact?
3. Is it a role played by an existing party rather than a new actor entity?
4. Is it a subtype that shares a parent identity, or only a classification value?
5. Does the relationship represent a business fact, and can both directions be named clearly?
6. Are technical source identifiers separate from the approved business key and reusable business identifiers?
7. Does a controlled vocabulary need canonical values, a source-code crosswalk, or an effective-dated association?

## When to Open the PDF

Open the PDF when any of these apply:

- the proposed structure changes conceptual entity identity, subtype boundaries, or association grain;
- a decision materially depends on a Silverston pattern and must be cited in the assessment;
- the source suggests a pattern not covered above, such as products, orders, shipments, budgeting, human resources, or warehouse transformation;
- a book pattern appears to conflict with approved NLOEDM semantics or source evidence.

In the assessment, cite the chapter, printed page, and PDF page when known. Summarize the applicable principle; do not reproduce book diagrams or extended text.