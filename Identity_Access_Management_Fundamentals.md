# Identify & Access Management (IAM) Fundamentals

**Author:** Mitchell Swapnil Chatterjee
**Document Version:** 1.0
**Classification:** Portfolio Deliverable / Technical Reference
**Alignment:** ISO/IES 27001:2022 (A.5.15-A.5.18), SOC 2 Type II (CC6.1, CC6.2, CC6.3), NIST SP 800-63

---

## The IAAA Security Model

Every secure identity system relies on four sequential pillars: **identification, Authentication, Authorization, and Accounting (IAAA)**.

```
      ┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
      │  IDENTIFICATION  │ ───► │  AUTHENTICATION  │ ───► │  AUTHORIZATION   │ ───► │    ACCOUNTING    │
      │  "Who are you?"  │      │ "Prove who you   │      │ "What are you    │      │ "What did you    │
      │                  │      │       are"       │      │  allowed to do?" │      │       do?"       │
      └──────────────────┘      └──────────────────┘      └──────────────────┘      └──────────────────┘
```

### Identification
- **Definition:** The process where an entity claims an identity in a system.
- **Enterprise Execution:** Entering a username (e.g., 'm.chatterjee'), email address, employee ID number, or scanning a smart card badge prior to credential verification.

### Authentication (AuthN)
- **Definition:** The verification step where the system validates that the entity is genuinely who they claim to be.
- **Enterprise Execution:** Verifying proof via passwords, biometric scans (faceID/Fingerprint), hardware security (YubiKey), or time-based one-time passwords(TOTP).

### Authorization (AuthZ)
- **Definition:** The process of enforcing permission and granting access rights to specific resources after successful authentication.
- **Enterprise:** Deciding id a logged-in user can perform actions (Read, Write, Execute, Delete) on a resource. For example, a Finance Associate can view payroll spreadsheets, but is blocked from modifying database schemas.

### Accounting (Auditing & Logging)
- **Definition:** The continuous tracking and logging o user actions and security events to maintain accountability and an audit trail.
- **Enterprise Execution:** Recording timestamped logs of user logins, privilege escalations, file downloads, and system changes into SIEM (e.g., Microsoft Sentinel or Splunk) for forensic investigation and audit evidence.

---

## Core Access Control Principles

### Least privilege
- **Core Concept:** Users and system accounts must be granted only the absolute minimum permission necessary to complete their assigned job duties-nothing more.
- **Business Imapct:** Restricts the "blast radius" if a user is compromised by malware or a phishing attack.
- **Real-World Example:** A marketing coordinator requires write access to the company blog and social accounts, butmust never be gran ted server SSH access or Domain Admin privileges.

### Need-to-Know
- **Core Concept:** Access to specific sensitive information is restricted to personnel who explicitly require it to execute business task, regardless of their seniority or department.
- **Real-World Example:** An HR Manager has permissions inside the HR software, but should not have access to unreleased application source code unless they are actively counducting a technical audit of software engineering teams.

### Role-Based Access Control (RBAC)
- **Core Concept:** Access permissions are assigned to predefined organizational roles (e.g., `Finance_Analyst`, `Helpdesk_Tier1`) rather than granted individually to users.
- **Operational Advantage:** Drastically reduces administrative overhead and access drift. When an employee joins or changes positions, assigning them to the target role automatically provisions the correct permissions.

### Multi-Factor Authentication (MFA)
- **Core Concept:** Requiring two or more distinct authentication factors before granting access.
- **The Three Classic Factors:**
  1. **Something You Know:** Password, PIN, or passphrase.
  2. **Something You Have:** Smartphone with authenticator app, hardware key (YubiKey), or smart card.
  3. **Something You Are:** Fingerprint, facial recognition, or iris scan.
- **Why It Matters:** MFA neutralizes up to 99% of bulk automated credential stuffing and password-spraying attacks.

---

## The Joiner-Mover-Leaver (JML) Lifecycle

The JML process governs how identity accounts are created, modified, and retired across an employee's tenure.

| Phase | Operational Trigger | Security Action Required | Key Risks Mitigated |
| :--- | :--- | :--- | :--- |
| **Joiner** | New hire onboarded by HR | Provision IdP account, assign RBAC role, enforce MFA setup on Day 1. | Unauthorized initial access, unmonitored accounts. |
| **Mover** | Internal transfer or promotion | Audit current access, **revoke previous role permissions**, grant new RBAC profile within 48 hours. | **Privilege Creep** (accumulating unneeded access across positions). |
| **Leaver** | Employee resignation or termination | Terminate active sessions immediately; disable IdP account within 2 hours (voluntary) or immediately (involuntary); collect physical assets. | **Orphaned Accounts**, insider threats, disgruntled ex-employee data theft. |

---

## Access Reviews (Attestation)

- **Definition:** Periodic (quarterly or bi-annual) audits where resource owners and managers review and re-certify who has access to sensitive files, applications, and cloud environments.
- **Audit Requirement:** ISO 27001 (A.5.18) and SOC 2 (CC6.2) require documented evidence that access reviews were conducted and that stale or unneeded permissions were revoked.

---

## Key Takeaways
1. **AuthN vs. AuthZ:** Authentication verifies identity ("Who are you?"); Authorization enforces boundaries ("What can you do?").
2. **Minimize Blast Radius:** Least Privilege and RBAC prevent localized compromised credentials from escalating into company-wide domain takeovers.
3. **Offboarding is Critical:** The Leaver workflow must be rapid and thorough to eliminate orphaned accounts that attackers target for persistent access.	
