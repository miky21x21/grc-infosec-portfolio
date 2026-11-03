# 02_Registers

| ID | Artifact | Status |
| :--- | :--- | :--- |
| MIC-RSK-001 | [Risk register](./MIC-RSK-001_Risk_Register.csv) | Version 2.0, 3 November 2026: 11 risks for the Meridian Sextant scope |
| MIC-INV-001 | [AI system inventory](./MIC-INV-001_AI_System_Inventory.md) | Version 1.0, 3 November 2026 |
| MIC-AST-001 | [Asset inventory](./MIC-AST-001_Asset_Inventory.md) | Version 1.0, 3 November 2026 |
| MIC-SOA-001 | [Statement of Applicability: ISO/IEC 27001:2022](./MIC-SOA-001_SoA_ISO27001.csv) | Version 1.0, 3 November 2026: all 93 Annex A controls |
| MIC-SOA-002 | Statement of Applicability: ISO/IEC 42001:2023 | Next |

Registers are published as CSV or Markdown so they render as tables in the browser.

## What changed in MIC-RSK-001 version 2.0

Version 1.0 (8 risks, September 2026) was written for the earlier scope, the Pune BFS delivery unit. When the scope moved to Meridian Sextant (MIC-DEC-002, MIC-SCP-001 v2.0), most of those risks no longer described the system in scope. Version 2.0 replaces them with 11 risks drawn from Sextant's own design and decisions:

- **AI-specific risks** from the v1 products: cross-client retrieval (R-001), unsupported claims passing human review (R-002), prompt injection through tool output (R-003), unapproved agent tools (R-004) and missing AI disclosure (R-011).
- **Risks the lab has already shown to be real**: dependence on a single model provider, realised as finding F-06 (R-006), and the reliability of evidence and access records (R-009, R-010).
- **DORA and residency risks** from the EU and Indian clients (R-005, R-007).
- **Workforce use of personal AI tools** (R-008), treated by the AI use and governance policy MIC-POL-001.

Version 1.0 remains in the repository's history.

## Crosswalk columns

MIC-RSK-001 carries nine framework columns so that one control set can be traced to every applicable obligation: ISO/IEC 27001:2022 Annex A, ISO/IEC 42001:2023 Annex A, SOC 2 TSC, NIST CSF 2.0, **DORA** (added in version 2.0, per MIC-DEC-001), DPDP Act 2023, CERT-In 2022, GDPR and the EU AI Act.

Blank cells are meaningful. A risk with no ISO/IEC 42001 or EU AI Act mapping has no AI dimension, and saying so is more useful than forcing a reference. ISO/IEC 42001 references are given at Annex A control-group level (A.2 to A.10).

Where an EU AI Act article is cited for a system that is not high-risk, the column says the principle is **applied voluntarily**. MIC-CLS-001 records why the v1 products are not high-risk.

## How to read the Statements of Applicability

Every Annex A control is listed, applicable or not. **Implementation status** is stated plainly:

| Status | Meaning |
|---|---|
| Implemented (lab) | Built in the real AWS lab account and evidenced in MIC-EVD-001 |
| Partly implemented (lab) | Some of the control is built and evidenced; the rest is designed |
| Designed | Specified in a decision, policy or register, but not built |
| Planned | Accepted as needed; not yet specified |
| Inherited | Provided by Meridian group functions or by AWS under shared responsibility. For the simulated company these are stated, not evidenced |
| Excluded | Not applicable, with the reason given |

Most controls are Designed because the company is simulated. Only what the lab account proves is marked Implemented.

## Open gaps in this register

- **Scoring method.** MIC-MTH-001 still names roles from the earlier BFS scope (for example the BFS Delivery Head). The scales are unchanged; the role names will be updated in its next revision.
- **Not yet covered:** physical security of the client bays, backup and recovery, and model drift once live models are in use.

---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer.
