# Silverston Review: NLOEDM Logical Layer

**Review date:** 2026-08-24  
**Scope:** Read-only assessment of `edm/logical/yaml/NLOEDM_logical/` against the reusable-model patterns in [2001 Data_model Resource Book Volume 1.pdf](./2001 Data_model Resource Book Volume 1.pdf).  
**Status:** Findings only. No NLOEDM YAML, converter, or dbt artifacts were changed.

## Reference Principles

The review uses the following principles from Len Silverston's *The Data Model Resource Book, Volume 1*:

- Use a meaningful singular noun for each entity. Type entities represent controlled classifications rather than instances of a real-world thing (PDF page 20, printed page 9).
- A subtype inherits the common attributes and relationships of a meaningful supertype; subtype-only attributes belong on the subtype (PDF pages 20-21, printed pages 9-10).
- Model roles that a party may play concurrently or over time through party roles rather than duplicating the party's base identity (PDF pages 44-45, printed pages 33-34).
- Relationship names should describe the business meaning in both directions and read as a complete sentence (PDF page 27, printed page 16).

The book is supplemental guidance. Approved business decisions, source evidence, and NLOEDM's conceptual, logical, and physical authorities remain higher-precedence sources.

## Review Summary

The logical model has a strong UDM foundation: 171 entities, including 62 type entities, 25 subtypes, and 8 logical-only supertypes. All 210 relationship attribute references resolve to existing columns, and all subtypes use their parent's primary key. The most significant discrepancies are semantic identity and documentation issues rather than broken YAML syntax.

## Findings

### 1. High - Party identification does not model the identifying value

[Party identification](../../../edm/logical/yaml/NLOEDM_logical/logical.party_identification.yml) describes itself as the combination of a party, identification type, and identification value, such as a VAT number. However:

- it has no identifier value, code, or name attribute;
- its alternate key is `party_identification_id`, `record_source`, and `party_identification_type_key`;
- its alternate key does not include `party_key`.

The logical identity is therefore a source-system row identifier instead of the business fact that a party has a typed identifier value. This weakens cross-source identity resolution and contradicts the entity's stated grain.

**Decision required:** Confirm whether this entity must support canonical party identifiers across sources. If so, model the identifier value and use the approved party/type/value business grain; retain source identifiers as lineage attributes rather than the sole identity.

### 2. High - Entity identifiers and names are materially inconsistent

Twenty-three entities have a `name` that differs from their `id`. Some are aliases, but several change the apparent business concept:

- [Event](../../../edm/logical/yaml/NLOEDM_logical/logical.event.yml) has `name: logical.work_effort`.
- [logical.d](../../../edm/logical/yaml/NLOEDM_logical/logical.d.yml) is an event supertype but has `name: logical.party_supertype` and label `d`.
- [Work effort type](../../../edm/logical/yaml/NLOEDM_logical/logical.work_effort_type.yml) has `name: logical.work_effort`.
- `party_party_categories`, `work_effort_category`, and `work_effort_work_effort_category` all use `name: logical.party_category`.

This violates the meaningful-name principle and makes reviews, generated documentation, and name-consuming tooling ambiguous.

**Decision required:** Establish whether `id` or `name` is the canonical logical identity. Normalize the non-canonical property only after confirming the Draw.io/YAML authority and generated-artifact impact.

### 3. Medium - Inheritance relationships assign the source endpoint to a child-owned key

All 25 supertype-to-subtype relationships use the subtype's inherited key as the `attributeids.source` value, although the relationship source is the supertype. For example, [Work effort supertype](../../../edm/logical/yaml/NLOEDM_logical/logical.work_effort_supertype.yml) declares a relationship to `matter` but assigns `logical.matter.work_effort_key` to both endpoints instead of using `logical.work_effort_supertype.work_effort_key` on the source.

The shared key correctly represents inheritance, but endpoint metadata does not reflect ownership. This can mislead model readers and any downstream renderer or validator that interprets relationship attributes semantically.

**Decision required:** Confirm the converter's required inheritance representation. Correct endpoint ownership only if the logical relationship schema and Draw.io synchronization support it.

### 4. Medium - Party-role vocabulary mixes source codes with enterprise roles and contains duplicates

[Party role type](../../../edm/logical/yaml/NLOEDM_logical/logical.party_role_type.yml) contains source-prefixed values such as `eqx applicant`, `eqx inventor`, and `eqx contact`. It includes duplicate `eqx applicant` and `eqx inventor` values.

This is a weaker realization of the party-role pattern: Applicant and Inventor are enterprise roles, while source-specific representations should normally be mapped to those canonical values. The current vocabulary risks treating the same role in different source systems as different business concepts.

**Decision required:** Define canonical party-role values and decide whether source codes belong in sourcemap logic, aliases, or a separate crosswalk. Preserve genuinely distinct business roles only where their semantics differ.

### 5. Medium - Type-entity governance is incomplete

Nine type entities have no `entitytypevalues`, including:

- `charge_adjustment_reason`
- `communication_event_document_type`
- `communication_event_work_effort_type`
- `event_status`
- `party_document_role_groups`
- `party_role_responsibility`
- `work_effort_party_role_group`
- `work_effort_status`
- `work_effort_status_group`

The [logical-layer guidance](../../../edm/documentation/logicallayer.md) states that even source-populated type entities should maintain a curated approved set. Without that governance, classifier values can become unreviewed source artifacts rather than controlled business vocabulary.

**Decision required:** For each entity, explicitly classify it as curated, source-managed with periodic approval, or an incorrectly modeled type.

### 6. Low - Entity and relationship descriptions do not consistently support business review

Five entities have blank or placeholder descriptions, including `accounts_payable`, `accounts_receivable`, `process`, `work_effort_identification_supertype`, and `work_effort_supertype`. Eighteen relationships have blank labels, while several supertype artifacts use labels such as `d` or `o` and descriptions such as `Event to d`.

This limits the model's ability to serve as a shared enterprise vocabulary and falls short of the book's relationship-naming convention.

**Decision required:** Set an accepted minimum for entity description, relationship label, and relationship description before approving logical-model changes.

## Patterns That Are Aligned

The following structures are consistent with the book's reusable modeling approach:

- `party` plus `party_roles` and `party_relationship` separate an actor's identity, roles, and relationships.
- `contact_mechanism`, `work_effort`, and other generic entities are specialized through shared-key subtypes.
- Association entities are used for many-to-many business facts, such as party categories, party contact mechanisms, and work-effort party roles.
- A subtype such as [Employee](../../../edm/logical/yaml/NLOEDM_logical/logical.employee.yml) is not automatically a duplication of a party role: it contains employee-specific attributes, while `party_roles` represents contextual participation.

## Suggested Remediation Order

1. Resolve the party-identification grain and business key before adding more source mappings.
2. Establish canonical entity naming and repair the high-risk `id`/`name` conflicts through the approved Draw.io/YAML workflow.
3. Confirm and standardize supertype relationship endpoint conventions.
4. Curate party-role and other type vocabularies, including duplicate removal and source-code crosswalk decisions.
5. Complete missing descriptions and relationship labels as part of the same approved logical-model maintenance run.

## Evidence and Limitations

- The review read the supplied 525-page PDF and the split logical YAML model as of 2026-08-24.
- It is a design-quality assessment, not a claim that the existing model violates schema validation or that every finding requires change.
- Physical hash composition, source data profiling, and approved business exceptions were outside this review's scope and may justify retaining an apparent discrepancy.