# MIC-SCP-001 — Scope of the Management System: Meridian Sextant

| Field | Value |
|---|---|
| ID | MIC-SCP-001 |
| Version | 2.0 |
| Date | 23 September 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Supersedes | Version 1.0, the Pune BFS delivery unit scope held in the project README |
| Standards | ISO/IEC 27001:2022 clause 4.3; ISO/IEC 42001:2023 clause 4.3 |
| Related | MIC-DEC-002, 003, 004, 005, 006, 009, 010 |

## 1. Scope statement

> The information security and AI management systems cover **Meridian Sextant**, the AI platform unit of Meridian Infotech Consultancy Ltd, based in Pune, India. They cover the design, operation and assurance of governed compliance-intelligence and operations-advisory services for regulated financial institutions in the United States, the European Union and India, delivered from Meridian-owned AWS environments.

## 2. The organisation and why this scope

Meridian Infotech Consultancy Ltd is a publicly listed Indian IT services company headquartered in Mumbai, with about 180,000 employees and delivery centres in India, Poland, Mexico and the Philippines. Financial services is its largest industry; it also serves manufacturing, retail, healthcare, communications and energy clients.

Its traditional business, building and running software for clients on an effort basis, is under pressure as AI automates that work. **Meridian Sextant is the company's governed response**: a deliberately narrow unit of about 320 people that builds and operates AI for Meridian's financial-services clients and makes governance part of the service. Sextant sells **outcomes, not software licences**: clients buy answered audit requests and triaged incidents, and never license or install the platform.

The unit's engineers work from secure client bays on Meridian's Pune delivery floor, which Meridian owns and operates (a contractor offshore development centre).

## 3. Services in scope

**Compliance intelligence (v1).** A client, auditor or regulator asks a question, for example "how does Meridian meet DORA Article 30(3) for our contract?". The platform checks the requester's access, retrieves the relevant regulations, contract clauses, controls and evidence from that client's own curated graph and documents, and drafts an answer in which every claim is cited. A Sextant analyst reviews and signs off every answer before it leaves. The output is an evidence pack, and gaps found along the way become findings.

**Operations agents (v1).** During a client's production incident, an agent reads the ticket, logs and runbooks through read-only tools and drafts a triage: likely cause, the matching runbook step, and its confidence. A human engineer decides and executes any fix through the client's own change process. **No v1 tool can change anything in a client's systems.**

**Not operated (roadmap):** the agent registry and earned autonomy (v2); the confidential AI tier and the AI assurance service (v3). They are designed but not run, and so are outside this scope until they are.

## 4. Clients and other interested parties

| Client | Country and type | Sextant service | What binds Sextant |
|---|---|---|---|
| Hartwell Bancorp | US, regional retail bank | Operations agents | Contract; US interagency third-party guidance; SOC 2 Type II evidence |
| Ashgrove Card Services | US, card issuer | Compliance intelligence | Contract; PCI DSS flows down, though Sextant holds no card data |
| Rheinmark Bank AG | Germany, commercial bank | Compliance intelligence | DORA Article 30, as a critical function; GDPR |
| Veluwe Payments B.V. | Netherlands, payment institution | Operations agents on Veluwe's own AWS tenancy | DORA Article 30; GDPR; shared responsibility |
| Anvaya Bank Ltd | India, private-sector bank (RBI) | Compliance intelligence | RBI IT outsourcing and IT governance directions; FREE-AI expectations; DPDP |

Other interested parties: the clients' regulators (reached through the clients' contracts); Meridian group functions (Chief Risk Officer, Group CISO, Internal Audit, the privacy lead); suppliers (AWS, and model providers reached through Amazon Bedrock); and Sextant's employees.

## 5. Boundaries

**Organisational.** Sextant's five teams (platform engineering, AI engineering, cloud security engineering, client leads, and the governance and risk office), led by the Head of Sextant, who reports to the Group CEO. The governance and risk office reports to the Group Chief Risk Officer, with a dotted line to the Head of Sextant, so that it can challenge freely. The Sextant AI Risk Committee approves every new agent, model change and, in future, autonomy promotion.

**Physical.** The Pune delivery-floor areas used by Sextant staff, including the client bays they work from.

**Technical.** Sextant's AWS environment in two regions: Asia Pacific (Mumbai) and Europe (Frankfurt). US clients' material is held in a US region in the target design (MIC-DEC-009). Asia Pacific (Hyderabad) is reserved as a future in-country failover region for Indian content.

**Who owns what:**

| Layer | Owned by | In scope? |
|---|---|---|
| Sextant AWS environment: platform, knowledge bases, graphs, agents, logs | Meridian | Yes — the core |
| Pune delivery floor, client bays, endpoints | Meridian | Yes (supporting) |
| Meridian corporate identity, network and email | Meridian group | Interfaces only |
| Client applications, databases and production data | Client | No — covered by contract |
| Client virtual desktops and jump hosts | Client | No — interface only |
| Veluwe's AWS tenancy, administered by Sextant | Client | Shared — by contract |
| AWS infrastructure and Bedrock models | AWS | Supplier — shared responsibility |

## 6. Data residency and processing

These rules implement MIC-DEC-010.

1. **Stored in the home region.** EU clients' material is stored in Frankfurt; Indian clients' material in Mumbai; US clients' material in a US region (target design).
2. **Processed only within the same jurisdiction.** AI processing may run anywhere inside the client's jurisdiction (the EU, India or the US) and never outside it. This also gives active-active processing within each jurisdiction.
3. **Human access from India is a declared, contracted exception.** Pune analysts view EU clients' results through sessions that keep no copies in India. Under EU guidance this remote access is a transfer, so each EU client's data processing agreement carries the Standard Contractual Clauses (Module 2, controller to processor) and a transfer impact assessment.
4. **Client-specific exceptions** (for example, a bank requiring one named data centre) are written into that client's contract and override rule 2 for that client.
5. **No customer personal data** enters the platform: only runbooks, contracts, controls, regulations and evidence (MIC-DEC-003).

**Logs are split by what they contain.** CERT-In's directions require an Indian entity to keep ICT logs for 180 days. Its FAQ allows storage outside India if the logs can be produced to CERT-In within a reasonable time, though some practitioners read it as requiring a copy in India. So:

- **Security and access logs** (sign-ins, API activity, allow and deny decisions) contain no client content. A copy is kept in Mumbai for 180 days, which satisfies even the strictest reading.
- **Content-bearing logs** (for example, an EU client's questions and answers) stay in the client's jurisdiction, and can be produced to CERT-In within a reasonable time if required.
- Sextant keeps no financial-transaction records, so the separate requirement to store those in India does not arise.

**Active-active storage** would need a second region inside each jurisdiction (Mumbai with Hyderabad; Frankfurt with another EU region). That is part of the target design and is not built in the lab.

## 7. Applicable requirements

| Framework | How it applies to Sextant |
|---|---|
| ISO/IEC 27001:2022 | The information security management system |
| ISO/IEC 42001:2023 | The AI management system |
| SOC 2 Type II | Assurance evidence for US clients |
| NIST CSF 2.0 | Common language, especially with US clients |
| DORA | Contractual, through EU clients' Article 30 clauses (MIC-DEC-001) |
| GDPR | Sextant is a processor for EU clients; transfers for human access covered by the Standard Contractual Clauses |
| EU AI Act | Applies to AI provided to EU clients; the v1 products are believed not to be high-risk uses (classification memo pending) |
| DPDP Act 2023 and Rules 2025 | Data Processor for clients' data; Data Fiduciary for Meridian's own staff data |
| CERT-In Directions 2022 | Six-hour incident reporting; 180-day log retention (see section 6) |
| RBI directions and FREE-AI | Through Anvaya's contract (MIC-DEC-004) |
| US banking guidance | Foreign-based providers are generally permissible, provided critical data remains readily available to the bank |

## 8. Exclusions and why

| Excluded | Why |
|---|---|
| The rest of the Meridian group, including its other business units | A separate management system; Sextant depends only on the interfaces listed in section 5 |
| The Pune BFS delivery unit's own services | Governed by the group; only the floor areas Sextant uses are in scope |
| Clients' own environments and production data | Owned and controlled by the clients; Meridian's obligations are contractual |
| The Physical AI lab (world models) | A different unit, serving different industries, with a different risk profile |
| Roadmap products (section 3) | Not operated |

## 9. Real and simulated

**Real:** the AWS account, every control built in it, and all recorded evidence (MIC-EVD-001). **Simulated:** the company, its clients, their documents and its headcount. The lab is one AWS account (MIC-DEC-007) with keyless access (MIC-DEC-008). The multi-account design, the US region and active-active storage are target design only, and MIC-GAP-001 will record them as not implemented rather than claim them.

## 10. Review

The scope is reviewed at least once a year, and whenever a client, region, product or major regulation changes. Owner: Head of Sextant. Approval: the Sextant AI Risk Committee.

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | September 2026 | Scope: the Pune BFS delivery unit (held in the README) |
| 2.0 | 23 September 2026 | Scope moves to Meridian Sextant (MIC-DEC-002); five clients; jurisdiction-level residency (MIC-DEC-010) |

---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
