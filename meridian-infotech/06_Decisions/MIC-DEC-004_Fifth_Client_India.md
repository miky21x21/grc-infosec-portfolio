# MIC-DEC-004 — A fifth Sextant client, regulated in India

| Field | Value |
|---|---|
| ID | MIC-DEC-004 |
| Status | Accepted (the specific client is a working assumption) |
| Decided | 22 September 2026 |
| Recorded | 22 September 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Related | MIC-DEC-002, MIC-DEC-005, MIC-DEC-006 |

## Context

Sextant's four clients were all in the US and EU. That left two gaps. Indian regulation touched the scope only through the DPDP Act (for Meridian's own staff data) and CERT-In, although the portfolio is meant to represent both Indian and international regulation. And the Mumbai region had no client whose data was required to live there.

## Decision

Sextant takes a **fifth client regulated by the Reserve Bank of India**.

Working assumption for the client: **Anvaya Bank Ltd**, a Mumbai-based private-sector bank (placeholder name). Meridian's legacy delivery unit runs its production support and digital channels, including UPI integration; Sextant provides compliance intelligence that maps RBI requirements to controls and evidence. Working rule R1b: Indian-client content is indexed and answered only in the Mumbai region.

## Alternatives considered

- **No Indian client.** Rejected for the two gaps above.
- **An NBFC instead of a bank.** Open: it would add RBI's digital-lending rules but break the pattern of the client set.

## Consequences

- New regulatory material reaches Sextant through the client's contract:
  - RBI (Outsourcing of Information Technology Services) Directions, 2023, and the RBI Master Direction on IT Governance, Risk, Controls and Assurance Practices, 2023.
  - RBI's FREE-AI framework (13 August 2025): advisory, but regulated entities are expected to hold their technology providers to its principles.
  - RBI's 2026 draft guidance on model risk management: monitored as a consultation draft, not treated as binding. Its status comes from a vendor source and must be confirmed on rbi.org.in before it is relied on.
  - RBI's 2018 requirement to store payment system data in India. Sextant holds no payment data, so this shapes design rather than binding the platform.
- Client concentration improves: each client is now roughly a fifth of Sextant's business rather than a quarter.
- Managed GraphRAG in Bedrock Knowledge Bases is not listed for the Mumbai region, but Amazon Neptune Analytics has been available in Mumbai since 26 September 2025. Anvaya's graph can therefore stay in India as a curated graph the agent queries directly (working assumption, to be confirmed at build time).
---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
