# Divine Healthcare — Information Governance & Risk Programme

> **This is a simulated engagement.** Divine Healthcare is a fictional 340-bed US hospital
> created as a self-directed learning exercise. It is not a client or an employer, and no
> real patient or organisational data appears anywhere in this project. Every artifact here
> was written by me from scratch.

**Author:** Mitchell Swapnil Chatterjee
**Sector:** Healthcare provider (US)
**Primary regulation:** HIPAA Security Rule and Privacy Rule
**Supporting frameworks:** NIST CSF 2.0, ISO/IEC 27001:2022, ISO/IEC 27005:2022, NIST SP 800-30 Rev. 1

---

## What this project is for

[Meridian Infotech](../meridian-infotech/) demonstrates breadth — one control set mapped
simultaneously across ISO 27001, SOC 2, DPDP, CERT-In, GDPR and ISO 42001. This project
does the opposite. It goes deep on a single regulation.

HIPAA is unusual among security regulations because it splits its implementation
specifications into **Required** and **Addressable**, and an addressable specification is
not optional — it must be implemented, or a written justification must exist explaining why
it is not reasonable and appropriate, along with the equivalent alternative measure adopted.
Most organisations get this wrong, and it is one of the most common findings in OCR
enforcement actions.

So the deliverables here are built to answer a specific question: **can this organisation
produce written evidence for every safeguard decision it has made?**

---

## The organisation

| | |
|---|---|
| Size | 340 beds |
| Services | Emergency, clinical treatment, laboratory, radiology, surgery, pharmacy, billing, insurance processing, telehealth |
| Information assets | ePHI, PII, medical imaging, financial records, employee data, audit logs |
| Known audit findings | AUD-2026-011 (no standardised handling requirements), AUD-2026-019 (no documented enterprise risk analysis) |

---

## Artifacts

| ID | Artifact | Location | Status |
|---|---|---|---|
| DH-SCP-001 | Scope and context statement | `00_Scope/` | Planned |
| DH-MTH-001 | Risk assessment methodology | `01_Methodology/` | In progress |
| DH-RSK-001 | Enterprise risk register | `02_Registers/` | In progress |
| DH-BSL-001 | Control baseline register | `02_Registers/` | Published |
| DH-POL-001 | Information governance programme | `03_Policies/` | Planned |
| DH-STD-001 | Information classification and handling standard | `03_Policies/` | Planned |
| DH-DEC-001 | Design decision record | `06_Decisions/` | Published |
| DH-GAP-001 | HIPAA safeguard gap assessment | `04_Assessments/` | Planned |

---

## Three decisions worth explaining

Portfolios usually show the finished document. These are the judgement calls behind them,
which is what I would want to be asked about.

**A handling matrix of allowed / prohibited does not survive contact with a hospital.**
My first version prohibited reading Confidential information, which would have stopped
doctors opening patient records. The restriction in a handling standard is almost never the
activity — it is who performs it, under what condition. That pushed the design toward
conditional rules (internal email permitted, external email requires encryption) rather than
flat permissions.

**Availability failure in a hospital is a patient safety event.**
Loss of patient data is severe and recoverable. Loss of clinical systems means ambulance
diversion and patients travelling further to care, with no clinical error anywhere in the
chain. This is why the impact criteria in DH-MTH-001 score patient safety as its own
dimension rather than folding it into operational impact, and why the methodology carries an
override rule escalating any patient-safety-5 scenario regardless of likelihood.

**A control that exists is not a control that works.**
DH-BSL-001 separates Evidenced, Assumed, Defined-but-not-enforced, Unknown and Absent,
because residual risk may only credit controls that can be evidenced. Of 56 controls in the
current baseline, **zero are evidenced** — which is the honest position for an organisation
that has just started its governance programme. Recording that is more useful than assuming
the environment is better than it is.

---

## Skills demonstrated

- HIPAA Security Rule interpretation, including required vs addressable specifications
- Risk assessment methodology design: impact and likelihood criteria, inherent vs residual
- Control baseline assessment under incomplete information
- Information classification and conditional handling rules
- Data ownership, custodianship and accountability models
- Governance programme design and stakeholder mapping
- Enterprise security documentation hierarchy

---

## Contact

Mitchell Swapnil Chatterjee
[linkedin.com/in/mitchell-chatterjee-7a042b287](https://linkedin.com/in/mitchell-chatterjee-7a042b287)
mitchell.s.chatterjee@gmail.com
