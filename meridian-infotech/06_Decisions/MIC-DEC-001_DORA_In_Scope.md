# MIC-DEC-001 — DORA brought into the framework stack

| Field | Value |
|---|---|
| ID | MIC-DEC-001 |
| Status | Accepted |
| Decided | 21 September 2026 |
| Recorded | 22 September 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Related | MIC-RSK-001, MIC-DEC-002 |

## Context

Two of Meridian Sextant's clients are EU financial entities: Rheinmark Bank AG (Germany) and Veluwe Payments B.V. (Netherlands). Both are bound by the Digital Operational Resilience Act, Regulation (EU) 2022/2554, which has applied since 17 January 2025. Meridian's framework stack (ISO/IEC 27001:2022, SOC 2 Type II, NIST CSF 2.0, DPDP Act 2023, CERT-In Directions 2022, GDPR, ISO/IEC 42001:2023, EU AI Act) did not include it.

DORA binds the financial entity, not Meridian directly. It reaches Meridian through contract: Article 30(2) lists the provisions every ICT services contract must contain (service description, data locations, security, incident assistance, cooperation with authorities, termination rights). Article 30(3) adds further provisions where the service supports a critical or important function, including full access, inspection and audit rights, exit strategies with a mandatory transition period, and participation in threat-led penetration testing where in scope.

## Decision

DORA joins the framework stack as a **contractual flow-down framework**: it applies to Meridian through its EU clients' contracts, not as a directly applicable regulation.

## Alternatives considered

- **Leave DORA out.** Rejected: for an IT services provider to EU banks it is the most directly relevant regulation of all.
- **Treat Meridian as directly regulated.** Rejected: DORA applies directly only to financial entities and, through the oversight framework, to designated critical ICT third-party providers (CTPPs).

## Consequences

- MIC-RSK-001 gains a DORA column in its crosswalk.
- Candidate artifacts: an Article 30 clause mapping per EU client, an exit plan for Rheinmark's critical-function engagement, and an incident-assistance procedure.
- **Standing assumption, monitored:** the Meridian group is not a designated CTPP. The first list, published on 18 November 2025, named 19 providers, including Tata Consultancy Services but not Infosys, Wipro or HCLTech. Designation follows an assessment against four criteria, so the assumption is reviewed whenever a new list is published.

## Sources

- Regulation (EU) 2022/2554 (DORA), Articles 28–30.
- European Supervisory Authorities, press release designating critical ICT third-party providers, 18 November 2025.
---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
