# AI Governance & Cloud GRC Portfolio

**Mitchell Swapnil Chatterjee** · AI governance and cloud GRC
[LinkedIn](https://www.linkedin.com/in/mitchell-chatterjee-7a042b287) · [mitchellswapnil.com](https://mitchellswapnil.com)

> **Disclosure:** Every organisation in this repository is fictional. Scenarios, clients and their data are self-directed exercises created to demonstrate GRC and AI governance work. Where a record describes the AWS lab environment, that environment is real and operated personally by the author. No real client, employer or production data appears anywhere in this repository.

---

## Two projects, two ends of the AI market

| Project | Who | AI role | What it shows |
| :--- | :--- | :--- | :--- |
| [**Meridian Sextant**](./meridian-infotech/) | 320-person AI platform unit of a fictional Indian IT services firm, serving five regulated banks in the US, EU and India | **Builds and provides** AI systems | An AI and information security management system built and evidenced on a real AWS account: scope, 12 decision records, a risk register crosswalked to nine frameworks, an AI system inventory, AI policy, EU AI Act classification, Terraform, and hash-verified evidence |
| [**Harrow & Vale LLP**](./harrow-vale-ai-governance/) | 48-person accounting firm in Ohio and Manchester | **Uses** third-party AI tools | A complete white-label AI governance evidence pack: shadow-AI discovery, tool decisions, a one-page policy, training records and evidence-backed answers to a customer's security questionnaire |

Meridian goes deep: one organisation, many obligations, real cloud controls. Harrow & Vale goes practical: what a small firm actually needs when its biggest customer starts asking about AI.

---

## How the work is traced

Both projects follow the same chain, so any control can be traced back to the risk that justified it and forward to the evidence that proves it operates:

```
Context & Scope → Risk Assessment → Risk Register → Controls and Decisions
      → Policies → Assessments → Findings → Remediation → Evidence
```

Every artifact carries a document ID, version and date. Decisions are recorded with their alternatives and consequences, and findings stay in the record even when they show the author's own mistakes (see Meridian's F-08 and F-09).

---

## Repository structure

```
grc-infosec-portfolio/
├── README.md
├── meridian-infotech/              ← Meridian Sextant (flagship)
│   ├── 00_Scope/                   ← scope, clients, residency, lab limits
│   ├── 01_Methodology/             ← risk methodology, working method
│   ├── 02_Registers/               ← risk register, asset and AI inventories, SoAs
│   ├── 03_Policies/                ← information security and AI policies
│   ├── 04_Assessments/             ← EU AI Act classification, cloud gap assessment plan
│   ├── 05_Evidence/                ← evidence register, findings, build log, lab evidence
│   ├── 06_Decisions/               ← decision records MIC-DEC-001 to 012
│   └── 07_Infrastructure/          ← Terraform
├── harrow-vale-ai-governance/      ← small-business AI governance sample pack
└── foundations/                    ← study notes, not portfolio deliverables
```

---

## Frameworks and standards referenced

**Management systems and control frameworks:** ISO/IEC 42001:2023 (AI management system, Annex A.2 to A.10) · ISO/IEC 27001:2022 · NIST AI RMF 1.0 · NIST CSF 2.0 · SOC 2 Trust Services Criteria · CIS AWS Foundations Benchmark

**Regulation:** EU AI Act (Regulation 2024/1689, as amended by the 2026 Digital Omnibus) · DORA · GDPR and UK GDPR · India's DPDP Act 2023 · CERT-In Directions 2022 · RBI directions and FREE-AI expectations · FTC Safeguards Rule · IRC §7216

**Questionnaires:** Shared Assessments SIG · CSA AI-CAIQ

---

## Status (3 November 2026)

| Artifact | Project | Status |
| :--- | :--- | :--- |
| Scope (MIC-SCP-001 v2.1) | Meridian | Done |
| Decision records MIC-DEC-001 to 012 | Meridian | Done |
| Risk register (MIC-RSK-001 v2.0, 11 risks) | Meridian | Done |
| AI system inventory (MIC-INV-001) | Meridian | Done |
| Information security policy (MIC-POL-002) | Meridian | Done |
| AI use and governance policy (MIC-POL-001) | Meridian | Done |
| EU AI Act classification (MIC-CLS-001) | Meridian | Done |
| AWS lab controls and evidence (MIC-EVD-001) | Meridian | Ongoing |
| Asset inventory (MIC-AST-001) | Meridian | Done |
| Statement of Applicability: ISO/IEC 27001 (MIC-SOA-001, 93 controls) | Meridian | Done |
| Statement of Applicability: ISO/IEC 42001 (MIC-SOA-002, 38 controls) | Meridian | Done |
| AI system impact assessment | Meridian | Next |
| Cloud gap assessment (MIC-GAP-001) | Meridian | Plan written; to be re-scoped before fieldwork |
| Evidence pack (HV-AIG-PACK-001 v1.1) | Harrow & Vale | Done |

This table is kept honest: planned means planned, and next means not yet written.
