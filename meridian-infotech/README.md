# Meridian Sextant — a governed AI platform, built and evidenced

> **Sextant is a deliberately narrow, governance-first AI unit: built where the evidence says AI projects succeed, and controlled where the evidence says they fail.**

This project models **Meridian Sextant**, the AI platform unit of a fictional Indian IT services company, Meridian Infotech Consultancy Ltd. Sextant serves five regulated financial institutions in the **US, the EU and India**. The company is simulated; **the AWS environment, its controls and the evidence are real**, built and operated by the author.

## What Sextant does

It turns a bank's compliance and operations questions into **evidence-backed answers**, and a person signs off every one before it leaves.

- **Compliance intelligence:** "How do you meet DORA Article 30(3) for our contract?" The platform follows regulation → contract clause → control → evidence, drafts an answer in which every claim is cited, and an analyst approves it.
- **Operations agents (read-only):** during an incident, an agent reads logs and runbooks and drafts the triage. A human decides and executes any fix.

## How it is built

| Layer | Technology | Key control |
|---|---|---|
| Agents | Amazon Bedrock AgentCore | Cedar policies, deny by default; guardrails on tool traffic; read-only tools in v1 |
| Retrieval | Knowledge bases on S3 Vectors; a curated compliance graph | One store per client; every answer cited |
| Platform | AWS Mumbai and Frankfurt, built entirely in Terraform | Data stays in its jurisdiction; no access keys anywhere |

Evidence is designed in, not gathered at audit time: every control emits logs, which are collected, sealed with a hash and mapped to the frameworks they satisfy.

## Where to look

| Folder | Contents |
|---|---|
| [`00_Scope`](00_Scope) | **MIC-SCP-001**: what is in scope, the clients, the residency rules and the exclusions |
| [`06_Decisions`](06_Decisions) | **MIC-DEC-001 to 011**: each decision with its context, alternatives and consequences |
| [`05_Evidence`](05_Evidence) | **MIC-EVD-001**: the evidence register, findings, root-activity record and build log |
| [`07_Infrastructure`](07_Infrastructure) | **Terraform code**, starting with lab 01: an S3 bucket strangers cannot list |
| [`01_Methodology`](01_Methodology) | Risk methodology, and **MIC-MTH-002**: how this project is run |
| [`02_Registers`](02_Registers) | Risk register |
| [`04_Assessments`](04_Assessments) | Gap assessment |

## Frameworks

ISO/IEC 27001:2022 · ISO/IEC 42001:2023 · SOC 2 · NIST CSF 2.0 · DORA · GDPR · EU AI Act · DPDP Act 2023 · CERT-In Directions · RBI directions and FREE-AI

## Status (24 September 2026)

- **Done:** account security, keyless access and cost controls, recorded as evidence; scope and eleven decision records; the first Terraform build, attacked and proven (EV-011); a CloudTrail audit that corrected the project's own root-activity record (F-08).
- **Next:** risk register update (AI and DORA rows), then the first Terraform build.
- **Open:** Amazon Bedrock model invocation is blocked at account level pending an AWS eligibility review (finding F-06).
- **Limits of the lab:** one AWS account rather than an organization; no US region; no active-active storage. These are target design only, and are recorded as such.

The previous scope for this project (version 1.0, the Pune BFS delivery unit) is preserved in the repository's history.

---

**Author:** Mitchell Swapnil Chatterjee · [LinkedIn](https://www.linkedin.com/in/mitchell-chatterjee-7a042b287)

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
