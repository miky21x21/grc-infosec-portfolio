# Information Security Foundations & Governance Guide
**Author:** Mitchell Swapnil Chatterjee  
**Document Version:** 1.0  
**Classification:** Internal / Portfolio Deliverable  

---

## 1. The CIA Triad in Enterprise Operations

### Confidentiality
- **Definition:** Ensuring that sensitive information is accessible only to authorized personnel and protected against unauthorized disclosure.
- **Enterprise Example:** Enforcing Role-Based Access Control (RBAC) and AES-256 encryption on `AST-DAT-001` (Customer PII & Payment Database) so only authorized finance and legal personnel can view raw cardholder data.

### Integrity
- **Definition:** Safeguarding the accuracy, completeness, and authenticity of data and systems, ensuring they are not altered in an unauthorized or undetected manner.
- **Enterprise Example:** Utilizing SHA-256 cryptographic hashing and digital signatures during deployment pipelines to verify that software source code (`AST-SFT-002`) has not been tampered with before pushing to production.

### Availability
- **Definition:** Guaranteeing that systems, networks, and data are timely and reliably accessible to authorized users whenever required for business operations.
- **Enterprise Example:** Maintaining an offsite, immutable backup NAS array (`AST-HW-002`) with automated snapshot synchronization to ensure swift operational recovery in the event of a ransomware attack.

---

## 2. Threat vs. Vulnerability vs. Risk

### Core Formula
$$\text{Risk} = \text{Threat} \times \text{Vulnerability} \times \text{Impact}$$

### Real-World Business Analogy
- **Vulnerability (The Weakness):** An unlocked ground-floor window in a bank building.
- **Threat (The Adversary / Event):** A burglar patrolling the street looking for easy entry points.
- **Impact (The Cost):** Loss of $50,000 cash stored in the vault behind that window.
- **Risk (The Calculation):** The total likelihood and financial loss resulting from the burglar entering through the unlocked window and stealing the cash. In GRC, placing a steel security grate (Technical Control) over the window reduces the risk to an acceptable level without requiring the bank to close down.

---

## 3. Security Controls Classification Matrix

| Control Category | Control Function | Operational Purpose | Enterprise Example |
| :--- | :--- | :--- | :--- |
| **Administrative** | Preventive | Sets governance policy and behavioral expectations | Enterprise Password & Authentication Policy |
| **Technical** | Detective | Identifies unauthorized actions or anomalous behavior | SIEM Log Monitoring & Endpoint Detection (EDR) |
| **Technical** | Preventive | Directly blocks unauthorized access | Multi-Factor Authentication (MFA) & Firewalls |
| **Physical** | Deterrent / Preventive | Blocks physical entry to critical assets | Biometric Data Center Locks & Security Badges |
| **Administrative** | Corrective | Guides recovery after a security incident | Incident Response Playbooks & Disaster Recovery Plans |
