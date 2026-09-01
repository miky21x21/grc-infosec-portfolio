# 02_Registers

| ID | Artifact | Status |
| :--- | :--- | :--- |
| MIC-RSK-001 | [Risk register](./MIC-RSK-001_Risk_Register.csv) | In progress — 8 rows of a target 15–20 |
| MIC-AST-001 | Asset inventory | Not started |
| MIC-SOA-001 | Statement of Applicability | Planned |

Registers are published as CSV so they render as tables in the browser.

## Crosswalk columns

MIC-RSK-001 carries seven framework columns so that one control set can be traced to
every applicable obligation: ISO/IEC 27001:2022 Annex A, ISO/IEC 42001:2023 Annex A,
SOC 2 TSC, NIST CSF 2.0, DPDP Act 2023, CERT-In 2022, GDPR and the EU AI Act.

Blank cells are meaningful. A risk with no ISO/IEC 42001 or EU AI Act mapping has no
AI dimension, and saying so is more useful than forcing a reference.

## Open gaps in this register

- **Asset IDs are forward references.** Rows cite `AST-CLD-003`, `AST-SFT-002`,
  `AST-DAT-004`, `AST-CLD-007`, `AST-AIS-001` and `AST-AIS-002`. No asset inventory
  using that scheme exists yet; MIC-AST-001 will resolve them.
- **Coverage is incomplete at 8 rows.** Physical security at the delivery centre,
  backup and recovery, change management, secure development, and model drift or
  performance degradation in production AI systems are the known gaps.
