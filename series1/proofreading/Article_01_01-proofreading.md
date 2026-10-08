# Article_01_01 proofreading report

Article: Article_01_01
Reviewed: 2026-09-20
Proofreading gate: Fail

## Summary

The article has a clear architectural argument and the shortened YAML improves focus, but the draft contains 24 Significant findings and 8 Minor polish findings across spelling, grammar, terminology, punctuation, headings, and SQL examples.

## Findings

| Severity | Location | Current text | Recommended correction | Reason |
|---|---|---|---|---|
| Significant | Opening recap | `Medallion sarchitecture` | `Medallion architecture` | Spelling error in a core term. |
| Significant | Opening recap | `details the life-cycle` | `describes the lifecycle` | Use consistent technical terminology and avoid unnecessary hyphenation. |
| Significant | Opening recap | `allways` and `souuce` | `always` and `source` | Spelling errors in the architecture summary. |
| Significant | Opening recap | `canonical layer that represents data structures in business concepts` | `canonical layer that represents business concepts in a consistent structure` | The current wording is awkward and obscures the intended meaning. |
| Significant | Opening recap | `canonical entties` | `canonical entities` | Spelling error in a core concept. |
| Significant | Cost section | `The additional layer introduces` | `The additional layers introduce` | The architecture adds several defined layers, so the subject should agree with the plural concept. |
| Significant | Bronze requirements | `Having all history available does not mean have all historical records available` | `Having all history available does not mean that every historical record must be retained in the same form` | The current sentence is grammatically incomplete and unclear. |
| Significant | Bronze requirements | `We do not know allways what we will use` | `We do not always know how we will use` | Spelling and grammar errors. |
| Significant | Bronze requirements | `helps in determinging` | `helps in determining` | Spelling error. |
| Significant | Bronze transformations | `all attributed are uniformely cased` | `all attributes are consistently cased` | Spelling, number, and wording errors. |
| Significant | Bronze transformations | `becommes available` | `becomes available` | Spelling error. |
| Significant | Bronze transformations | `record source indicator is added (record_source))` | `a record-source indicator is added (record_source)` | Extra closing parenthesis and missing article. |
| Significant | Bronze transformations | `These transformation provide use` | `These transformations provide us` | Subject-verb agreement and pronoun error. |
| Significant | Bronze SQL example | `a.[user]` followed by `CAST` without a comma | Add the missing comma after `a.[user]`. | The displayed SQL is syntactically malformed. |
| Significant | Bronze SQL example | `a.[id]` appears twice | Remove the duplicate column or explain its purpose. | Duplicate output column makes the example misleading. |
| Significant | Bronze SQL example | `a.[load_datime]` | `a.[load_datetime]` | Inconsistent system-column name. |
| Significant | Core section | `consist of canonical structures` | `consists of canonical structures` | Subject-verb agreement error. |
| Significant | Core section | `well defined relationships` | `well-defined relationships` | Compound modifier needs a hyphen. |
| Significant | Core section | `a AI readable OKF-Bundle` | `an AI-readable OKF bundle` | Article, hyphenation, capitalization, and terminology consistency. |
| Significant | Core section | `descripion` | `description` | Spelling error in a statement about documentation. |
| Significant | YAML heading | `YAML example of  sales_invoice` | `YAML example of sales_invoice` | Extra space and heading should use consistent capitalization. |
| Significant | Silver section | `transforms to source structures to the core data model` | `transforms source structures into the Core Data Model` | Incorrect prepositions and inconsistent capitalization obscure the layer responsibility. |
| Significant | Silver section | `particulaer` and `inovoice` | `particular` and `invoice` | Spelling errors in the worked example. |
| Significant | Silver SQL template | `, a.invoice_number,` | `, a.invoice_number` | Extra comma makes the displayed SQL invalid. |
| Significant | Gold section | `structures for  analysis` | `structures for analysis` | Extra whitespace and awkward spacing. |
| Significant | Gold heading | `Exmple: Dim invoices` | `Example: Invoice dimension` | Spelling error and inconsistent heading style. |
| Significant | Gold example | `the invoices itself` and `tge invoice` | `the invoice itself` and `the invoice` | Grammar and spelling errors. |
| Significant | Gold example | `outputs on line per invoice` | `outputs one row per invoice` | Missing word and incorrect terminology for relational grain. |
| Significant | Gold SQL example | `invoice legal entity` in the filter and `invoice payer` elsewhere | Use one approved role name consistently. | Role labels must match the documented Core type values. |
| Significant | Gold closing | `sturctured`, `recognizeable`, and `layed` | `structured`, `recognisable`, and `laid` | Spelling errors weaken the explanation of AI and automation. |
| Minor | Throughout | `data model`, `Core Data Model`, and `core data model` | Choose capitalization by meaning and apply it consistently. | Terminology consistency. |
| Minor | Throughout | `KPI's` and `macro's` | `KPIs` and `macros` | Plurals do not use apostrophes. |
| Minor | Throughout | `SQL`, `YAML`, `dbt`, and `OKF-Bundle` vary in capitalization and hyphenation | Standardize the forms throughout. | Presentation consistency. |
| Minor | Headings | `### # The generic ingestion template` | `### The generic ingestion template` | Remove the redundant heading marker. |
| Minor | Lists | Several list items begin with lowercase text while nearby prose uses sentence case | Apply one list-capitalization convention. | Consistent Markdown presentation. |
| Minor | Whitespace | Multiple blank lines and trailing spaces occur around examples | Reduce repeated blank lines and remove trailing spaces. | Markdown polish. |
| Minor | Gold SQL example | `invoice payer` and `legal_entity` are exposed as text values | State whether these are business keys or display attributes. | The wording should distinguish key columns from descriptive values. |
| Minor | Closing transition | `UDM principles` and `Universal Data Model` appear in different forms elsewhere | Use `Universal Data Model (UDM)` on first mention, then `UDM`. | Terminology consistency across the series. |

## Minor polish

- Replace `For the bronze layer the following requirements exist` with `The Bronze layer has the following requirements`.
- Use sentence case for layer names in prose and reserve title case for the defined `Core Data Model`.
- Remove repeated introductory phrases such as `If we continue with...` where the invoice example is already established.
- Consider adding a blank line before each fenced SQL block for consistent Markdown rendering.
- Check the image alt text `![alt text](image.png)` and replace it with a descriptive alternative text.
- Ensure the final article ends with a single newline.
- Use `historised` or `historicized` consistently according to the series glossary and target audience.
- Replace `analysis tools` with `analytical tools` where the intended meaning is tooling rather than the activity of analysis.

## Gate decision

`Fail` — the article cannot pass the proofreading gate until the Significant spelling, grammar, terminology, and malformed-example findings are corrected. The architecture review may continue independently, but publication should wait for a clean proofreading report.
