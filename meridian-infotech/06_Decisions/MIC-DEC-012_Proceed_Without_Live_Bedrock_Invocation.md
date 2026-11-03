# MIC-DEC-012 — Proceed without live model invocation in the lab

| Field | Value |
|---|---|
| ID | MIC-DEC-012 |
| Status | Accepted |
| Decided | 3 November 2026 |
| Recorded | 3 November 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Related | MIC-DEC-003, MIC-EVD-001 (F-06, EV-010), MIC-RSK-001 (MIC-R-006), MIC-SCP-001 |

## Context

Every Amazon Bedrock model invocation on the lab account has failed since September with `ValidationException: Operation not allowed`, in Mumbai and N. Virginia, despite full administrator permissions (finding F-06). It was re-tested after the first bill closed on 1 October and was still blocked. An AWS support case was opened the same day, and the build log set a fallback decision for 15 October.

The model layer is a supplier dependency. The rest of the lab (identity, logging, cost control, Terraform, evidence handling) does not depend on it.

## Decision

- **The lab stops waiting for Bedrock.** No further effort goes into getting model invocation enabled on this account.
- **The target design does not change.** Meridian Sextant still uses Amazon Bedrock in the scenario, because in-region inference, guardrails and AgentCore are what a real Indian IT services firm on AWS would choose. The design documents keep describing it.
- **What is built and evidenced in the lab** is everything around the model: identity, network, logging, residency guards, the evidence pipeline and Terraform. Where a control needs model output to test (for example the citation check), it is tested with **fixed, recorded sample responses**, clearly labelled as such.
- **F-06 is closed** as a realised supplier risk, accepted with this decision, and recorded in the risk register as MIC-R-006.

## Alternatives considered

- **Keep waiting on the support case.** Rejected: six weeks without a resolution, and the lab's other work was stalling behind it.
- **Switch the lab to another model provider** (for example a direct API). Rejected for now: it would put data outside the AWS residency design that MIC-DEC-005 and MIC-DEC-010 depend on, and it would show a design the scenario would not use.
- **Run a local open-weight model.** Rejected for now: it proves little about the cloud controls this project exists to show, and the lab runs entirely within free credits.

## Consequences

- The portfolio states plainly that model calls are **designed, not run** in the lab. This is recorded in MIC-SCP-001's lab limits and the project README.
- Controls that depend on model output are evidenced as **design plus test harness**, not as production operation.
- The lesson becomes part of the risk register: a single model provider is a single point of failure, and the target design adds an exit plan per DORA Article 28(8).

---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
