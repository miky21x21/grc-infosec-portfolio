# MIC-DEC-008 — Lab workforce identity: named IAM user, MFA and `aws login`

| Field | Value |
|---|---|
| ID | MIC-DEC-008 |
| Status | Accepted |
| Decided | 22 September 2026 |
| Recorded | 22 September 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Related | MIC-DEC-007, MIC-EVD-001 |

## Context

Sextant's target design federates Meridian's workforce identity (Microsoft Entra ID) into AWS IAM Identity Center, so staff never hold long-term AWS credentials. In the lab, the organization instance of Identity Center would require an AWS Organization, which MIC-DEC-007 rules out. The goal remains the same: **no long-term credentials, anywhere**.

## Decision

- **Root user:** locked with a passkey MFA device, no access keys, and used only for tasks that genuinely require it. Every root session is recorded in MIC-EVD-001.
- **One named IAM user, `mitchell-admin`:** console access with MFA, and permissions granted only through the `Administrators` group, never attached directly to the user.
- **Command line:** `aws login` (AWS CLI 2.36.50) reuses the console sign-in through an OAuth 2.0 authorization-code flow with PKCE. It issues short-lived credentials that refresh automatically about every 15 minutes, within a session of up to 12 hours. **No access keys are created for any identity.**

## Alternatives considered

- **IAM Identity Center account instance.** Not evaluated in the lab; its availability depends on the account's sign-up experience. Can be revisited later.
- **IAM user with access keys.** Rejected: long-term keys on a laptop are exactly the credential this design exists to eliminate.

## Consequences

- `AdministratorAccess` is broad. Narrower roles (for example, a role that Terraform uses to deploy) come later and are recorded as a planned improvement.
- With a single human identity, separation of duties cannot be demonstrated in the lab. This is a documented limitation.
- `~/.aws/config` holds a `login_session` reference and no keys; the evidence is EV-008.

## Sources

- AWS Sign-In User Guide, "Sign in through the AWS Command Line Interface".
- AWS CLI User Guide, "Login for AWS local development using console credentials".
---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
