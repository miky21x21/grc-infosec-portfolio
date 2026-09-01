# Meridian Infotech Consultancy Ltd. — ISMS Programme

**Author:** Mitchell Swapnil Chatterjee
**Document ID:** MIC-README
**Version:** 1.1
**Classification:** Public (fictional scenario)

> **Disclosure:** Meridian Infotech Consultancy Ltd. is a fictional organisation.
> All scenarios, data, findings and evidence in this folder are self-directed
> training exercises. No real client, employer or production data is represented.

---

## 1. The organisation

Meridian Infotech Consultancy Ltd. is a publicly listed Indian IT services
multinational headquartered in Mumbai, with approximately 180,000 employees and
delivery centres across India, Poland, Mexico and the Philippines.

Meridian's service lines are:

- **Application development and maintenance** — building and running client
  business applications
- **Managed infrastructure** — operating client compute, network and endpoint estates
- **Cloud services** — migration to and managed operation of client workloads on
  public cloud (AWS and Azure), including landing zone design and cloud operations
- **AI and data services** — building, deploying and operating machine learning and
  generative AI systems for clients, and supporting the data pipelines behind them

The cloud and AI lines are the growth business, and they are where the unit's
security obligations are least settled. That is deliberate: this programme is built
around the areas where a real ISMS is under the most pressure, not the ones where
control design is already mature.

## 2. Why the scope is narrow

ISO/IEC 27001 certification is never granted to an entire multinational. Clause 4.3
requires the organisation to determine the boundaries and applicability of the ISMS,
and in practice certificates are scoped to a defined delivery unit, site or service
line. Defining a scope that could not realistically be certified would invalidate
everything downstream of it.

This programme therefore covers one delivery unit, not the enterprise.

## 3. ISMS scope statement

> The Information Security Management System covers the design, development,
> maintenance, cloud platform operations and AI system delivery performed by the
> Banking & Financial Services (BFS) vertical from Meridian Infotech Consultancy
> Ltd.'s Pune delivery centre (Hinjawadi Phase II), comprising approximately 1,200
> personnel, in support of three contracted banking clients located in the United
> States and the European Union.
>
> **In scope:** BFS application development and maintenance services; managed
> infrastructure services for in-scope clients; client-dedicated cloud landing
> zones on AWS and Azure operated by the BFS cloud practice; AI and machine
> learning systems built, deployed or operated by the BFS AI practice on behalf of
> in-scope clients, including the data pipelines supporting them; the Pune delivery
> centre physical premises and BFS-designated secure work areas; client-dedicated
> virtual desktop infrastructure; BFS supporting corporate services (BFS HR
> operations, BFS procurement liaison).
>
> **Out of scope:** All other Meridian verticals and delivery centres; corporate
> functions delivered from Mumbai HQ; client-owned infrastructure operated inside
> client data centres under client control; the underlying cloud service provider
> infrastructure, which sits on the provider's side of the shared responsibility
> model and is assured through the provider's own certifications; general-purpose
> AI models procured from third-party providers, where Meridian's obligations are
> those of a downstream deployer rather than a model provider.

**Note on the shared responsibility model.** Cloud provider infrastructure being out
of scope is not the same as it being unassessed. The boundary itself is a control
point: which side of the line each control falls on is documented per service in
MIC-SOA-001, and provider assurance is handled as third-party risk under
A.5.19–A.5.22.

## 4. Interested parties and their requirements

| Interested party | Requirement | Source |
| :--- | :--- | :--- |
| US banking client (2 contracts) | Annual SOC 2 Type II report; third-party risk assessment; right to audit | Master services agreement |
| EU banking client (1 contract) | GDPR Article 28 processor obligations; EBA outsourcing register inclusion; AI Act deployer support obligations | Data processing agreement; AI services schedule |
| Indian regulator | Personal data protection obligations as a Data Processor | DPDP Act, 2023 |
| CERT-In | Incident reporting within 6 hours; 180-day log retention within India | CERT-In Directions, April 2022 |
| EU market surveillance authorities | Transparency obligations for AI systems interacting with natural persons or generating synthetic content | EU AI Act Article 50 |
| Cloud service providers (AWS, Azure) | Customer-side obligations under the shared responsibility model; acceptable use | Cloud provider agreements |
| Meridian corporate | Group ISMS policy conformance; ISO/IEC 27001:2022 certification maintenance | Internal mandate |
| BFS employees | Clear, workable security procedures; privacy of employee data | Internal |

## 5. Why this framework stack

Meridian's obligations arrive from four independent directions, which is the normal
condition for an Indian delivery organisation running cloud and AI workloads for
regulated foreign clients:

- **Contractual flow-down.** Meridian is a third party to regulated banks. Its
  clients' own supervisory obligations flow down through contract, which is what
  drives the SOC 2 Type II requirement and the right-to-audit clauses.
- **Indian statute.** DPDP Act 2023 and CERT-In Directions apply because Meridian
  operates in India, regardless of where its clients are.
- **Corporate mandate.** ISO/IEC 27001:2022 certification is a commercial
  prerequisite for bidding on enterprise work.
- **AI-specific obligation.** Delivering AI systems to an EU client brings the EU AI
  Act into scope, and makes ISO/IEC 42001:2023 the natural management-system
  companion to 27001. It is also a sales requirement in practice: banking clients
  ask for AI governance assurance before letting a supplier near a model.

These are not stacked for display. A single control frequently satisfies several at
once, which is why this programme maintains **one control set with a crosswalk**
rather than parallel framework-specific registers. See
[`02_Registers/`](./02_Registers/).

### Where the AI Act actually bites, as at September 2026

Misstating this is the fastest way to make an AI governance artifact look dated, so
the position is set out explicitly:

| Obligation | Status | Relevance to Meridian |
| :--- | :--- | :--- |
| Prohibited practices; AI literacy | Applicable since 2 February 2025 | Applies now |
| GPAI model provider obligations | Applicable since 2 August 2025 | Meridian is a downstream deployer, not a model provider — not directly applicable |
| General application, including Article 50 transparency | Applicable since 2 August 2026 | **Applies now.** Any client-facing assistant or synthetic content Meridian builds carries disclosure duties |
| High-risk, Annex III standalone | Deferred to 2 December 2027 | Relevant to a bank's creditworthiness models; Meridian's duty is to support its client's compliance, not to carry it |
| High-risk, Annex I product-embedded | Deferred to 2 August 2028 | Not applicable to this scope |

The high-risk deferrals came from the Digital Omnibus on AI, which entered into
force on 27 July 2026. The deferral did **not** touch Article 50, which is why
transparency appears as a live risk in MIC-RSK-001 while conformity assessment does
not.

## 6. Artifacts in this folder

| ID | Artifact | Location | Status |
| :--- | :--- | :--- | :--- |
| MIC-SCP-001 | Context & scope | Sections 1–5 of this README | Drafted |
| MIC-MTH-001 | Risk assessment methodology | [`01_Methodology/`](./01_Methodology/) | Drafted |
| MIC-RSK-001 | Risk register | [`02_Registers/`](./02_Registers/) | In progress — 8 rows of a target 15–20 |
| MIC-AST-001 | Asset inventory | `02_Registers/` | Not started |
| MIC-SOA-001 | Statement of Applicability | `02_Registers/` | Planned |
| MIC-STD-001 | Access control standard | `03_Policies/` | Planned |
| MIC-GAP-001 | Cloud control gap assessment | [`04_Assessments/`](./04_Assessments/) | Scoped — fieldwork not started |
| MIC-EVD-001 | Evidence index | `05_Evidence/` | Planned |

MIC-SCP-001 is currently held inline in this README rather than as a separate
document. It will be extracted into `00_Scope/` when the context analysis is
expanded beyond the scope statement.
