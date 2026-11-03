# MIC-POL-002 — Information Security Policy: Meridian Sextant

| Field | Value |
|---|---|
| ID | MIC-POL-002 |
| Version | 1.0 |
| Effective | 3 November 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Owner | Governance and Risk Office Lead |
| Approver | Head of Sextant |
| Standards | ISO/IEC 27001:2022 clause 5.2 and Annex A 5.1 |
| Related | MIC-SCP-001, MIC-POL-001, MIC-RSK-001, MIC-SOA-001, MIC-SOA-002 |

## 1. Purpose

Five regulated banks trust Sextant with their documents, contracts, logs and the questions their regulators ask. This policy commits Sextant to protecting that information, sets the objectives the information security management system works towards, and names the rules that put it into practice.

## 2. Scope

The information security management system defined in MIC-SCP-001: Meridian Sextant's people, its Pune delivery floor and client bays, its AWS environment, its AI systems, and the information it handles for its clients. It applies to all Sextant staff, contractors and suppliers working on Sextant services.

## 3. Commitments

The Head of Sextant commits to:

1. **Protect client information** so that it is seen only by the people and systems that client's service needs, stays in its client's jurisdiction, and is available when the client needs it.
2. **Meet every legal, regulatory and contractual requirement** listed in MIC-SCP-001 section 7, including DORA, GDPR, India's DPDP Act, the CERT-In Directions, RBI directions and the EU AI Act, and the security terms of each client contract.
3. **Manage risk deliberately**: assess it with a published method (MIC-MTH-001), treat it, and accept residual risk only at the level in that method.
4. **Provide the people, time and tools** the management system needs.
5. **Improve continually**, using findings, incidents, audits and reviews to change practice, and recording each change.

## 4. Objectives

Objectives are reviewed at each management review. Progress is reported quarterly to the Head of Sextant.

| Objective | Measure | Target |
|---|---|---|
| No client content disclosed to another client | Canary documents found in another client's output | Zero |
| No client data in unapproved AI tools | Confirmed incidents from monthly discovery | Zero; any case reported the same day |
| Privileged access kept to people and moments that need it | Unexplained root or administrator sessions after CloudTrail reconciliation | Zero |
| Evidence clients can rely on | Evidence files whose SHA-256 no longer matches its record | Zero |
| Incidents reported on time | Reports made within contractual and regulatory deadlines | 100% |
| Staff who know the rules | Staff trained and acknowledged within 30 days of joining, and yearly | 100% |
| Risks treated on time | High and Critical risks with a treatment plan within the method's deadline | 100% |

## 5. Principles

- **Least privilege and separation.** Access is per client, per role, and no wider than the task needs.
- **No standing secrets.** No long-lived access keys; human access uses MFA and short sessions (MIC-DEC-008).
- **Designed in, evidenced continuously.** Controls produce their own logs and evidence; evidence is not assembled at audit time.
- **Residency by design.** Client content is stored and processed only within its jurisdiction (MIC-DEC-010).
- **A person is accountable.** Every change, AI output and exception has a named owner and approver.
- **Honest records.** Findings, including our own mistakes, stay in the record with their resolution.

## 6. Roles

| Role | Responsibility |
|---|---|
| Head of Sextant | Owns this policy and the management system; approves risk acceptance above appetite |
| Governance and Risk Office Lead | Runs the management system: risk, policy, evidence, internal checks; reports independently to the Group Chief Risk Officer |
| Head of Cloud Security Engineering | Identity, network, logging and cloud configuration controls |
| Head of Platform Engineering | Secure development, change and continuity of the platform |
| Head of AI Engineering | Security and oversight controls in the AI systems |
| Client Leads | Each client's contractual and regulatory requirements |
| Sextant AI Risk Committee | Approves AI systems, models and tool changes (MIC-POL-001) |
| Every member of staff | Follows the policies, completes training and reports events the same day |

## 7. Topic-specific policies and standards

This policy is supported by the documents below. Each traces to the controls in the Statements of Applicability and the risks in MIC-RSK-001.

| Document | Status |
|---|---|
| MIC-POL-001 AI use and governance policy | In force |
| MIC-STD-001 Access control standard | Planned |
| Incident response plan, including AI incident playbooks | Planned |
| Supplier and model-provider security standard | Planned |
| Logging and evidence standard | Planned |
| Group policies used by Sextant: acceptable use, HR security, physical security, device management | In force (Meridian group) |

## 8. Compliance and exceptions

Compliance is checked monthly by the Governance and Risk Office and reported quarterly. Exceptions need written approval from the Head of Sextant, a time limit and a compensating control, and are recorded in the risk register. Breaches are handled under Meridian's disciplinary process.

## 9. Communication

This policy is available to all Sextant staff on joining and on the intranet, acknowledged yearly, and shared with clients and other interested parties on request.

## 10. Review

Reviewed at least yearly and at each management review, and whenever the scope, a client, a region, a supplier or a major regulation changes.

---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer.
