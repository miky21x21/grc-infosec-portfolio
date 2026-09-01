# GRC & Information Security Portfolio

**Mitchell Swapnil Chatterjee**
Information Security / GRC Analyst — CompTIA Security+ scheduled October 2026
[LinkedIn](https://www.linkedin.com/in/mitchell-chatterjee-7a042b287) · [mitchell.s.chatterjee@gmail.com](mailto:mitchell.s.chatterjee@gmail.com)

> **Disclosure:** Every organisation in this repository is fictional. All scenarios,
> data, findings and evidence are self-directed training exercises created to
> demonstrate GRC methodology. No real client, employer or production data is
> represented anywhere in this repository.

---

## What this portfolio demonstrates

Two end-to-end programmes, each traceable from context and scope through risk
identification, control selection, assessment and remediation tracking.

| Project | Sector | Regulatory drivers | Control frameworks |
| :--- | :--- | :--- | :--- |
| [Meridian Infotech Consultancy](./meridian-infotech/) | IT services delivery — applications, cloud and AI — to US/EU banking clients | DPDP Act 2023, CERT-In Directions 2022, GDPR (processor), EU AI Act, client contractual flow-down | ISO/IEC 27001:2022, ISO/IEC 42001:2023, SOC 2 Type II |
| [Divine Healthcare](./divine-healthcare/) | US healthcare provider | HIPAA Security Rule | NIST CSF 2.0 |

The two projects are deliberately different. Meridian is an Indian delivery
organisation carrying simultaneous Indian and international obligations across
cloud and AI workloads, and is where the multi-framework control crosswalk lives.
Divine Healthcare is a single-jurisdiction US scenario built on HIPAA and NIST CSF,
which exercises depth against one regulation rather than reconciliation across
several.

---

## Traceability model

Both programmes follow the same chain, so any control can be traced backwards to
the risk that justified it and forwards to the evidence that proves it operates:

```
Context & Scope → Risk Assessment → Risk Register → Control Selection (SoA)
      → Policies & Standards → Control Assessment → Findings → Remediation → Evidence
```

Every artifact carries a document ID, version and date. Registers are published as
CSV so they render as tables in the browser.

---

## Repository structure

```
grc-infosec-portfolio/
├── README.md
├── meridian-infotech/
│   ├── README.md              ← scenario, scope statement, framework rationale
│   ├── 00_Scope/              ← context, interested parties, scope boundary
│   ├── 01_Methodology/        ← risk assessment methodology, scoring rubrics
│   ├── 02_Registers/          ← asset inventory, risk register, SoA
│   ├── 03_Policies/           ← policies and standards
│   ├── 04_Assessments/        ← cloud gap assessment, control testing, findings
│   └── 05_Evidence/           ← evidence index (EV-xxx)
├── divine-healthcare/         ← HIPAA / NIST CSF scenario, not yet started
└── foundations/               ← study notes, not portfolio deliverables
```

---

## Frameworks and standards referenced

**Management systems and control frameworks**

- **ISO/IEC 27001:2022** — ISMS clauses 4–10 and Annex A controls
- **ISO/IEC 42001:2023** — AI management system; Annex A controls A.2–A.10
- **ISO/IEC 27005** — risk management methodology
- **SOC 2 Type II** — Trust Services Criteria (Security, Confidentiality, Availability)
- **NIST CSF 2.0** — Govern, Identify, Protect, Detect, Respond, Recover
- **CIS AWS Foundations Benchmark** — cloud configuration baseline

**Regulation**

- **Digital Personal Data Protection Act, 2023 (India)**
- **CERT-In Directions, April 2022** — incident reporting and log retention
- **GDPR** — processor obligations (Articles 28, 32, 33)
- **EU AI Act (Regulation 2024/1689)**, as amended by the Digital Omnibus on AI
  (in force 27 July 2026) — Article 50 transparency applicable from 2 August 2026;
  Annex III high-risk obligations deferred to 2 December 2027
- **HIPAA Security Rule** (Divine Healthcare)

---

## Status

| Artifact | Project | Status |
| :--- | :--- | :--- |
| Context & scope | Meridian | Drafted |
| Risk assessment methodology | Meridian | Drafted |
| Risk register | Meridian | In progress — 8 rows of a target 15–20 |
| Asset inventory | Meridian | Not started |
| Statement of Applicability | Meridian | Planned |
| Access control standard | Meridian | Planned |
| Cloud control gap assessment | Meridian | Scoped — fieldwork not started |
| All artifacts | Divine Healthcare | Not started |

This table is maintained honestly. Planned means planned, and not started means
nothing has been written yet.
