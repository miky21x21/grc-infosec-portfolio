# MIC-DEC-002 — ISMS scope moves to Meridian Sextant

| Field | Value |
|---|---|
| ID | MIC-DEC-002 |
| Status | Accepted |
| Decided | 21 September 2026 |
| Recorded | 22 September 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Supersedes | The Pune BFS delivery unit scope in the current MIC-SCP-001 (project README) |
| Related | MIC-DEC-001, MIC-DEC-004, MIC-DEC-005 |

## Context

The original ISMS scope was Meridian's Pune BFS delivery unit: an offshore delivery centre whose engineers work inside banks' own environments. That scope is almost entirely physical and endpoint security, with little cloud or AI content. The portfolio's purpose is cloud security and AI governance, and the real Indian IT services industry is moving from effort-based services toward platform-led, outcome-linked delivery.

## Decision

The ISMS scope becomes **Meridian Sextant**, a new AI-native platform unit inside Meridian. Sextant is Pune-based and serves Meridian's financial-services clients through a platform running in Meridian's own AWS estate. The Pune BFS delivery unit remains in the scenario as supporting context: its secure bays and managed endpoints are where Sextant's engineers work.

The name comes from the sextant's "noon sight", which fixes a ship's exact position as the sun crosses the meridian. The unit's job is to give each client an exact fix on where it stands against its obligations, with evidence.

## Alternatives considered

- **Keep the Pune delivery unit as scope.** Rejected: it would demonstrate a 2010s offshore model rather than cloud and AI governance.
- **Scope the whole Meridian group.** Rejected: far too broad for one person to evidence credibly.

## Consequences

- MIC-SCP-001 (currently inline in the project README) must be rewritten for Sextant. Until then, the README describes the superseded scope.
- The central design change: client documents now land in Meridian's own estate (knowledge bases and graphs). This raises obligations everywhere, from residency (MIC-DEC-006) to DORA critical-function status.
- Sextant's commercial model ("sells outcomes, not software licences") is a working assumption and is not part of this decision.
---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
