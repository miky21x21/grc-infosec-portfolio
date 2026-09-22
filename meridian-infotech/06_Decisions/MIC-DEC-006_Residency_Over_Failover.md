# MIC-DEC-006 — Residency takes priority over failover

| Field | Value |
|---|---|
| ID | MIC-DEC-006 |
| Status | Accepted |
| Decided | September 2026 |
| Recorded | 22 September 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Related | MIC-DEC-005 |

## Context

Active-active multi-region design keeps a service running when a region fails by moving the workload, and its data, elsewhere. Data residency commitments in client contracts (under GDPR, DORA and RBI expectations) require certain data to stay in a named region. The two goals conflict whenever a failover would move client data across a border.

## Decision

- **Internal-classified content may fail over** between Sextant's regions.
- **Client-confidential content never leaves its residency region**, even if that means the service is unavailable to that client during a regional outage.

## Alternatives considered

- **Full active-active for all content.** Rejected: a single failover would breach residency commitments.
- **In-country failover for Indian content** (Mumbai to Hyderabad). A future option that keeps data in India; not built in the lab.

## Consequences

- Client service levels and continuity plans must state plainly that a regional outage can mean temporary unavailability.
- A region-down test is planned for the control-testing phase to prove that client-confidential content does not move.
---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
