# MIC-AST-001 — Asset Inventory: Meridian Sextant

| Field | Value |
|---|---|
| ID | MIC-AST-001 |
| Version | 1.0 |
| Date | 3 November 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Owner | Governance and Risk Office Lead |
| Standards | ISO/IEC 27001:2022 A.5.9 (inventory), A.5.12 (classification); ISO/IEC 42001:2023 A.4.2 (resource documentation) |
| Related | MIC-SCP-001, MIC-RSK-001, MIC-INV-001, MIC-SOA-001, MIC-SOA-002 |

This inventory lists the assets that the risk register and the Statement of Applicability refer to. It is kept at the level that risks are assessed: one row per group of assets that share an owner, a location and a protection need. Individual AWS resources are tracked by Terraform and tags, not here.

## Classification scheme

| Level | Meaning | Example |
|---|---|---|
| **Restricted** | Disclosure could breach a client contract or a regulation, or expose every client at once | Client documents, credentials, logs with client content |
| **Confidential** | Meridian business information not for outside parties | Platform design, internal risk records |
| **Internal** | For staff; little harm if disclosed | Internal procedures |
| **Public** | Published deliberately | This portfolio |

## Assets

| ID | Asset | Type | Owner | Location and jurisdiction | Classification | Real or simulated | Risks |
|---|---|---|---|---|---|---|---|
| AST-AIS-001 | Compliance intelligence (SXT-AI-01): retrieval, graph queries, answer drafting, citation check | AI system | Head of AI Engineering | AWS Mumbai (India clients), Frankfurt (EU clients); US region in target design | Restricted | Designed; not run in the lab (MIC-DEC-012) | R-001, R-002, R-006, R-011 |
| AST-AIS-002 | Operations agents (SXT-AI-02): read-only tools, Cedar policies | AI system | Head of AI Engineering | AWS; for Veluwe, on Veluwe's own AWS tenancy | Restricted | Designed; not run in the lab | R-003, R-004, R-006, R-011 |
| AST-DAT-001 | Client knowledge bases and curated compliance graphs, one set per client | Information | Client Lead for each client | In the client's own jurisdiction (MIC-DEC-010) | Restricted | Simulated | R-001, R-005 |
| AST-CLD-001 | Sextant AWS environment: account, IAM, networking, storage, regions | Cloud service | Head of Cloud Security Engineering | AWS account; Mumbai and Frankfurt enabled; Hyderabad reserved | Restricted | **Real**: one lab account (MIC-DEC-007) | R-005, R-007, R-009 |
| AST-IDN-001 | Identities: root user, `mitchell-admin`, MFA devices, `aws login` sessions | Identity | Head of Cloud Security Engineering | AWS IAM (global) | Restricted | **Real** (EV-001, EV-003, EV-009) | R-009 |
| AST-LOG-001 | Logs and evidence: CloudTrail, the root-activity report, hash-verified evidence files | Information | Governance and Risk Office Lead | AWS Mumbai; evidence copies in this repository | Restricted (logs); Public (published evidence, redacted) | **Real** (EV-012, EV-013) | R-010 |
| AST-COD-001 | Infrastructure code and project records (Terraform, this repository) | Software and records | Head of Platform Engineering | GitHub (public); state kept local and never committed (MIC-DEC-011) | Public (code); state Restricted | **Real** | R-009, R-010 |
| AST-EPT-001 | Endpoints and client bays on the Pune delivery floor | Hardware and premises | Meridian group IT (Sextant interfaces) | Pune, India | Restricted | Simulated | R-008 |
| AST-SUP-001 | Suppliers: AWS, and model providers reached through Amazon Bedrock | Third-party service | Head of Sextant | Per supplier agreement | Confidential (agreements) | AWS real; model access blocked in the lab (F-06) | R-006, R-007 |
| AST-PPL-001 | Sextant staff (about 320): engineers, analysts, client leads, governance and risk office | People | Head of Sextant | Pune, India | n/a | Simulated | R-002, R-008 |

## What changed

The risk register (MIC-RSK-001 v2.0) referred to six asset IDs before this inventory existed. All six are now defined above. AST-IDN-001, AST-COD-001, AST-SUP-001 and AST-PPL-001 were added so the Statement of Applicability can name the asset each control protects.

## Keeping it current

Reviewed quarterly with the risk register, and whenever a client, region, AI system or supplier is added. A new AI system also needs a row in MIC-INV-001.

---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Assets marked **Real** are the author's own AWS lab account, code and evidence.
