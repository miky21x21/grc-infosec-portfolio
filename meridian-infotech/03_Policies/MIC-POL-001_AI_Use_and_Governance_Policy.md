# MIC-POL-001 — AI Use and Governance Policy: Meridian Sextant

| Field | Value |
|---|---|
| ID | MIC-POL-001 |
| Version | 1.0 |
| Effective | 3 November 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Owner | Governance and Risk Office Lead |
| Approver | Head of Sextant, on the recommendation of the Sextant AI Risk Committee |
| Standards | ISO/IEC 42001:2023 clause 5.2 and Annex A.2 (AI policy); ISO/IEC 27001:2022 A.5.10 |
| Treats | MIC-RSK-001: R-002, R-004, R-008, R-011 |
| Related | MIC-INV-001, MIC-CLS-001, MIC-SCP-001 |

## 1. Purpose

Sextant builds AI for regulated banks and uses AI in its own work. This policy sets the rules for both, so that every AI output a client receives is approved by a named person, and no client data reaches an AI system that has not been approved for it.

## 2. Scope

All Sextant staff, contractors and interns; every AI system Sextant provides to clients; and every AI tool used for Sextant work, on any device.

## 3. Principles

1. **A person is accountable for every output.** No AI-drafted answer, triage or document reaches a client until a named analyst or engineer approves it.
2. **Approved systems only.** Only systems and tools listed as approved in MIC-INV-001 may be used, and only for the data shown there.
3. **Client data stays in its client's boundary.** It is used only for that client's service, only in that client's jurisdiction, and never to train or tune a model.
4. **Least capability.** AI systems get the smallest set of tools and data access their purpose needs. In v1, no AI system can change anything in a client's systems.
5. **Disclosed, not hidden.** Clients are told where AI drafted an output and who approved it.

## 4. Approval of AI systems, models and tools

- Any new AI system, model, model version, agent tool or wider data access needs **AI Risk Committee approval before use**, recorded in MIC-INV-001.
- The request states the purpose, data, capability, human oversight, supplier terms (training on inputs, retention, processing region) and the EU AI Act classification (MIC-CLS-001).
- **Write-capable agent tools are not approved in v1**, whatever the request.
- The deployment pipeline blocks any agent tool not listed as approved.

## 5. Rules for staff

| Data | May be used in |
|---|---|
| Public information | Any approved tool, and personal AI tools |
| Meridian internal (no client content) | Approved staff tools in MIC-INV-001 section 2 |
| Client content, logs, tickets, documents, personal data | **Only** the client's own Sextant system (SXT-AI-01 or SXT-AI-02) |

- Never put client content, credentials, keys or personal data into a personal AI tool, a browser extension or any tool not approved for it.
- Do not record or transcribe client meetings with AI unless the client agrees at the start of the call.
- Check AI output against its sources before approving it. If a claim has no supporting source, remove it or mark it unsupported; never approve it to save time.

## 6. Human oversight

- Reviewers see the AI output, its sources and the model version, and record **accept, edit or reject with a reason**.
- The Governance and Risk Office places known-faulty outputs in review queues each month and reports how many were caught. A reviewer with a near-zero edit rate is checked for rubber-stamping.
- Approval authority is set per client service. Reviewers are trained on automation bias before they approve.

## 7. Training

Everyone completes AI literacy training on joining and yearly, and acknowledges this policy. Reviewers also complete oversight training before approving client outputs. Records are kept for the life of the employment plus three years.

## 8. Incidents

Report the same day, to the Governance and Risk Office, if client data reached an unapproved AI tool, an AI output that reached a client was wrong, or an AI system acted outside its approved scope. These are handled as security incidents; client and regulator notifications follow the incident response plan and each client's contract (including DORA and CERT-In timelines where they apply).

## 9. Exceptions and breaches

Exceptions need written AI Risk Committee approval, a time limit and a compensating control, and are recorded in MIC-INV-001. Breaches are handled under Meridian's disciplinary process.

## 10. Review

Reviewed at least yearly, and whenever a new AI system goes live, a model changes, a client is added or the EU AI Act or its guidance changes.

---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer.
