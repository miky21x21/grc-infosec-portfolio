# MIC-MTH-002 — Working Method

| Field | Value |
|---|---|
| ID | MIC-MTH-002 |
| Version | 1.0 |
| Date | 24 September 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Related | MIC-MTH-001 (risk methodology), MIC-EVD-001, MIC-DEC-011 |

How this project is run: how facts, decisions, evidence, code and cost are handled. It exists so that anyone reviewing the portfolio can see not only what was built, but how.

## 1. Principles

1. **Only publish what can be defended.** Nothing is committed that the author cannot explain under questioning.
2. **Every real-world fact has a primary source.** Claims from secondary summaries, vendors or AI assistants are checked before use; unsupported figures are left out.
3. **Status is always visible.** Material statements are marked as decided, working assumption, proposed or open.
4. **The simulation is declared.** The company and its clients are fictional; the AWS environment and its evidence are real.

## 2. Decisions

Every significant design choice gets a decision record in `06_Decisions` (MIC-DEC-NNN): context, decision, alternatives considered, consequences, and sources. Records change status (Proposed to Accepted) rather than being rewritten, and later decisions refine earlier ones explicitly.

## 3. Evidence

**Three kinds of evidence.** Design (a control is configured correctly), operation (it ran that way over time) and effectiveness (it held when tested). All three are sought, not only screenshots of settings.

**How it is produced:**

1. **Generate:** every control is built to emit evidence, to CloudWatch Logs or a restricted log bucket. Logs follow residency: logs containing client content stay in the client's jurisdiction.
2. **Collect:** evidence is pulled into dated files, increasingly by script.
3. **Seal:** files are hashed (SHA-256) and the hash is recorded, so later alteration is detectable.
4. **Map:** each item gets an EV number in MIC-EVD-001, linked to its control and framework references.
5. **Publish carefully:** only redacted extracts go into the public repository. Account IDs, canonical user IDs and email addresses are covered with solid boxes, never blur. Raw logs stay in AWS.

**Records are checked against logs.** Human records are reconciled against CloudTrail; where they disagree, the log wins and the record is corrected (F-08).

## 4. Building

- **Infrastructure as code only.** Resources are created by Terraform, not by clicking in the console.
- **Plan, review, apply the reviewed plan.** `terraform plan -out`, then `terraform apply` on that saved plan.
- **Scratch work stays outside the repository; state is never committed** (MIC-DEC-011).
- **Break it, fix it, prove it.** Where possible, a control is tested with the same technique an attacker would use (EV-011).
- **Commits:** one commit per artifact. Scripts commit locally and never push; every change is reviewed before `git push`.

## 5. Identity and access

- **Root** is locked with a passkey and a backup authenticator, and used only for tasks that require it. Every root session is recorded and then reconciled against CloudTrail.
- **Daily work** is done as the named administrator, `mitchell-admin`, with MFA.
- **Command line and Terraform** use the `aws login` session: short-lived credentials, no access keys, and no credentials exported into the terminal. Sessions end with `aws logout`.
- **Check the region** before every console action.

## 6. Cost

- A monthly budget measured **without credits**, so real usage is visible.
- Anything built for a test is **destroyed the same day**.
- Everything is torn down before the free plan ends on **28 February 2027**.

## 7. Practice

- **Daily:** a build block, a hands-on challenge block, and a three-line log (did, stuck, learned). The log names causes, not just symptoms.
- **Weekly challenge themes:** identity, breaking things, data and networks, incidents, governance, and automation. Each week's finding becomes a control, and then a script that checks it.
- **Monthly:** one short public field note on a control, how it was tested, and what the evidence showed.
- **Teach-back:** an artifact is finished only when it can be explained in two minutes without notes.

## 8. What the portfolio will show

A front-door README; infrastructure in Terraform with a scan in CI and one deliberate misconfiguration caught and fixed; identity and residency guards; the agent path with Cedar policies and guardrails on tool traffic; retrieval with citations over a curated graph; an AI threat model mapped to the OWASP Top 10 for Agentic Applications; a control test report; evidence as code; the GRC set (scope, risk register, crosswalk, gap assessment, decisions); an AI governance pack; monthly field notes; a short walkthrough video; and a few clearly labelled design memos on where the field is heading.
---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
