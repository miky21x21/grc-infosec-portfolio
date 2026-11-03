# MIC-AIA-001 — AI System Impact Assessments: Meridian Sextant

| Field | Value |
|---|---|
| ID | MIC-AIA-001 |
| Version | 1.0 |
| Date | 3 November 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Owner | Governance and Risk Office Lead |
| Approver | Sextant AI Risk Committee |
| Standards | ISO/IEC 42001:2023 clause 6.1.4 and Annex A.5.2 to A.5.5; ISO/IEC 42005:2025 (guidance); NIST AI RMF MAP function |
| Covers | SXT-AI-01 Compliance intelligence; SXT-AI-02 Operations agents (MIC-INV-001) |
| Related | MIC-POL-001, MIC-CLS-001, MIC-RSK-001, MIC-SOA-002 |

## Summary

| System | Who it affects most | Highest impact if it fails | Rating before controls | Rating after controls | Decision |
|---|---|---|---|---|---|
| SXT-AI-01 Compliance intelligence | Bank compliance staff, their auditors and regulators | A bank tells its regulator something untrue about its own controls | High | Medium | Approved for v1 with conditions |
| SXT-AI-02 Operations agents | Bank engineers during incidents; the bank's customers indirectly | A wrong triage lengthens an outage of a banking service | High | Medium | Approved for v1, read-only, with conditions |

Neither system makes decisions about individual people, and neither is high-risk under the EU AI Act (MIC-CLS-001). The impacts that matter are on the banks' ability to give accurate statements to regulators, and on the availability of services their customers use.

## 1. The assessment process (A.5.2)

**When an assessment is required**
- Before any AI system goes live, and before it is offered to a new client.
- Before a change in model, data sources, tools, autonomy or intended use (the triggers in MIC-CLS-001 section 5).
- At least yearly for every system in MIC-INV-001.

**Who does it.** The system owner drafts it; the Governance and Risk Office challenges it; a Client Lead checks the client's view; the AI Risk Committee approves it. Nobody approves an assessment of a system they built.

**Steps**
1. Describe the system: purpose, intended use, users, data, capability, oversight (from MIC-INV-001).
2. Identify who is affected, directly and indirectly.
3. List what could go wrong for each: errors, misuse, failures, foreseeable misuse.
4. Rate severity and likelihood with the scales in MIC-MTH-001, before and after controls.
5. Decide: approve, approve with conditions, or reject. Conditions become controls in MIC-RSK-001 and MIC-SOA-002.
6. Record and review (A.5.3): this document, versioned, kept for the life of the system plus three years.

**Severity scale for people and society** (used alongside MIC-MTH-001's impact scale)

| Level | Meaning |
|---|---|
| Severe | Lasting harm to people's rights, money or access to essential services, or a false statement to a regulator that is relied on |
| Significant | Harm that is reversible but costly, or a service disruption customers notice |
| Moderate | Wasted effort or delay, caught before it reaches anyone outside the bank |
| Minor | Inconvenience only |

## 2. SXT-AI-01 Compliance intelligence

**What it does.** Drafts answers to compliance and audit questions from the requesting bank's own documents and graph, with every claim cited. An analyst approves each answer before it leaves Sextant.

**Who is affected (A.5.4)**

| Group | How they are affected |
|---|---|
| Bank compliance staff | Rely on answers to respond to auditors and regulators |
| Auditors and regulators | Read statements based on the answers |
| Sextant analysts | Approve answers; carry accountability; exposed to automation bias |
| Bank customers (indirect) | Protected by the bank's controls, which the answers describe |
| Individuals named in client documents | Their personal data may sit in contracts and policies used for retrieval |

**What could go wrong**

| Impact | Severity | Likelihood before | Controls (conditions of approval) | Likelihood after |
|---|---|---|---|---|
| An unsupported claim reaches a regulator, so a bank misstates its own controls | Severe | Likely | Automated citation check blocks release; seeded faulty answers measure reviewer catch rate; reasons recorded for every approval (R-002) | Unlikely |
| One bank's confidential content appears in another bank's answer | Severe | Possible | Per-client store and attribute check; canary documents fail the release (R-001) | Rare |
| Analysts approve without reading because the system is usually right | Significant | Likely | Edit-rate monitoring, seeded faults, automation-bias training (MIC-POL-001 s6) | Possible |
| Personal data in client documents is processed outside its jurisdiction | Significant | Possible | Jurisdiction-level residency; in-region models only (R-005) | Rare |
| Bank staff think a person wrote the answer | Moderate | Possible | Every answer labelled AI-drafted and human-approved (R-011) | Rare |

**Societal impact (A.5.5).** Low. The system serves compliance teams, not the public. The one wider effect is positive if it works and negative if it fails: regulators' trust in AI-assisted compliance evidence. That is why an unsupported claim is rated Severe.

**Decision:** approved for v1 with all conditions above. Re-assess before any client uses answers without analyst approval, which is not permitted in v1.

## 3. SXT-AI-02 Operations agents

**What it does.** During a bank's production incident, reads tickets, logs and runbooks through read-only tools and drafts a triage. An engineer decides and acts through the bank's change process.

**Who is affected (A.5.4)**

| Group | How they are affected |
|---|---|
| Bank engineers | Use the triage under time pressure |
| Bank customers (indirect) | Experience the outage the triage is meant to shorten |
| Sextant engineers | Accountable for the agents' design and limits |
| Individuals in logs | Logs may contain customer identifiers |

**What could go wrong**

| Impact | Severity | Likelihood before | Controls (conditions of approval) | Likelihood after |
|---|---|---|---|---|
| Text hidden in a log line steers the triage, and an engineer follows it | Significant | Possible | Tool output treated as data; instruction-like content flagged; raw evidence shown beside each step; red-team tests (R-003) | Unlikely |
| An agent gains a tool that can change production | Severe | Possible | Read-only tools only in v1; pipeline blocks unlisted tools (R-004) | Rare |
| A confident but wrong triage delays the real fix | Significant | Possible | Confidence shown; engineer decides; runbook step cited | Unlikely |
| Customer identifiers in logs are exposed more widely than needed | Moderate | Possible | Redaction of personal data from agent inputs and stored logs (SoA A.8.11) | Unlikely |
| Model provider unavailable during an incident | Moderate | Possible | Engineers work without the agent; exit plan for a second provider (R-006) | Possible |

**Societal impact (A.5.5).** Low. The indirect effect on bank customers is shorter or longer outages. Because the agents cannot act, the worst case is a slower fix, not an action the agent takes on its own.

**Decision:** approved for v1, read-only, with all conditions above. **Any write capability (the v2 earned-autonomy roadmap) needs a new assessment and EU AI Act re-classification before it is built**, because an agent that acts changes the severity of every row above.

## 4. Lab note

Both systems are designed but not run in the lab, because model invocation is blocked (MIC-DEC-012). The controls that depend on model output (citation check, seeded faults, red-team cases) are specified here and will be tested with fixed, labelled sample responses.

## 5. Review

Next review: before any trigger in section 1, and no later than November 2027.

---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer.
