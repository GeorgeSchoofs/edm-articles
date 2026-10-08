# The Journey to a Data Warehouse in the AI Era
## Article Outlines

---

### Track 0 — Introduction

**01.** Transforming a legacy data warehouse for the AI era. The why and most importantly, the how

Introduction to the series. Why this journey. Why we bite the bullet and embark on a major restructuring of our legacy data warehouse and what the series is about.

**02. Retired** — the AI goals are now included in the closing section of Article 00_01, “What we wanted AI to enable.” The draft remains in `Article_00_02.md` for reference but is no longer part of the publication sequence.

---

### Track 1 — Architecture

**01.** The missing layer: why the medallion architecture falls short for AI

The medallion architecture becomes suitable for AI when every layer has an explicit responsibility, and a canonical (core) data model owns business meaning between source ingestion and consumption models.

A focused outline:

The architectural problem: conventional Silver has too many responsibilities
Why a process architecture needs explicit information contracts
The enhanced model: Bronze, Silver, Core, Gold Engineering, Gold
What each layer owns and guarantees
A customer-to-Party-to-gold-dimension worked path
Governance, traceability, and parallel delivery
What the additional discipline costs
What this enables for AI
Transition to the UDM article



Topics to highlight in Article 01.01

The missing layer is an ownership boundary

The important claim is not simply “add a core model.” It is that the core model owns canonical business meaning, while Bronze owns source fidelity, Silver owns source-to-core translation, and Gold Engineering owns consumption-oriented reshaping.

What each layer guarantees

This is the most valuable expansion path. Define the contract of every layer:

Bronze: complete, historised, source-faithful data
Silver: repeatable mapping from source structures to canonical concepts
Core Data Model: reusable business entities, relationships, keys, and definitions
Gold Engineering: transformation patterns that prepare the canonical model for specific consumption needs
Gold: metrics, KPIs, dimensions, facts, and semantic consumption models
Why Silver becomes two distinct concerns

This is the central architectural move in the draft. Explain that conventional Silver often combines source interpretation, business modelling, transformation logic, and preparation for consumption. Separating source-to-core mapping from core-to-gold preparation gives both jobs a clear purpose and a stable input/output contract.

The core model as a shared dependency

Once it exists, teams can develop source ingestion and gold models in parallel. They share the core model as a stable interface. This is a useful managerial and architectural point because it explains how the additional layer can reduce coordination cost rather than merely add process.

Governance and audit traceability

Expand the line about audit questions. The core model provides a defined route:


The argument is that traceability comes from explicit transformation and semantic contracts, not from trying to reconstruct meaning from scattered SQL after the fact.

The role of documentation in the architecture

Article 00_01 establishes that documentation matters. Article 01_01 should explain where it belongs: definitions and relationships are part of the core-model contract, while each transformation layer documents its mapping and derivation. Documentation becomes a maintained architectural asset, rather than a separate after-the-fact deliverable.

Why AI benefits from the separation

Keep this concrete and restrained:

AI can use core definitions to select relevant concepts
AI can use relationships to construct valid joins
AI can use documented metrics to explain calculations
AI can use mapping rules to help onboard a new source
Do not repeat general “AI needs structure” statements. Show the architectural mechanism that provides it.

What this architecture costs

This is largely absent and would make the article more credible. It requires modelling discipline, explicit contracts, source mapping work, versioned documentation, and governance over semantic changes. That trade-off is especially relevant to managers.

A worked path through the layers

Use one compact running example, perhaps a source system’s customer record:

A source customer arrives in Bronze without semantic reshaping
Silver maps it to canonical Party and Party Role concepts
The Core Data Model retains the canonical business structure
Gold Engineering derives a reporting-friendly customer dimension
Gold exposes customer metrics through a semantic model
This is stronger than adding a large YAML sample. It turns the architecture into a traceable sequence.






**02.** The Universal Data Model: what it is and why it fits the AI era

What is udm: a universal way of describing data

- 3NF based model entities as  as business concepts
- use types to distinguish between various forms of the business concept
- use subtypes when the attribute between the types differ can the concept appear in multiple context or change - over time: use role to identifies this changeexample: partyif you read this and think, this sounds very much like ontologies, you are right. close to an ontology

Examples: 

- customer table becomes party, with type "organisation" and subtype "customer"
- enployee table becomes party, with type "person" and subtype "employee"

what are ontologies and why do they fit with ai. 

why universal data modelling structures the data similar to an an ontology



**03.** Metadata-driven modelling of the core data layer: conceptual, logical, and physical layers explained

- Why layers are required: separate business meaning, logical rules, and target-platform implementation so each decision has one authoritative home.
- Use one running `Party` example across all three layers, including its type/role relationships and `1:N` cardinality.

### Conceptual layer

- Business vocabulary only: entity definitions, labels, descriptions, UDM entity types, controlled type values, relationships, and cardinality.
- Decisions to make before adding a new entity: type value, role, subtype, generic association, or genuinely new business concept.
- Keep attributes, keys, datatypes, and implementation detail out of this layer; make it reviewable by business stakeholders.

### Logical layer

- Add attributes, generic datatypes, primary and alternate business keys, relationship attribute mappings, confidentiality, and effective dates.
- Define the history grain explicitly through driving keys; it can differ from the entity's own primary key.
- Preserve provenance with `derivedfrom` links back to conceptual entities and carry descriptions forward.
- Explain why this is the authoritative semantic contract that drives documentation and downstream generation.

### Physical layer

- Generate one target-specific YAML contract per entity from the logical definition.
- Resolve generic types to Fabric SQL types; add nullable rules, table/schema names, hash-key composition, and foreign-key hashes.
- Add ETL-only system columns and physical history ordering: `load_datetime`, CDC, record hash, process run, and current-record flag.
- Show the boundary: physical concerns must not redefine the business meaning held by the logical model.

### YAML, diagrams, and validation

- YAML as version-controlled metadata: a conceptual collection, split logical entity files plus metadata, and one physical file per entity.
- Draw.io as a visual editing and review surface for the conceptual model, with round-trip synchronisation to YAML.
- JSON Schema and custom validation for identifiers, controlled vocabularies, relationships, key requirements, uniqueness, and cross-layer provenance.
- Synchronisation and drift: changes should flow deliberately through the layers, with validation and content hashes preventing silent divergence.



**05.** The logical layer as the authoritative core — driving physical, dbt, and documentation

- Why the logical model is the centre of modelling: it owns the semantic decisions that must remain stable across platforms, transformations, documentation, and AI-assisted work.
- Clarify the ownership boundary: conceptual YAML owns the high-level business vocabulary; logical YAML owns the complete business structure and rules; physical YAML owns Fabric-specific implementation and ETL mechanics.

### The logical contract

- Entity identity and provenance: stable IDs, names, descriptions, aliases, tags, UDM entity type, and `derivedfrom` links to the conceptual model.
- Business attributes with generic datatypes, consistent template attributes, confidentiality classification, and source provenance through `record_source`.
- Identity and relationships: logical primary keys, alternate/business keys, foreign-key attribute mappings, and cardinality.
- Time as a modelling decision: effective dates and history configuration, especially the driving-key grain that determines what changes together.
- Inheritance and classification: shared identity for subtypes and versioned, approved values for type entities.

### What stays out of the logical layer

- No platform datatypes, table/index/partition choices, hash algorithm or component paths, or operational CDC and process columns.
- Explain why retaining this boundary lets the same logical model drive another physical target without changing its business meaning.

### From model to working artefacts

- Conceptual-to-logical generation creates the structural starting point and preserves the conceptual `derivedfrom` lineage; modelers enrich the logical YAML with the business decisions.
- Logical-to-physical generation resolves SQL types, nullable rules, hash and foreign-key definitions, technical history columns, and table contracts.
- Documentation generation produces the OKF bundle: entity and attribute definitions, keys, incoming/outgoing relationships, and sourcemap SQL templates.
- dbt generation uses the logical semantics and physical contract to scaffold EDM metadata, history models, and source-to-core ingestion structures.

### Why this matters in practice

- Treat logical YAML as version-controlled, reviewable model metadata and the primary change surface for semantic changes.
- Generation and validation turn each approved logical change into consistent downstream artefacts, reducing manual duplication and documentation drift.
- Use `Party` to show the chain from a conceptual definition to logical business keys and history grain, then to its physical `edm.party` contract and generated documentation.



**06.** Anti-patterns and hard lessons learned

- udm modelling requires getting used to
- synching is really hard
- drawio works on the conceptual level, but not ath the logical layer



---

### Track 2 — The Model & Toolchain

**01.** The YAML model: conceptual, logical, and physical files in practice

JSON schema's for every layer allows validation


**02.** The edm studio: the tool that bridges model layers and drives generation

- conceptual /drawio to yaml roundtrips
- conceptual to logical
- logical to physical
- physical in
- generate documentation

- dbt model generation



**03.** Generating the OKF documentation bundle from the logical layer

what does an okf bundle try to solve?

what is okf: open knowledge format. 
- a bundle
- markdown files
- the index
- the okf header 
- a change log 


a simple way of expressing knowledge in markdown files that offers authorative knowledge sources for ai generation.

- description of the entities
- the keys
- the relationships between entities
- sql example templates that help ingestion

Example: simple okf bundle


The bundle can be referenced in AI skills

having a okf bundle with the description of each entity allows ai to understand what entities to use, which releations are needed. The bundle can be used for the ingestion and  it can be used for the gold layer.

It also serves as the definitive documentation of the core model. 



**04.** How core studio generates dbt SQL from YAML






**05.** Keeping layers in sync: validation, drift detection, and JSON Schema

### The problem

The model is is a chain: drawio → conceptual → logical → physical → sourcemap → dbt models → OKF documentation. Every layer is a derivation of the one before it. The moment one link changes and the others do not, the model becomes inconsistent. 

But we want to keep the  model editiable by humans, that adds to the ease-of-use. 

We can identify two types of drift:

- **Structural drift**: a file is edited by hand and no longer matches the shape the generators expect (missing primary key, empty relationship, invalid id).
- **Cross-layer drift**: the layers are each internally valid, but no longer agree with each other. Logical has a new column, physical does not. Conceptual entity renamed, logical `derivedfrom` still points at the old id.


### JSON Schema as the contract

Every layer has its own schema: `conceptual.json`, `logical.json`, `physical.json`, `sourcemap.json`, plus the mxgraph variants for drawio.

The schema is where the modelling rules are written down. Worth showing concretely:

- **Naming as a contract**: entity ids must match `^logical\.[a-z][a-z0-9_]*$`, physical tables `^[a-z][a-z0-9_]*\.[a-z][a-z0-9_]*$`, hash components carry their traversal path in the name pattern. Naming conventions become enforceable.
- **Controlled vocabularies**: `entitytype` is an enum of `type/supertype/subtype/regular`, logical types are a closed list. This is the vocabulary the UDM article introduced and it is now machine checked
- **Provenance is required**: `derivedfrom` on physical must point to a `logical.*` id. The lineage between layers is a schema-enforced field.
- **Conditional rules**: `if/then` — only a `primary_key` hash may have `primary_compose_from`. Schema captures real modelling logic.
- **`additionalProperties: false`** on the physical schema: typos in keys fail loudly instead of being silently ignored by the generator.

Good point to make: the schema is the *specification* of the layer. When you want to change what a logical entity may contain, you change the schema first — and everything downstream is forced to follow.

### Where JSON Schema runs out

Some rules cannot be expressed in draft-07, so the validator extends it with custom keywords and business rules:

- `uniqueBy: "/id"` — entity ids unique across the collection
- `uniqueWithin` — group by one pointer, enforce uniqueness of another inside each group
- `x-globalUniqueColumnIds` — column ids unique across *all* entities, not just within one

The lesson worth writing: you will always need an escape hatch. Keep the rules declared in the schema (as custom keywords), and implement them in the validator, rather than scattering hardcoded checks through the codebase. The schema stays the single place you read to know what a valid model is.


### Validation in practice

The validator reassembles the split-file layers first (the logical layer is one file per entity plus `_metadata.yml`), then validates the whole. Then structure, then custom uniqueness, then business rules such as required default columns on logical entities.

Show real output. The log format is honest and unglamorous:

```
Type: SCHEMA_VALIDATION
Message: [] should be non-empty
Location: er → entities → 2 → keys → primary
Validator: minItems
```

Two stories worth telling here:

- A first validation run on a real inherited model produced 49 errors on the logical layer and 984 on the sourcemap — mostly missing primary keys, empty relationship attribute lists, and null datatypes. That is the true starting condition of most models. Validation does not create quality; it makes the absence of quality visible.
- The path/JSON-pointer location is what makes the errors fixable at scale — including by AI. An error list with precise locations is a work list an agent can grind through.

### Drift detection between drawio and YAML

The interesting part, because it is bidirectional. Both drawio and YAML are editable, so either can be the newer one.

Mechanism:

- `_file_metadata` in the YAML records `last_written`, `source_file`, `source_hash` (hash of what it was generated from) and `content_hash` (hash of its own ER content, with `_file_metadata` excluded to avoid the circularity).
- The drawio `mxfile` element carries `sourceYamlHash` and `sourceYamlPath` as attributes.
- Before any conversion, recompute both hashes and compare against the recorded ones. Timestamps alone are not enough — a file can be touched without changing.

Outcome is a status, not a silent overwrite: `NO_CONFLICT`, `YAML_NEWER`, `DRAWIO_NEWER`, `BOTH_MODIFIED`, `NO_METADATA`, `FILE_MISSING` — each with a recommendation. `BOTH_MODIFIED` is the one that matters: the tool refuses and asks, instead of destroying an afternoon of diagram work.

Note the deliberate design choice: content hash over timestamp, and metadata stored *inside* both artefacts rather than in a side database, so the sync state travels with the files through git.

### Why this matters more in the AI era

Closing argument, tie back to Track 0:

- AI generation amplifies drift. One inconsistent layer becomes a hundred wrong generated models and a documentation bundle that teaches the wrong thing.
- The OKF bundle is generated from the logical layer, so documentation drift and model drift become the same problem — and are solved once.
- Validation is the guardrail that makes autonomous steps acceptable. You can let an agent restructure the model because the schema will catch it if the result is not a valid model.
- Deterministic checks are cheap; AI review is expensive and non-reproducible. Use the schema for everything that can be decided mechanically, and save AI judgement for the semantic questions it is actually good at.

Honest note for the anti-patterns theme: strict schemas are painful at first. Every tightening breaks something. The temptation is to relax the rule; the discipline is to fix the model.





---

### Track 3 — What the Foundation Enables: AI in Practice

**01.** The ingestion challenge: what it takes to add a new source to the warehouse

Source system are often poorly described and the structures suffer from years of updates and work arounds. Updates that are focussed to smooth the ingestion of data. General lookup tables that give no hint at what they are used for.

This makes ingestion of data a challenge. Because the business concepts can not easily be inferred from the table structures. If it is difficult to understand by an analist, do not expect AI to magically offer a solution. It is possible that AI is trained on information that it can apply, but more often than not, information is missing. 

Is an attribute in a table just an attribute, or is this in the udm world a category that needs it own table?

Are debtors customers and suppliers the same concept?


What is the function of a date type attribute? Does it indicate a history that needs to be tracked or is just a date that can be understood as an attribute


And when there is ambiguity AI will start to "hallucinate". That is another word for trying to convince you that it knows something that it doesn't know. 

So we cannnot accept an AI analysis at face value. The analysis should be helped by the analist as much as possible, that will dramatically improve the quality.

Afther the analysis a proposal can be drafted that details how the new source fits into the core model. This description  list all the existing entities that wiill be touched, but also what changes need to be made. 




**02.** AI skills for source analysis: mapping a new source to the EDM model


Ingesting new data into the data warehouse with the core layer follows the following pattern:

Start:
- the source needs to conform to the contract for the bronze layer. It needs to be historized

#### Source description

Source descritpion: to succesfully ingest the new data the source needs to be undefrstood. for each table we would need to know what data is stored, why it is stored, what source primary keys are and what source business keys are. What are the relationships to other tables.

We can describe this as a user or we can let ai try to inferr this. Best to make this a cooperation where you provide as much information as possible and hten let ai help you to add missing pieces, or to point to gaps.

The outcome of this process is a detailed source description document that can be scored on quality. This document catches missing information early in the process and this will save time

#### Source intake

The source description document is used as input for the next step. In this step the source structures need to be translated into business concepts and these need to be fitted into the existing core model entities. The source description documents provides the information the helps ai to make a guess. AI can be gounded in additional background information that help ai to make this translation. This is an iterative process where ai can offer a proposed structure, and with additional input this proposal can be refined into a source-intake document. AI can use the OKF bundle for the reasining. After approval of this document we now have a plan about what we want to do with the source.


##### Core model update

After the appoval the implementation can take place. 

This is a multie step process:

- update the core model for all the layers, conceptual, logical and physical 
- update the dbt models scripts from the core data layer, both the yaml and sql models. 
- actually run the builds of the models. This will create empty tables in fabric

This whole process is executed as an AI skill, with guardrails and checks for each step.

You end up with a fully documented, updated data warehouse that is  now ready for ingestion and data analysis, 

The complete documentation means that these entities can also be used in this analysis phase. 


**03.** AI-assisted dbt ingestion generation: from source analysis to working SQL

The ingestion of data can be thought as two different steps:

- the source data has to be transformed to the target structures of the core model
- the data has to be ingested.


### Transformation

The transformation is a sql script for a views that outputs a core model structure, with all the required attributes and naming. It is based on the SQL template that is created during the generation of the OKF bundle for the model.

This template is the guidance and ensures uniformity.

Each source table is transformed into one or more target tables. Each transformation script is independent of other scripts, thus allowing stand-alone processing. 


### Ingestion

The ingestion model is built in a dbt macro that uses the transformation model and adds the logic to efficiently and correctly ingest the data. This handles the complex logic to:

- build hash keys for the keys and the full record
- only add new or modified rows into the target
- identify deletes, bot explcit deletes and implicit deletes
- add extended logging information







**04.** Using AI to build gold layer models and analysis from documented core model structures

Transforming the data into gold models is greatly helped by the okf bundle and the dbt yaml models.  


it uses various dbt macro's that support specific functions for the gold models:

- genration if oint in time structures according to requirements




---

### Track 4 — dbt with Microsoft Fabric Implementation

**01.** Medallion modelling in dbt: the full layer overview









**02.** Bronze: ingesting source data into the warehouse

**03.** Sourcemap and pre-EDM: a single macro for the silver layer

**04.** The EDM layer as a data contract with enforced column schema

**05.** EDM history: full temporal history in a separate, mirrored layer

**06.** The gold layer: group dimensions, facts, and PIT tables

**07.** The Puppini bridge

**08.** The semantic model

**09.** Enabling AI: OKF bundles, dbt AI wizard, and local AI integration

