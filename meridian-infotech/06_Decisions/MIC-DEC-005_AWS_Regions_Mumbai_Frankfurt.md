# MIC-DEC-005 — AWS regions: Mumbai and Frankfurt

| Field | Value |
|---|---|
| ID | MIC-DEC-005 |
| Status | Accepted |
| Decided | September 2026 |
| Recorded | 22 September 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Related | MIC-DEC-004, MIC-DEC-006, MIC-DEC-007 |

## Context

Sextant must show data residency working in practice, for clients in the EU and India. The lab runs on free credits that end on 28 February 2027, so every additional region costs real budget and effort.

## Decision

- **Asia Pacific (Mumbai), `ap-south-1`:** Meridian-internal content and Indian-client content. Also the region the AWS CLI defaults to.
- **Europe (Frankfurt), `eu-central-1`:** EU-client content only.
- **US-client content: open.** Hosting it in India may not be acceptable to US banks; a US region is deferred on cost.

## Alternatives considered

- **One region.** Rejected: it cannot demonstrate residency.
- **Add a US region now.** Deferred on cost and effort.
- **Asia Pacific (Hyderabad), `ap-south-2`,** is already enabled on the lab account. It is noted as a possible in-country failover region for Indian content (see MIC-DEC-006), not used for now.

## Consequences

- Managed GraphRAG is available to the Frankfurt clients but is not listed for Mumbai (see MIC-DEC-004).
- Every build step must check the active region: resources created in the wrong region are both a residency failure and a cost leak.
---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
