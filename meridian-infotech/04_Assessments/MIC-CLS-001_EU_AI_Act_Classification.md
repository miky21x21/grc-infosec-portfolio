# MIC-CLS-001 — EU AI Act classification of Sextant's v1 AI systems

| Field | Value |
|---|---|
| ID | MIC-CLS-001 |
| Version | 1.0 |
| Date | 3 November 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Owner | Governance and Risk Office Lead |
| Approver | Sextant AI Risk Committee |
| Covers | SXT-AI-01 Compliance intelligence; SXT-AI-02 Operations agents (MIC-INV-001) |
| Related | MIC-SCP-001 (section 7, previously "classification memo pending"), MIC-RSK-001, MIC-POL-001 |

## Conclusion

Neither v1 system is a prohibited practice or a high-risk AI system under the EU AI Act. Both are AI systems that interact with people, so **the Article 50 transparency duty applies**, and **Article 4 (AI literacy) applies** to Sextant as an organisation using AI. Sextant voluntarily applies the human-oversight and logging principles of Articles 12 and 14 because its clients' regulators expect them under DORA.

This is a working classification for the management system, not a legal opinion. It is reviewed before any change in Section 5 happens.

## 1. Why the Act applies at all

Sextant is outside the EU but provides AI-drafted output to two EU financial entities, Rheinmark Bank AG (Germany) and Veluwe Payments B.V. (Netherlands). The Act applies to providers placing AI systems on the EU market or putting them into service there, and to providers outside the EU whose systems' output is used in the EU (Article 2(1)(a) and (c)).

## 2. Sextant's role

| System | Role | Reason |
|---|---|---|
| SXT-AI-01, SXT-AI-02 | **Provider** of the AI system | Sextant develops both systems and makes them available to clients under its own name |
| Same systems | Also **deployer** | Sextant's analysts and engineers use them under Sextant's authority |
| Underlying foundation models | **Not** the general-purpose AI model provider | The model obligations of Chapter V sit with the model's provider. Sextant's duty is due diligence on the model's terms and documentation (MIC-RSK-001, R-006) |

## 3. Test against each category

| Test | SXT-AI-01 Compliance intelligence | SXT-AI-02 Operations agents |
|---|---|---|
| **Prohibited practices** (Article 5) | No. No manipulation, social scoring, biometric categorisation or emotion recognition | No |
| **High-risk through product safety law** (Article 6(1), Annex I) | No. Not a safety component of a regulated product | No |
| **High-risk use cases** (Article 6(2), Annex III) | No. Answering compliance and audit questions is not a listed use. It does not assess creditworthiness (point 5(b)), price life or health insurance (5(c)), or make employment decisions (point 4) | No, on balance. Annex III point 2 covers safety components of **critical digital infrastructure**, the category defined by EU critical-entities law (internet exchanges, DNS, cloud and data-centre providers and similar). Bank application systems are regulated under DORA, not as critical digital infrastructure, and the agents are advisory and read-only |
| **Transparency** (Article 50(1)) | **Applies.** Client staff and auditors ask questions and read AI-drafted answers | **Applies.** Client engineers read AI-drafted triage |
| **AI literacy** (Article 4) | **Applies** to Sextant's staff who build and use the systems | Same |

## 4. What Sextant does as a result

- **Transparency (Article 50):** every answer and triage is labelled as AI-drafted and human-approved, naming the approver (MIC-RSK-001, R-011). Client contracts describe the AI's role.
- **AI literacy (Article 4):** training on joining and yearly, with acknowledgement (MIC-POL-001, section 7). The Digital Omnibus of 2026 softened Article 4's wording to supporting AI literacy; Sextant keeps the training record regardless, because clients' questionnaires ask for it.
- **Voluntary high-risk practices:** logging of what each reviewer saw and decided (Article 12 principle), and measured, effective human oversight with seeded test cases (Article 14 principle), as treatment for R-002 and R-003.
- **Model due diligence:** model terms (training on inputs, retention, processing region) checked before approval and each quarter.

## 5. What would change this classification

Re-classify before any of these happens:

- **An agent gains write access** to client systems (the v2 earned-autonomy roadmap). An agent acting on infrastructure moves closer to Annex III point 2 and needs fresh analysis.
- **A client asks Sextant to support credit, insurance-pricing or employment decisions**, which are Annex III uses.
- **A new client is a critical-digital-infrastructure provider** (for example a cloud or data-centre operator) and the operations agents run on its systems.
- **The Act or its guidance changes**, including the Commission's guidelines on high-risk classification and any further Digital Omnibus amendments. High-risk obligations for Annex III systems apply from 2 December 2027 under the Omnibus timetable.

## 6. Outside the EU

- **India:** no AI-specific statute. Anvaya Bank's RBI obligations, including the FREE-AI framework's expectations, flow down through its contract (MIC-DEC-004).
- **United States:** no federal AI statute applies to these services. US banking clients' third-party risk guidance flows down through contracts.

---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer.
