# MIC-DEC-010 — Residency is enforced by jurisdiction, not by single region

| Field | Value |
|---|---|
| ID | MIC-DEC-010 |
| Status | Accepted |
| Decided | 23 September 2026 |
| Recorded | 23 September 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Refines | MIC-DEC-005 (regions) and MIC-DEC-006 (residency over failover) |
| Related | MIC-DEC-004, MIC-DEC-009, MIC-SCP-001 section 6 |

## Context

The earlier rules promised that EU clients' content would be answered only in Frankfurt, and Indian clients' content only in Mumbai. Two findings made those single-region promises unworkable.

**Models do not run where the rule assumed.** On 23 September 2026 the Bedrock console in Mumbai showed Amazon Nova 2 Lite available through Global routing only; GPT-5.6 Terra through Global or India ("IN") routing; and gpt-oss on demand within the region (evidence EV-010). AWS documentation shows Nova 2 Lite reaching Frankfurt through EU geographic routing rather than in-region. A request may therefore be processed in another data centre inside the same geography.

**The laws care about jurisdiction, not location.** GDPR restricts personal data leaving the EU, not moving between EU regions. Indian expectations concern India as a whole.

## Decision

1. **Stored in the home region:** EU clients' material in Frankfurt; Indian clients' material in Mumbai; US clients' material in a US region (MIC-DEC-009).
2. **Processed only within the same jurisdiction** (EU, India or US) and never outside it. Models are chosen per region accordingly; any Global-only model is excluded from client content.
3. **Human access from India is a declared, contracted exception.** Under EU guidance, remote access from a non-EU country is a transfer, and India has no EU adequacy decision. Pune analysts therefore view EU clients' results through sessions that keep no copies in India, covered in each EU client's data processing agreement by the Standard Contractual Clauses (Module 2, controller to processor) and a transfer impact assessment.
4. **Client-specific exceptions**, such as a bank requiring one named data centre, are written into that client's contract and override rule 2 for that client.
5. **Logs are split by content.** CERT-In requires 180-day log retention by Indian entities. Its FAQ permits storage outside India if logs can be produced within a reasonable time, though some practitioners read it as requiring a copy in India. Security and access logs, which contain no client content, keep a 180-day copy in Mumbai; content-bearing logs stay in their client's jurisdiction.

## Alternatives considered

- **Keep single-region rules.** Rejected: the available models would break them immediately, or leave no usable model.
- **Allow processing anywhere, relying on contracts alone.** Rejected: it would remove the architectural control that makes residency provable.

## Consequences

- **Active-active processing within each jurisdiction** comes with the design, because geographic routing spreads requests across regions inside it.
- **Active-active storage** would need a second region per jurisdiction (Mumbai with Hyderabad; Frankfurt with another EU region). It is target design, not built in the lab.
- Residency tests in the control-testing phase test jurisdiction, not region: EU content must never be retrievable or processed outside the EU.
- MIC-DEC-006 still holds, restated: client content never fails over outside its jurisdiction.

## Sources

- Amazon Bedrock console, Mumbai, 23 September 2026 (EV-010); Amazon Bedrock model card for Nova 2 Lite (regional availability).
- AWS Machine Learning Blog, OpenAI models on Amazon Bedrock for in-country inferencing in India, September 2026.
- EDPB Guidelines 05/2021 on the interplay between Article 3 and Chapter V of the GDPR.
- Commission Implementing Decision (EU) 2021/914 (Standard Contractual Clauses).
- CERT-In Directions of 28 April 2022, and CERT-In FAQs (questions 35 and 36).
---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
