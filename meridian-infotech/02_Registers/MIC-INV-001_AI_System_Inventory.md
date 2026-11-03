# MIC-INV-001 — AI System Inventory: Meridian Sextant

| Field | Value |
|---|---|
| ID | MIC-INV-001 |
| Version | 1.0 |
| Date | 3 November 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Owner | Governance and Risk Office Lead |
| Approver | Sextant AI Risk Committee |
| Standards | ISO/IEC 42001:2023 Annex A (A.4 resources, A.6 life cycle, A.9 use); NIST AI RMF GOVERN 1.6 |
| Related | MIC-SCP-001, MIC-POL-001, MIC-CLS-001, MIC-RSK-001, MIC-DEC-003, MIC-DEC-012 |

Every AI system Sextant builds, operates or lets its staff use for client work is listed here. Nothing goes live, and no tool or model is changed, unless its row is approved first. The deployment pipeline checks agent tools against this list (MIC-RSK-001, R-004).

## 1. AI systems Sextant provides to clients

| ID | System | Purpose | Clients | Model and platform | What it can do | Human oversight | EU AI Act (MIC-CLS-001) | Key risks | Status |
|---|---|---|---|---|---|---|---|---|---|
| SXT-AI-01 | Compliance intelligence | Drafts evidence-backed answers to compliance and audit questions | Ashgrove, Rheinmark, Anvaya | Foundation model through Amazon Bedrock, in-region; client knowledge base and curated graph | Read the requesting client's own documents and graph; draft cited answers | Analyst approves every answer before release; edits and reasons recorded | Not high-risk; transparency label applied (Art. 50) | R-001, R-002, R-005, R-006, R-011 | Approved for v1. Lab: designed, not invoked (MIC-DEC-012) |
| SXT-AI-02 | Operations agents | Drafts incident triage: likely cause, runbook step, confidence | Hartwell, Veluwe | Bedrock AgentCore; Cedar policies, deny by default | **Read-only** access to tickets, logs and runbooks. No write tools in v1 | Engineer decides and executes any fix through the client's change process | Not high-risk; transparency label applied | R-003, R-004, R-006, R-011 | Approved for v1, read-only. Lab: designed, not invoked |

**Approved agent tools (SXT-AI-02, v1):** `read_ticket`, `query_logs` (time-bounded, per client), `read_runbook`. Any other tool, and any tool that writes, is rejected by the pipeline in v1.

## 2. AI tools Sextant staff use

| ID | Tool | Use | Data allowed | Decision | Conditions |
|---|---|---|---|---|---|
| SXT-AI-03 | Enterprise coding assistant (company workspace) | Code completion and review for Sextant's own platform code | Sextant source code; never client data | Approved | Company workspace with SSO; no training on Meridian content under business terms; suggestions reviewed like any code change |
| SXT-AI-04 | Meeting transcription in the corporate collaboration suite | Internal meeting notes | Internal; client meetings only with the client's consent | Restricted | Consent at the start of client calls; transcripts kept 90 days |
| SXT-AI-05 | Personal AI chat tools (any provider) | — | Public information only | Banned for client or Meridian data | Uploads blocked from client bays and managed devices (R-008) |
| SXT-AI-06 | Browser AI extensions | — | — | Banned | Removed and blocked by device management; they can read client portal pages |

## 3. Designed but not operated (roadmap)

| System | Version | Why it is not in this inventory's approved set |
|---|---|---|
| Agent registry and earned autonomy | v2 | Would allow agents to gain write actions after a record of good performance; needs its own impact assessment and committee approval |
| Confidential AI tier | v3 | Model inference inside confidential computing; not built |
| AI assurance service | v3 | Testing clients' own AI systems; a new service with its own risks |

Each roadmap item gets a row in sections 1 or 2, and a fresh classification in MIC-CLS-001, before it is operated.

## 4. How this inventory is kept current

- **New system, tool, model or tool permission:** request to the Governance and Risk Office; decision by the AI Risk Committee; row added before go-live.
- **Monthly:** compare deployed agent tools with section 1, and AI service use seen in proxy logs with section 2.
- **Quarterly:** full review with the AI Risk Committee; supplier terms for each model and tool rechecked (R-006).

---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer.
