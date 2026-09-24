# MIC-DEC-009 — US clients' data lives in a US region, not built in the lab

| Field | Value |
|---|---|
| ID | MIC-DEC-009 |
| Status | Accepted |
| Decided | 22 September 2026 |
| Recorded | 23 September 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Resolves | The open item in MIC-DEC-005 ("US-client content: open") |
| Related | MIC-DEC-005, MIC-DEC-010, MIC-SCP-001 |

## Context

Two Sextant clients, Hartwell Bancorp and Ashgrove Card Services, are US institutions. The lab runs in two regions only, Mumbai and Frankfurt, on free credits that end on 28 February 2027.

US federal banking guidance does **not** impose a general data-localisation rule. OCC Bulletin 2002-16, which remains in force alongside the 2023 interagency guidance on third-party relationships, treats foreign-based service providers as generally permissible, provided the bank manages the risks and critical data remains readily available to it. Hosting US clients' material in India would therefore be legally possible, subject to each bank's agreement.

## Decision

In the scenario, **US clients' material is stored and processed in a US region**. This is a **client-contract choice**, reflecting what US banks commonly ask of a vendor that hosts their material, **not a legal requirement**.

The lab does **not** build a US region. Hartwell's and Ashgrove's material exists in the target design only.

## Alternatives considered

- **Host US clients' material in Mumbai.** Legally possible, but a harder conversation with each bank, and it mixes three jurisdictions in one region.
- **Build a third region in the lab.** Rejected: cost and effort, for a demonstration the EU and India regions already make.

## Consequences

- The lab demonstrates residency with the EU and India only; the US region is recorded in MIC-GAP-001 as target design, not implemented.
- The rationale must always be stated as contractual. Claiming US law requires it would be wrong.

## Sources

- OCC Bulletin 2002-16, "Bank Use of Foreign-Based Third-Party Service Providers" (OCC News Release 2002-43).
- OCC Bulletin 2023-17, "Third-Party Relationships: Interagency Guidance on Risk Management".
---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
