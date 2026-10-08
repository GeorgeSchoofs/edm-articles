# The Journey to a Data Warehouse in the AI Era

An article series about transforming a legacy data warehouse — the architectural decisions, the hard lessons, and the implementation in full.

## Core premise

All about the implementation and how to build a solution based on a sound architectural basis. The series is practical and showcases thinking and implementation skills. It describes how to do this working in an environment with specific tools: dbt, Microsoft Fabric, YAML, Python, and DrawIO.

Some articles emphasise architectural decisions. Others emphasise practical implementation using the tools. The series is structured accordingly into four tracks.

## The series

### Name

The Journey to a Data Warehouse in the AI Era

### Track structure

The series is organised into four tracks with a clear arc: Track 0 sets the stage, Track 1 makes the architectural case, Track 2 explains the toolchain, Track 3 delivers the AI payoff, and Track 4 is the deep implementation reference for practitioners who want to build the same thing themselves.

---

## Track 0 — Introduction

1. Why this journey. Why we bite the bullet and embark on a major restructuring of our legacy data warehouse and what the series is about. *(complete)*
2. What we wanted AI to do — the destination, shown concretely before a single architecture concept is introduced.

---

## Track 1 — Architecture

1. The missing layer: why the medallion architecture falls short for AI
2. The Universal Data Model: what it is and why it fits the AI era
3. The core data model as the new layer in the medallion architecture
4. Metadata-driven modelling: conceptual, logical, and physical layers explained
5. The logical layer as the authoritative core — driving physical, dbt, and documentation
6. Anti-patterns and hard lessons learned

---

## Track 2 — The Model & Toolchain

1. The YAML model: conceptual, logical, and physical files in practice
2. The converter: the tool that bridges model layers and drives generation
3. Generating the OKF documentation bundle from the logical layer
4. How the converter generates dbt SQL from YAML
5. Keeping layers in sync: validation, drift detection, and JSON Schema

---

## Track 3 — What the Foundation Enables: AI in Practice

The payoff track — what the entire structure enables. Because of the documentation and model rigour, AI can now do in minutes what used to take weeks.

1. The ingestion challenge: what it takes to add a new source to the warehouse
2. AI skills for source analysis: mapping a new source to the EDM model
3. AI-assisted dbt sourcemap generation: from analysis to working SQL
4. Using AI to build gold layer models and analysis from documented EDM structures

---

## Track 4 — dbt & Microsoft Fabric Implementation

The deep technical reference track — the full dbt implementation in detail, for readers who want to build the same thing themselves.

1. Medallion modelling in dbt: the full layer overview
2. Bronze: ingesting source data into the warehouse
3. Sourcemap and pre-EDM: a single macro for the silver layer
4. The EDM layer as a data contract with enforced column schema
5. EDM history: full temporal history in a separate, mirrored layer
6. The gold layer: group dimensions, facts, and PIT tables
7. The Puppini bridge macro
8. The semantic model
9. Enabling AI: OKF bundles, dbt AI wizard, and local AI integration
