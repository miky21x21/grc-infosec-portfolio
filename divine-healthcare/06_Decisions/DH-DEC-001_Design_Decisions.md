# DH-DEC-001 — Design Decision Record

> **Simulated engagement.** Divine Healthcare is a fictional 340-bed US hospital created as a
> self-directed learning exercise. It is not a client or an employer, and no real patient or
> organisational data appears in this document.

**Author:** Mitchell Swapnil Chatterjee
**Version:** 1.0
**Owner:** Information Security Office

---

## Purpose

This register records design decisions taken while building the Divine Healthcare information
security programme, the reasoning behind each, and the alternatives rejected.

It exists because a finished standard shows only its conclusions. When a requirement is
challenged eighteen months later — by an assessor, a new analyst, or a department head who
finds it inconvenient — the question is never *what does it say* but *why was it written that
way*. Undocumented reasoning gets re-litigated, and usually reversed by whoever argues hardest
rather than whoever is right.

Each decision carries a status. **Accepted** means the decision is in force and downstream
artifacts must comply. **Proposed** means it is recommended but not confirmed, and artifacts
should not yet depend on it. **Superseded** means a later decision replaced it; the record is
retained rather than deleted, because the reversal is itself information.

---

## DEC-001 — Classification and handling published as a single standard

**Status:** Accepted

### Context

Earlier drafting referred inconsistently to a combined *Information Classification and
Handling Standard* (DH-STD-001) and to a split pair — DH-STD-001 for classification and
DH-STD-002 for handling. Both appeared in working notes. DH-SCP-001 cross-references these
documents by ID, so the ambiguity had to be resolved before scope was issued.

### Decision

Classification and handling are published as one document, **DH-STD-001 — Information
Classification and Handling Standard**, structured as a body of requirements with four annexes:

| | |
|---|---|
| Annex A | Information Classification Matrix |
| Annex B | Information Handling Matrix |
| Annex C | Technical Enforcement Matrix |
| Annex D | HIPAA and NIST CSF 2.0 mapping |

`DH-STD-002` is left unallocated for the next standard issued, expected to be Access Control.

### Reasoning

Classification without handling is inert. A document defining four sensitivity levels and
stopping there tells the reader what information is worth and nothing about what to do with
it; the handling rules are what give the levels consequence.

The two are also structurally the same artifact. The rows of the handling matrix are the
classification levels. Publishing them separately places the same taxonomy in two documents
that must agree, and version drift between documents that must agree is a recurring audit
finding.

Operationally, a clinician deciding what may be done with an imaging report should consult one
document, not two.

### Alternatives considered

**Split into two standards.** Appropriate where handling grows into per-channel and per-media
annexes running to dozens of pages, or where classification is owned by a data governance
function and handling by security operations. Divine Healthcare has neither condition: a
single information security office owns both, and the combined document is expected to run
well under thirty pages including annexes.

### Consequences

- DH-SCP-001 references DH-STD-001 only. No reference to DH-STD-002 until a standard is issued
  under that number.
- Annexes are separately versioned, so Annex B or C may be reissued without reopening the
  classification model, which is expected to remain stable for years.
- Annex C inherits a dependency on DEC-003 below.

---

## DEC-002 — Requirements are vendor-neutral; technology is confined to Annex C

**Status:** Accepted

### Context

Microsoft Purview is the assumed enforcement platform for information protection within the
Microsoft 365 estate. The question was whether named products may appear inside the
standard's numbered requirements.

### Decision

Requirements in the body of DH-STD-001 state outcomes without naming products. Named
technology appears only in **Annex C — Technical Enforcement Matrix**, which maps each
requirement to the mechanism currently enforcing it.

Correct:

> **5.4** Information classified Restricted shall be encrypted when transmitted outside the
> Divine Healthcare network.

Incorrect:

> **5.4** Information classified Restricted shall be encrypted using Microsoft Purview Message
> Encryption when transmitted outside the Divine Healthcare network.

### Reasoning

A requirement naming a product must be reissued when the product changes, and is
unenforceable in any system the product does not cover. In a hospital this is most systems:
Purview operates within Microsoft 365 and has no visibility into the EHR, PACS, the laboratory
information system, billing, or networked medical devices. A standard whose requirements
assume Purview would therefore be unenforceable across the majority of the estate holding the
organisation's most sensitive information.

This also preserves the documentation hierarchy. A standard defines how consistency is
achieved; the mechanism that achieves it belongs one layer down.

### Consequences

- Annex C maps requirements to enforcement mechanisms across the whole estate, not only
  Microsoft 365. Clinical systems map to their own native access controls.
- Annex C carries a **state** qualifier per row, distinguishing licensed, deployed, configured,
  and operating-with-evidence. Only the last constitutes a control for the purposes of
  DH-BSL-001 and residual risk scoring in DH-RSK-001.
- Annex C must remain consistent with DH-BSL-001. Where the baseline records a control as
  absent or unverified, Annex C describes target state and must say so explicitly.

---

## DEC-003 — Assumed licensing baseline excludes the Microsoft 365 compliance stack

**Status:** Proposed

### Context

Annex C cannot be drafted without a position on what Divine Healthcare is licensed for. The
Microsoft Purview capability set is split across licence tiers, and several controls relevant
to the findings in AUD-2026-011 sit above the base tier.

### Decision (proposed)

Divine Healthcare is assumed to hold Microsoft 365 E3 or Business Premium **without** the E5
Compliance or E5 Security add-ons.

Under that assumption:

| Capability | Availability |
|---|---|
| Manual sensitivity labels with encryption | Available |
| DLP for Exchange, SharePoint, OneDrive | Available |
| Audit log retention (90 days) | Available |
| Automatic and policy-based labelling | Requires E5 or Information Protection and Governance add-on |
| Endpoint DLP (print, clipboard, removable media) | Requires E5 or Purview DLP add-on |
| DLP for Teams chat | Requires E5 |
| DLP simulation mode | Requires E5 Compliance |
| Defender for Cloud Apps | Requires E5 or E5 Security add-on — **not** included in E5 Compliance |

### Consequences for AUD-2026-011

| Finding | Position under this baseline |
|---|---|
| Unencrypted internal patient email | Remediable — Exchange DLP and message encryption available |
| Research data in personal OneDrive | Partial — sanctioned tenant governable; unsanctioned cloud requires Defender for Cloud Apps |
| Unrestricted printing of salary data | Not remediable — requires Endpoint DLP |
| MRI images on local desktops | Not remediable — requires Endpoint DLP |
| Audit logs copied to removable media | Not remediable — requires Endpoint DLP |

Three of five audit findings have no available technical enforcement mechanism at this
licensing position.

### Reasoning

This baseline is chosen deliberately over the alternative, which would assume the compliance
stack is licensed but unconfigured.

Under the alternative, every requirement maps cleanly to an available Microsoft capability and
the remediation gap is configuration and rollout. That produces a tidier annex and a weaker
document. It also invites a specific error: crediting controls that are licensed but not
operating, which is precisely the distinction DH-BSL-001 exists to enforce.

The proposed baseline forces three things a licensed-but-unconfigured assumption does not.
Requirements without technical enforcement must be supported by compensating administrative
controls — procedure, training, and monitoring — with their weakness stated rather than
concealed. The unremediable findings must be assembled into a costed procurement case tied to
named audit findings. And the residual risk position stays consistent with DH-BSL-001, which
currently records zero evidenced controls.

A secondary consideration: E3 DLP has no simulation mode, so any policy deployed goes directly
to enforcement. In a clinical environment, an untested DLP policy blocking legitimate care
communication is an availability risk with patient safety consequences. The standard must
require phased deployment as a compensating measure for the missing capability.

### Open

This decision is **Proposed**, not Accepted. Confirmation is required before Annex C is
drafted. If the licensing position changes, this record is superseded rather than edited, and
Annex C is reissued against the new baseline.

---

## Revision history

| Version | Date | Change |
|---|---|---|
| 1.0 | — | Initial issue. DEC-001 and DEC-002 accepted; DEC-003 proposed. |
