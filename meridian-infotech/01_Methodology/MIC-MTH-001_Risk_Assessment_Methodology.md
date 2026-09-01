# Risk Assessment Methodology

**Organisation:** Meridian Infotech Consultancy Ltd. (fictional) — BFS Pune delivery unit
**Author:** Mitchell Swapnil Chatterjee
**Document ID:** MIC-MTH-001
**Version:** 1.0
**Effective date:** 1 September 2026
**Next review:** 1 September 2027
**Owner:** Head of Information Security, BFS Delivery
**Aligned to:** ISO/IEC 27001:2022 Clause 6.1.2; ISO/IEC 27005

---

## 1. Purpose

This document defines how information security risk is identified, analysed,
evaluated and treated within the ISMS scope. ISO/IEC 27001 Clause 6.1.2 requires a
documented risk assessment process that produces consistent, valid and comparable
results. Without a published rubric, risk scores are opinions rather than
assessments, and two assessors will not reach the same number.

## 2. Scope

Applies to all information assets, processes, systems and third parties within the
ISMS scope defined in MIC-SCP-001.

## 3. Roles

| Role | Responsibility |
| :--- | :--- |
| Risk Owner | Accountable for the risk and for accepting residual risk. Always a named role, never an individual's name, so the register survives staff turnover. |
| Control Owner | Accountable for the design and operation of a treatment control. |
| Information Security Manager | Facilitates assessment, maintains the register, reports to management review. |
| BFS Delivery Head | Approves risk acceptance above the appetite threshold. |

## 4. Risk identification

Risks are expressed in a fixed sentence structure so that each entry is testable:

> **[Threat source]** exploiting **[vulnerability]** affecting **[asset]**, resulting
> in **[consequence]**.

Example: *An external attacker exploiting absent MFA on the client VDI gateway
(AST-CLD-003), resulting in unauthorised access to EU banking client personal data.*

Entries that do not fit this structure are usually issues, not risks, and are routed
to the corrective action log instead.

## 5. Likelihood scale

Likelihood is assessed **before** treatment (inherent) and again **after** planned
treatment (residual).

| Score | Rating | Definition | Indicative frequency |
| :--- | :--- | :--- | :--- |
| 5 | Almost certain | Expected to occur in most circumstances; already occurring or observed in the environment | More than once per year |
| 4 | Likely | Will probably occur; known active threat and a weak or absent control | Once per 1–2 years |
| 3 | Possible | Might occur; plausible threat with a partially effective control | Once per 2–5 years |
| 2 | Unlikely | Could occur but not expected; effective control in place | Once per 5–10 years |
| 1 | Rare | Occurs only in exceptional circumstances; strong, tested control | Less than once per 10 years |

## 6. Impact scale

Impact is scored as the **highest** applicable value across the four dimensions
below. A risk that is minor financially but severe for regulatory exposure scores on
the regulatory dimension.

| Score | Rating | Client & contractual | Regulatory | Operational | Financial (INR) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 5 | Severe | Contract termination; loss of client | Regulatory enforcement action; CERT-In reportable breach of client personal data | Delivery halted more than 5 days | Over 25 crore |
| 4 | Major | Formal client escalation; right-to-audit invoked; SLA penalties | Reportable incident with regulator notification | Delivery degraded 2–5 days | 5–25 crore |
| 3 | Moderate | Client concern raised; remediation plan demanded | Internal non-conformity; audit finding | Delivery degraded up to 2 days | 50 lakh – 5 crore |
| 2 | Minor | Noted in service review | Minor control deviation, self-corrected | Localised disruption under 1 day | 5–50 lakh |
| 1 | Negligible | No client-visible effect | No regulatory relevance | No measurable disruption | Under 5 lakh |

## 7. Risk evaluation

**Risk score = Likelihood × Impact** (range 1–25).

|  | **I1** | **I2** | **I3** | **I4** | **I5** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **L5** | 5 | 10 | 15 | 20 | 25 |
| **L4** | 4 | 8 | 12 | 16 | 20 |
| **L3** | 3 | 6 | 9 | 12 | 15 |
| **L2** | 2 | 4 | 6 | 8 | 10 |
| **L1** | 1 | 2 | 3 | 4 | 5 |

| Score | Rating | Required response |
| :--- | :--- | :--- |
| 20–25 | Critical | Treatment plan within 5 working days; BFS Delivery Head informed immediately; remediation within 30 days |
| 12–19 | High | Treatment plan within 15 working days; remediation within 90 days |
| 6–11 | Medium | Treatment plan at next quarterly review; remediation within 180 days |
| 1–5 | Low | Accept and monitor; reassess annually |

## 8. Risk appetite

The BFS delivery unit accepts residual risk scoring **5 or below** without further
escalation.

Residual risk scoring **6 to 11** requires documented acceptance by the Risk Owner.

Residual risk scoring **12 or above** requires documented acceptance by the BFS
Delivery Head, and any such acceptance affecting client personal data must be
disclosed to the affected client under the applicable data processing agreement.

**Two exceptions override appetite entirely.** Regardless of calculated score, the
unit does not accept: (a) any residual non-conformity with CERT-In incident
reporting timelines, or (b) any control gap that would constitute a breach of a
signed Article 28 processor obligation. These are treated as mandatory-treatment
regardless of scoring.

## 9. Risk treatment

Four options, per ISO/IEC 27001 Clause 6.1.3:

| Option | Applied when | Example |
| :--- | :--- | :--- |
| **Modify** | A proportionate control can reduce likelihood or impact | Enforce phishing-resistant MFA on the client VDI gateway |
| **Avoid** | The risk-bearing activity is not essential | Cease storing client production extracts on delivery-centre file shares |
| **Share** | A third party can absorb part of the consequence | Cyber liability insurance; contractual indemnity with a subprocessor |
| **Retain** | Residual risk is within appetite, or treatment cost exceeds exposure | Accept low-scoring residual risk on a public-facing marketing asset |

Selected controls are recorded in the Statement of Applicability (MIC-SOA-001), with
justification for every Annex A control included or excluded.

## 10. Control crosswalk principle

The unit maintains **one control set**, mapped to every applicable framework, rather
than separate registers per framework. A single control such as quarterly access
recertification satisfies ISO/IEC 27001 A.5.18, SOC 2 CC6.2, the DPDP Act's
reasonable security safeguards obligation, and evidences the access-governance
element of GDPR Article 32 simultaneously.

Maintaining parallel registers produces divergence, duplicated evidence collection,
and contradictory findings between audits. The crosswalk columns in MIC-RSK-001
exist for this reason.

## 11. Review cadence

| Trigger | Action |
| :--- | :--- |
| Quarterly | Full register review with Risk Owners |
| On material change | Reassessment before go-live (new client, new subprocessor, architecture change) |
| Post-incident | Reassessment of the affected risk within 10 working days |
| Annually | Methodology itself reviewed and re-approved |

## 12. Limitations of this assessment

This is a qualitative methodology. Scores are ordinal, not cardinal — a risk scoring
20 is not "twice as bad" as one scoring 10, and scores should not be summed to
produce an aggregate exposure figure. Quantitative methods (FAIR) would be
appropriate if the unit later needs monetary loss expectancy for insurance or capital
decisions.

---

## Document control

| Version | Date | Author | Change |
| :--- | :--- | :--- | :--- |
| 1.0 | 1 September 2026 | M. S. Chatterjee | Initial issue |
