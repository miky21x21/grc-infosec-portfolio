# MIC-DEC-007 — Single-account lab build, without AWS Organizations

| Field | Value |
|---|---|
| ID | MIC-DEC-007 |
| Status | Accepted |
| Decided | 22 September 2026 |
| Recorded | 22 September 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Related | MIC-DEC-008, MIC-GAP-001 |

## Context

Sextant's target architecture is a multi-account AWS Organization: separate accounts for workloads, a sandbox and a log archive, with guardrails applied centrally. The lab account is on the AWS **free plan**. On that plan, creating an AWS organization automatically upgrades the account to a paid plan, and any remaining Free Tier credits expire immediately. The project's standing rule is that it runs entirely on credits, with no personal spend, until the free plan ends on 28 February 2027.

## Decision

The lab is built in **one AWS account**. Separation between workloads is logical rather than by account: consistent tags (`Owner`, `Project`), naming conventions, IAM permissions and a dedicated, tightly restricted bucket in place of a separate log-archive account. The multi-account Organization remains the documented target architecture.

## Alternatives considered

- **Create an Organization.** Rejected: the credits would be forfeited on the spot.
- **Open several standalone accounts.** Rejected: more to secure and track, with no shared guardrails anyway.

## Consequences

- Organization-level controls cannot be demonstrated in the lab: service control policies, an organization-wide CloudTrail trail, delegated administration and account-level isolation.
- MIC-GAP-001 will record those controls as **target design, not implemented in the lab**, rather than claiming them.
- This is an honest limitation, and a useful one to explain: knowing which controls depend on an Organization is part of designing one.

## Sources

- AWS documentation on Free Tier account plans (free and paid), and on IAM Identity Center organization and account instances.
---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
