# MIC-DEC-003 — Scope reductions for Sextant v1

| Field | Value |
|---|---|
| ID | MIC-DEC-003 |
| Status | Accepted |
| Proposed | 21 September 2026 |
| Accepted | 22 September 2026 |
| Recorded | 22 September 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Related | MIC-DEC-002, MIC-RSK-001 |

## Context

An evidence review on 21 September 2026 checked the Sextant design against published real-world data. The findings that bear on scope:

- MIT's 2025 "GenAI Divide" study reported that 95% of the enterprise GenAI pilots it examined showed no measurable profit-and-loss impact. Critics attribute much of that to missing baselines rather than technical failure. The same work found specialised vendor-led projects succeeded roughly twice as often as internal builds.
- AWS documents that guardrails attached to a Bedrock agent screen user input and the final answer, but not tool input and tool output.
- Confidential GPU inference is not available on AWS: Nitro Enclaves cannot use a GPU.
- Human reviewers of AI output are prone to fatigue and rubber-stamping.

## Decision

1. **Two products in v1:** compliance intelligence (the flagship), and operations agents that are **read-only advisers**. No v1 tool changes anything in a client's systems; a human executes every fix through the client's change process.
2. **Roadmap, not v1:** the confidential AI tier, the AI assurance service, the agent registry and earned autonomy.
3. **No customer personal data** enters the platform: only runbooks, contracts, controls, regulations and evidence.
4. **A curated graph**, built from structured crosswalks, rather than one extracted automatically from raw text.
5. **Baseline metrics recorded before go-live**, and human reviewers tested with seeded errors.

## Alternatives considered

- **All five products in v1.** Rejected on the evidence above and on the capacity of a solo build.

## Consequences

Fixes what is built in October and November 2026, and removes the most dangerous part of the guardrail gap, because read-only tools cannot cause harm through a manipulated call.
---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
