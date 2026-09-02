# DH-BSL-001 — Control Baseline Register

> **Simulated engagement.** Divine Healthcare is a fictional 340-bed hospital created
> as a self-directed learning exercise. No real organisational or patient data appears here.

**Organisation:** Divine Healthcare  
**Owner:** Information Security Office  
**Author:** Mitchell Swapnil Chatterjee  
**Version:** 1.0  
**Last updated:** 2026-09-02

## Purpose

This register records which security controls exist at Divine Healthcare, the confidence
held in each, and the basis for that assessment. Residual risk scores in DH-RSK-001 may
only credit controls recorded here as Evidenced, or partially credit controls recorded as
Assumed where the assumption is documented.

A control assessment is only useful if it distinguishes controls that demonstrably operate
from controls that are merely believed to exist. That distinction is the whole point of this
document.

## Status definitions

| Status | Meaning | Effect on residual risk |
|---|---|---|
| Evidenced | Control exists and evidence of operation is held | Credit in residual score |
| Assumed | Reasonable basis to believe it exists; not verified | Partial credit; assumption recorded |
| Defined, not enforced | Documented but not technically or operationally enforced | No credit |
| Unknown | No evidence and no reasonable basis to assume | No credit; raise as a finding |
| Absent | Confirmed not in place | No credit; residual equals inherent |

## Posture summary

| Status | Count |
|---|---|
| Evidenced | 0 |
| Assumed | 9 |
| Defined, not enforced | 3 |
| Unknown | 29 |
| Absent | 15 |
| **Total** | **56** |

0 of 56 controls can currently be credited in a residual risk score.
47 cannot, because they are absent,
unverified, or defined on paper only.

## Register

### Governance & program

| ID | Control | Status | Basis or evidence | Confidence | Source |
|---|---|---|---|---|---|
| GOV-01 | Information security policy approved and published | Unknown | — | Low | — |
| GOV-02 | Data classification model | Defined, not enforced | Four-level model approved by Governance Committee. No technical enforcement in place. | High | Mission 2 |
| GOV-03 | Information handling standard (DH-STD-001) | Defined, not enforced | Handling logic designed; standard not yet published or communicated. | High | Mission 5 |
| GOV-04 | Information governance program | Defined, not enforced | Program blueprint designed; operating model not yet stood up. | High | Mission 6 |
| GOV-05 | Data owners assigned to all systems | Absent | CISO states IT does not know who owns several systems. | High | Mission 6 |
| GOV-06 | Documented enterprise risk analysis | Absent | AUD-2026-019. HIPAA 164.308(a)(1)(ii)(A) is a Required implementation specification. | High | AUD-2026-019 |
| GOV-07 | Defined risk acceptance authority | Absent | AUD-2026-019 — no acceptance authority or escalation thresholds defined. | High | AUD-2026-019 |
| GOV-08 | Periodic board-level security review | Absent | AUD-2026-019 — no evidence of board review. | High | AUD-2026-019 |
| GOV-09 | Security awareness training program | Unknown | — | Low | — |
| GOV-10 | Single enterprise records retention schedule | Absent | CISO states Radiology and Legal maintain conflicting schedules. | High | Mission 6 |
| GOV-11 | Exception and deviation process | Absent | CISO states Security does not know who approves exceptions. | High | Mission 6 |

### Identity & access

| ID | Control | Status | Basis or evidence | Confidence | Source |
|---|---|---|---|---|---|
| IAM-01 | Multi-factor authentication on privileged accounts | Assumed | No contrary evidence. Typical for a provider of this size. Not verified. | Low | — |
| IAM-02 | Multi-factor authentication on all user accounts | Unknown | — | Low | — |
| IAM-03 | Role-based access control | Assumed | EHR and directory almost certainly role-driven. Scope and accuracy unverified. | Low | — |
| IAM-04 | Joiner-mover-leaver process | Unknown | — | Low | — |
| IAM-05 | Periodic user access review | Absent | No access review output exists in any program artifact. | Medium | — |
| IAM-06 | Least privilege enforced on the EHR | Absent | Excess privilege is the premise of an identified risk scenario. | Medium | Mission 8 |
| IAM-07 | Privileged access management | Unknown | — | Low | — |
| IAM-08 | Service and shared account governance | Unknown | — | Low | — |

### Data protection

| ID | Control | Status | Basis or evidence | Confidence | Source |
|---|---|---|---|---|---|
| DP-01 | Encryption of externally addressed email | Absent | AUD-2026-011 — nursing emails patient reports without encryption. | High | AUD-2026-011 |
| DP-02 | Removable media restriction | Absent | AUD-2026-011 — IT copies audit logs to USB drives. | High | AUD-2026-011 |
| DP-03 | Sanctioned cloud storage enforcement | Absent | AUD-2026-011 — research stores patient datasets in personal OneDrive. | High | AUD-2026-011 |
| DP-04 | Print and output controls | Absent | AUD-2026-011 — finance prints salary spreadsheets without restriction. | High | AUD-2026-011 |
| DP-05 | Enforced central storage of clinical images | Absent | AUD-2026-011 — radiology stores MRI images on local desktops. | High | AUD-2026-011 |
| DP-06 | Sensitivity labelling applied to information | Absent | Classification model exists on paper only. No labelling deployed. | High | Mission 2 |
| DP-07 | Encryption of data at rest in core systems | Assumed | Standard for EHR platforms. Scope and key management unverified. | Low | — |
| DP-08 | Secure disposal and destruction | Unknown | — | Low | — |
| DP-09 | Data loss prevention monitoring | Unknown | — | Low | — |

### Endpoint

| ID | Control | Status | Basis or evidence | Confidence | Source |
|---|---|---|---|---|---|
| EP-01 | Full disk encryption on laptops | Unknown | — | Low | — |
| EP-02 | Antivirus or endpoint detection and response | Assumed | Baseline expectation for the sector. Coverage unverified. | Low | — |
| EP-03 | Patch management for workstations and servers | Unknown | — | Low | — |
| EP-04 | Automatic workstation lock | Unknown | — | Low | — |

### Network

| ID | Control | Status | Basis or evidence | Confidence | Source |
|---|---|---|---|---|---|
| NW-01 | Perimeter firewall | Assumed | Baseline expectation. Ruleset and review cadence unverified. | Low | — |
| NW-02 | Network segmentation between clinical, corporate and device networks | Unknown | — | Low | — |
| NW-03 | Patching of internet-facing remote access infrastructure | Unknown | — | Low | — |
| NW-04 | Redundant internet connectivity | Unknown | — | Low | — |

### Physical & environmental

| ID | Control | Status | Basis or evidence | Confidence | Source |
|---|---|---|---|---|---|
| PH-01 | Badge access control to clinical and restricted areas | Assumed | Standard for hospitals. Coverage and enforcement unverified. | Low | — |
| PH-02 | Anti-tailgating measures | Absent | Tailgating is the premise of an identified risk scenario. | Medium | Mission 8 |
| PH-03 | Data centre environmental protection and monitoring | Unknown | — | Low | — |
| PH-04 | Visitor management | Unknown | — | Low | — |

### Resilience & backup

| ID | Control | Status | Basis or evidence | Confidence | Source |
|---|---|---|---|---|---|
| RES-01 | Backups performed on defined schedule | Assumed | Baseline expectation. Scope, frequency and coverage unverified. | Low | — |
| RES-02 | Backup restoration tested | Unknown | — | Low | — |
| RES-03 | Offline or immutable backup copy | Unknown | — | Low | — |
| RES-04 | Disaster recovery plan | Unknown | — | Low | — |
| RES-05 | Clinical downtime and paper procedures | Unknown | — | Low | — |
| RES-06 | Backup generator with fuel contract | Assumed | Required for licensure. Fuel duration and refuelling arrangement unverified. | Low | — |

### Third party

| ID | Control | Status | Basis or evidence | Confidence | Source |
|---|---|---|---|---|---|
| TP-01 | Business associate agreements executed before data sharing | Unknown | — | Low | — |
| TP-02 | Vendor security assessment before onboarding | Unknown | — | Low | — |
| TP-03 | Maintained inventory of third parties handling ePHI | Unknown | — | Low | — |

### Medical devices & clinical technology

| ID | Control | Status | Basis or evidence | Confidence | Source |
|---|---|---|---|---|---|
| MD-01 | Inventory of networked medical devices | Unknown | — | Low | — |
| MD-02 | Medical device network isolation | Unknown | — | Low | — |
| MD-03 | Default credentials changed on clinical devices | Unknown | — | Low | — |
| MD-04 | Management of legacy or unsupported device operating systems | Unknown | — | Low | — |

### Monitoring & logging

| ID | Control | Status | Basis or evidence | Confidence | Source |
|---|---|---|---|---|---|
| LOG-01 | Audit logs generated and retained | Assumed | Audit logs demonstrably exist — AUD-2026-011 notes IT copying them. Retention and integrity unverified. | Medium | AUD-2026-011 |
| LOG-02 | Logs centrally aggregated and reviewed | Unknown | — | Low | — |
| LOG-03 | EHR access auditing and break-glass review | Unknown | — | Low | — |

## Assumptions and limitations

- **A-01 (IAM-01)** Multi-factor authentication on privileged accounts is assumed to be in place. No contrary evidence. Typical for a provider of this size. Not verified. Verification required.
- **A-02 (IAM-03)** Role-based access control is assumed to be in place. EHR and directory almost certainly role-driven. Scope and accuracy unverified. Verification required.
- **A-03 (DP-07)** Encryption of data at rest in core systems is assumed to be in place. Standard for EHR platforms. Scope and key management unverified. Verification required.
- **A-04 (EP-02)** Antivirus or endpoint detection and response is assumed to be in place. Baseline expectation for the sector. Coverage unverified. Verification required.
- **A-05 (NW-01)** Perimeter firewall is assumed to be in place. Baseline expectation. Ruleset and review cadence unverified. Verification required.
- **A-06 (PH-01)** Badge access control to clinical and restricted areas is assumed to be in place. Standard for hospitals. Coverage and enforcement unverified. Verification required.
- **A-07 (RES-01)** Backups performed on defined schedule is assumed to be in place. Baseline expectation. Scope, frequency and coverage unverified. Verification required.
- **A-08 (RES-06)** Backup generator with fuel contract is assumed to be in place. Required for licensure. Fuel duration and refuelling arrangement unverified. Verification required.
- **A-09 (LOG-01)** Audit logs generated and retained is assumed to be in place. Audit logs demonstrably exist — AUD-2026-011 notes IT copying them. Retention and integrity unverified. Verification required.

## Controls requiring verification

Each of the following is recorded as Unknown. None may be credited in a residual risk
score, and each is a candidate recommendation in its own right.

- GOV-01 — Information security policy approved and published
- GOV-09 — Security awareness training program
- IAM-02 — Multi-factor authentication on all user accounts
- IAM-04 — Joiner-mover-leaver process
- IAM-07 — Privileged access management
- IAM-08 — Service and shared account governance
- DP-08 — Secure disposal and destruction
- DP-09 — Data loss prevention monitoring
- EP-01 — Full disk encryption on laptops
- EP-03 — Patch management for workstations and servers
- EP-04 — Automatic workstation lock
- NW-02 — Network segmentation between clinical, corporate and device networks
- NW-03 — Patching of internet-facing remote access infrastructure
- NW-04 — Redundant internet connectivity
- PH-03 — Data centre environmental protection and monitoring
- PH-04 — Visitor management
- RES-02 — Backup restoration tested
- RES-03 — Offline or immutable backup copy
- RES-04 — Disaster recovery plan
- RES-05 — Clinical downtime and paper procedures
- TP-01 — Business associate agreements executed before data sharing
- TP-02 — Vendor security assessment before onboarding
- TP-03 — Maintained inventory of third parties handling ePHI
- MD-01 — Inventory of networked medical devices
- MD-02 — Medical device network isolation
- MD-03 — Default credentials changed on clinical devices
- MD-04 — Management of legacy or unsupported device operating systems
- LOG-02 — Logs centrally aggregated and reviewed
- LOG-03 — EHR access auditing and break-glass review
