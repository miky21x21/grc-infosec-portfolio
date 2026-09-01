# Cloud Control Gap Assessment — Assessment Plan

**Organisation:** Meridian Infotech Consultancy Ltd. (fictional) — BFS Pune delivery unit
**Author:** Mitchell Swapnil Chatterjee
**Document ID:** MIC-GAP-001
**Version:** 0.1
**Date:** 1 September 2026
**Status:** Scoped — fieldwork not started
**Aligned to:** CIS AWS Foundations Benchmark; ISO/IEC 27001:2022 Annex A; NIST CSF 2.0

---

## 1. Purpose

MIC-RSK-001 identifies MIC-R-006 (misconfiguration in a client-dedicated cloud
landing zone) as a Critical inherent risk with a treatment plan built on continuous
configuration assessment. This document defines how that treatment is tested and
evidenced.

Its secondary purpose is methodological. Most control gap assessments in a portfolio
are written against a hypothetical environment, which means the findings were
decided by the author rather than discovered. This assessment runs against a real
cloud account so that findings are produced by a scanner and remediation is
demonstrable rather than asserted.

## 2. Assessed environment

A dedicated AWS account standing in for a client landing zone, built from
infrastructure-as-code in two states:

- **State A (pre-remediation)** — deliberately weakened against the benchmark
- **State B (post-remediation)** — the same environment after treatment

Both states are published as Terraform so the assessment is reproducible by a
reader rather than taken on trust.

## 3. Benchmark

CIS AWS Foundations Benchmark, covering identity and access management, storage,
logging, monitoring and networking. Findings are mapped onward to ISO/IEC 27001:2022
Annex A and NIST CSF 2.0 so that a control failure is traceable to the register risk
it belongs to.

## 4. Control selection

Selection is driven by MIC-RSK-001, not by what is convenient to scan. Each control
below is chosen because it treats an identified risk.

| Register risk | Control theme | Evidence achievable here |
| :--- | :--- | :--- |
| MIC-R-006 | Configuration baseline, drift detection, logging coverage | **Full** — scanner output before and after, remediation record |
| MIC-R-005 | Public access blocking, encryption at rest, object-level audit logging | **Full** — configuration state and data-event logs |
| MIC-R-001 | Root and privileged MFA enforcement, credential hygiene | **Partial** — the control pattern only; the VDI gateway itself is not represented |
| MIC-R-002 | Unused credential detection, external access analysis | **Partial** — detection only; the workforce-system deprovisioning trigger is out of reach |
| MIC-R-007 | Model invocation logging, guardrails, private endpoint routing | **Partial** — technical controls only; the approved-model register is a process control |

**Not assessed here.** MIC-R-003 (CERT-In reporting), MIC-R-004 (subprocessor
agreements) and MIC-R-008 (Article 50 transparency) are process and contractual
controls with no configuration surface. They are treated in the register and will be
evidenced through procedure and design artifacts, not through this assessment.
Stating this explicitly matters: a gap assessment that silently omits the controls it
cannot test overstates its own coverage.

## 5. Method

1. Deploy State A from Terraform.
2. Baseline scan. Capture raw scanner output as the primary evidence artifact.
3. Record each finding with benchmark reference, affected resource, observed
   configuration, and the framework controls it fails.
4. Rate each finding using the likelihood and impact scales in MIC-MTH-001, so
   ratings are consistent with the register rather than invented for this document.
5. Write the remediation plan, sequenced by rating.
6. Apply remediation as code, producing State B.
7. Re-scan. Record closure, and record any finding that remains open with a reason.
8. Publish the before/after comparison and the residual position.

## 6. Evidence products

| ID | Artifact | Form |
| :--- | :--- | :--- |
| EV-GAP-001 | Baseline scan output (State A) | Scanner report |
| EV-GAP-002 | Findings register with framework mapping | CSV |
| EV-GAP-003 | Remediation plan | Markdown |
| EV-GAP-004 | Post-remediation scan output (State B) | Scanner report |
| EV-GAP-005 | Environment definition, both states | Terraform |

Screenshots are not treated as primary evidence. Machine-generated scanner output
and version-controlled configuration are.

## 7. Cost control

The account runs on promotional credits, so cost is a real constraint on scope
rather than an afterthought.

- Set a budget alert before any resource is created.
- Verify current pricing for any managed security service before enabling it —
  several bill continuously once switched on.
- Confirm the expiry date on the promotional credits; AWS promotional credits carry
  a time limit.
- Prefer services that are free at this scale, and enable chargeable ones for a
  scan window rather than leaving them running.
- Destroy the environment with `terraform destroy` between sessions. The Terraform
  definition is the artifact; the running environment is not.

## 8. Limitations

This assessment is conducted against a purpose-built account, not a production
delivery environment. Three consequences follow, and are stated here rather than
left for a reader to discover:

- **Scale.** A handful of resources cannot exercise the findings that only appear at
  the scale of a real landing zone — account-boundary issues, organisation-wide
  policy conflicts, and cross-account trust relationships.
- **Absence of operational history.** Drift, change management failures and
  monitoring gaps are only visible in an environment that has been running and
  changing over time. This one has not.
- **Author-designed weaknesses.** The misconfigurations in State A were introduced
  deliberately. The scanner finds them independently, which is what makes the
  findings real, but their selection is not a substitute for discovering what an
  unexamined environment actually contains.

The assessment demonstrates method and control literacy. It does not claim to be an
audit of a live estate.

---

## Document control

| Version | Date | Author | Change |
| :--- | :--- | :--- | :--- |
| 0.1 | 1 September 2026 | M. S. Chatterjee | Initial scoping; fieldwork not started |
