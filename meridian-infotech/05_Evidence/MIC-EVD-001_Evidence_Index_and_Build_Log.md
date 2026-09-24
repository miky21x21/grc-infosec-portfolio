# MIC-EVD-001 — Evidence Index and Build Log

| Field | Value |
|---|---|
| ID | MIC-EVD-001 |
| Status | Living document |
| First entry | 21 September 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Scope | The Meridian Sextant AWS lab account (single account, see MIC-DEC-007) and the build workstation |

## How evidence is handled

- Evidence is recorded only for what has actually been done and observed. Planned work appears under **Open actions**, never as evidence.
- The AWS account ID is redacted as `<ACCOUNT_ID>` in text and blurred in screenshots.
- Screenshots are stored in `05_Evidence/lab/` as `EV-NNN_short-description.png`. Text evidence (command output) is reproduced in this file, redacted.
- Control references use ISO/IEC 27001:2022 Annex A numbering.

## Evidence register

| ID | Date | What it shows | ISO 27001:2022 | Form | Status |
|---|---|---|---|---|---|
| EV-001 | 22 Sep 2026 | Root user protected by a passkey MFA device, with an authenticator app added as backup; no root access keys, CloudFront key pairs or X.509 signing certificates | 8.2, 8.5 | Screenshot `EV-001` | Recorded |
| EV-002 | 22 Sep 2026 | Legacy generic IAM user `UserA` deleted | 5.16, 5.18 | Log entry below | Recorded |
| EV-003 | 22 Sep 2026 | Named admin `mitchell-admin` created with console access; permissions granted only through the `Administrators` group; MFA assigned | 5.16, 5.18, 8.2, 8.5 | Screenshots `EV-003a` (group and MFA), `EV-003b` (MFA prompt at sign-in) | Recorded |
| EV-004 | 22 Sep 2026 | IAM access to billing information activated by root, so that daily cost work never requires root | 8.2 | Screenshot `EV-004` | Recorded |
| EV-005 | 22 Sep 2026 | Budget `sextant-monthly-gross-spend`: USD 5 monthly, unblended cost, **credits excluded**, alerts at 80% actual and 100% forecast; the actual-cost alert fired immediately | 8.16 (supporting) | Screenshot `EV-005` | Recorded |
| EV-006 | 22 Sep 2026 | Mumbai clean-up: internet-facing launch-wizard security group `blog01` and the tutorial key pair deleted; no EC2 instances remain; no `rds!` secrets in Secrets Manager | 8.9, 8.20 | Screenshots `EV-006a` (EC2), `EV-006b` (Secrets Manager) | Recorded |
| EV-007 | 22 Sep 2026 | Workstation toolchain installed with winget from publishers' own download sources, each installer hash verified | 8.19 | Text below | Recorded |
| EV-008 | 22 Sep 2026 | Keyless CLI access: `aws login` session for `mitchell-admin`; `~/.aws/config` holds a login session and no access keys; no `credentials` file exists | 5.17, 8.5 | Text below | Recorded |
| EV-009 | 22 Sep 2026 | Access review closed: only `mitchell-admin` remains as an IAM user, and only `Administrators` as a group (`UserA` and the unused `DemoS3Access` group deleted) | 5.16, 5.18 | Screenshot `EV-009` | Recorded |
| EV-010 | 23 Sep 2026 | Amazon Bedrock model availability in Mumbai, observed in the console; every invocation blocked at account level | 5.23 | Text below | Recorded |
| EV-011 | 24 Sep 2026 | Terraform lab 01: an S3 bucket built from code with public access blocked, encryption, versioning and tags; an anonymous listing was refused while the owner's was allowed; destroyed in the same session | 5.15, 8.3, 8.9 | Text below; code in `07_Infrastructure/labs/tf-01-s3-public-block` | Recorded |
| EV-012 | 24 Sep 2026 | CloudTrail reconciliation of root and admin activity, 18–24 September, against the root-activity record (F-08) | 8.2, 8.15, 8.16 | Text below | Recorded |

### EV-007 — Toolchain versions (Git Bash, 22 Sep 2026)

```text
git version 2.55.0.windows.3
code 1.138.0 (x64)
Python 3.14.7
aws-cli/2.36.50 Python/3.14.6 Windows/11 exe/AMD64
Terraform v1.16.2 on windows_amd64
```

Each package was installed with `winget install`, which reported "Successfully verified installer hash" for VS Code, Python, the AWS CLI and Terraform. Downloads came from `vscode.download.prss.microsoft.com`, `python.org`, `awscli.amazonaws.com` and `releases.hashicorp.com`. Terraform 1.16.3 was available upstream but not yet in the winget catalogue; the version will be pinned in code.

### EV-010 — Bedrock inference options in Mumbai (console, 23 Sep 2026)

| Model | Inference options offered in Mumbai | Invocation result |
|---|---|---|
| Amazon Nova 2 Lite | Global only | ValidationException: Operation not allowed |
| GPT-6 Astra | Global only | Not tested (out of jurisdiction) |
| GPT-5.6 Terra | Global, or India ("IN") | Blocked (see F-06) |
| gpt-oss-120b | On demand, within the region | Blocked (see F-06) |

The same error appeared for gpt-oss-120b and GPT-5.6 Terra when tested in US East (N. Virginia), including on-demand in-region invocation, so the block is account-wide rather than tied to cross-Region routing. The options shown still confirm the design in MIC-DEC-010: an in-region model and an India-only route both exist in Mumbai.

### EV-011 — Terraform lab 01: the flaws.cloud flaw, prevented and tested (Git Bash, 24 Sep 2026)

```text
$ terraform apply
Apply complete! Resources: 5 added, 0 changed, 0 destroyed.
bucket_name = "sextant-tf01-28c07c"

$ aws s3 ls s3://sextant-tf01-28c07c --no-sign-request --region ap-south-1
An error occurred (AccessDenied) when calling the ListObjectsV2 operation: Access Denied

$ aws s3 ls s3://sextant-tf01-28c07c --region ap-south-1
(no output: allowed, bucket empty)

$ terraform destroy
Destroy complete! Resources: 5 destroyed.

$ aws s3 ls | grep sextant-tf01
(no output: nothing left)
```

The same anonymous command that listed the flaws.cloud bucket on 23 September was refused here. Terraform ran as `mitchell-admin` through the `aws login` session, with no access keys; CloudTrail confirms the identity (EV-012).

### EV-012 — CloudTrail reconciliation (CLI, 24 Sep 2026)

Queries: `aws cloudtrail lookup-events`, filtered by user name `root` and by event name, in US East (N. Virginia), where identity and sign-in activity is recorded, and in Asia Pacific (Mumbai). Read-only events (Get, List, Describe) were filtered out to focus on changes.

| Time (IST) | Identity | Events | Activity |
|---|---|---|---|
| 18 Sep 12:09 | root | DeleteSecurityGroup (Mumbai) | Tutorial clean-up, before a named administrator existed |
| 22 Sep 12:06 | root | ConsoleLogin; payment profile and balance reads | Credits and plan check |
| 22 Sep 12:44 | root | DeleteLoginProfile, DeleteUser | `UserA` removed |
| 22 Sep 12:55–13:27 | root | EnableMFADevice ×3, CreateVirtualMFADevice ×3, DeleteVirtualMFADevice, ConsoleLogin | Root passkey and backup authenticator, including attempts refused until an MFA-authenticated sign-in |
| 22 Sep 13:30–13:34 | root | CreateGroup, AttachGroupPolicy, CreateUser, AddUserToGroup, CreateLoginProfile | `Administrators` group and `mitchell-admin` |
| 22 Sep 13:55 | root | DetachGroupPolicy, DeleteGroup | `DemoS3Access` removed |
| 22 Sep 17:03 | root | SetIAMAccessPreference | IAM billing access activated |
| 22 Sep 17:44–17:45 | mitchell-admin | DeleteKeyPair, DeleteSecurityGroup (Mumbai) | Tutorial key pair and `blog01` removed |
| 23 Sep 12:20–13:43 | root | ConsoleLogin; read-only console activity; ConverseStream ×4 (Mumbai) | EV-001 screenshot, then the Bedrock test by mistake |
| 24 Sep 14:39 | mitchell-admin | CreateBucket (Mumbai) | Terraform lab 01 |

Root's 22 September console sessions in Mumbai also show `Search` events, consistent with using the console search bar; none changed anything.

### EV-008 — Keyless command-line identity (Git Bash, 22 Sep 2026)

```text
$ aws sts get-caller-identity
{
    "UserId": "<REDACTED>",
    "Account": "<ACCOUNT_ID>",
    "Arn": "arn:aws:iam::<ACCOUNT_ID>:user/mitchell-admin"
}

$ cat ~/.aws/config
[default]
login_session = arn:aws:iam::<ACCOUNT_ID>:user/mitchell-admin

$ ls -la ~/.aws
cli/  config  login/          (no credentials file)
```

The sign-in used an OAuth 2.0 authorization-code flow with PKCE (`code_challenge_method=SHA-256`) and a local callback on `127.0.0.1`.

## Findings raised during the build

| ID | Finding | Resolution |
|---|---|---|
| F-01 | With credits included, the budget view reported USD 0.00 for the previous month; with credits excluded it reported USD 12.20. **Credits were hiding real usage.** | Budget configured to exclude credits (EV-005) |
| F-02 | A tutorial security group with three inbound rules remained in Mumbai after its instance was gone | Deleted (EV-006) |
| F-03 | A generic IAM user from earlier tutorials still existed | Deleted (EV-002) |
| F-04 | A tutorial EC2 key pair still existed in Mumbai | Closed: key pair deleted in AWS by `mitchell-admin` (EV-006, EV-012); local `.pem` file deleted on 24 Sep |
| F-05 | The opt-in region Asia Pacific (Hyderabad) is enabled on the account | Kept as a future in-country failover region (MIC-DEC-010) |
| F-06 | Every Amazon Bedrock model invocation fails with "ValidationException: Operation not allowed", in Mumbai and N. Virginia, despite full administrator permissions. Community reports attribute this to an account-level eligibility restriction on new accounts without billing history. **A dependency on a supplier's eligibility decision.** | Open: AWS support route identified; re-test after the first bill closes on 1 October; decision on a fallback by 15 October |
| F-07 | The console was briefly used as root during the Bedrock test, a task that does not require root | Switched to `mitchell-admin`. CloudTrail confirms four model calls made as root (EV-012) |
| F-08 | **The root-activity record, written from memory, was incomplete.** Reconciliation against CloudTrail found three root uses it omitted or understated: the 22 September billing check, the deletion of `DemoS3Access`, and the 23 September session, which began with a legitimate root-only screenshot. All root changes on 22 September matched intended actions; no unexplained activity was found. The log also shows the control changing behaviour: routine work was done as root on 18 September, and as `mitchell-admin` from 22 September. | Record corrected below. Practice: reconcile the record against CloudTrail after every root session |

## Root user activity record

| Date | Purpose | Why root was required |
|---|---|---|
| 18 Sep 2026 | Tutorial clean-up in Mumbai (a security group deleted) | Root was the only identity; this predates the controls |
| 22 Sep 2026 | Check credits and plan status | IAM users could not yet see billing (activated at 17:03). Added after reconciliation (F-08) |
| 22 Sep 2026 | Delete `UserA` | No other administrator existed yet |
| 22 Sep 2026 | Assign root MFA: passkey, then a backup authenticator | Only root can manage root's own MFA |
| 22 Sep 2026 | Create the `Administrators` group and `mitchell-admin` | No other administrator existed yet |
| 22 Sep 2026 | Delete the unused `DemoS3Access` group | Not strictly required; done in the same root session. Added after reconciliation (F-08) |
| 22 Sep 2026 | Activate IAM access to billing information | This setting can only be changed by root |
| 23 Sep 2026 | Screenshot of root's security credentials (EV-001) | Only visible to root |
| 23 Sep 2026 | Bedrock playground test: four model calls | Not required: a mistake, noticed and corrected (F-07) |

Verified against CloudTrail on 24 September 2026 (EV-012).

## Build log

**21 September 2026 — Design: the company blueprint and the pivot to Sextant**

No changes to AWS; design and research only.

- Defined the company in depth, one topic at a time, grounding each claim in published sources and practitioners' own accounts.
- Blueprinted the original scope, the Pune BFS delivery unit: the client lifecycle (win, transition, run, assure, exit); a contractor-ODC delivery model (working assumption); the split between Meridian-owned, shared and client-owned controls; secure client bays; and the ISO 27005 primary assets. One finding: Meridian's DPDP role flips, as processor for its clients' customers but fiduciary for its own staff.
- Gap found: DORA was missing from the framework stack. Recorded as MIC-DEC-001.
- Owner's review: the blueprint described a traditional offshore delivery centre, not the cloud- and AI-centred company intended. Researched current real-world technology and its constraints (Bedrock AgentCore Policy, managed GraphRAG region availability, Neptune Analytics pricing, confidential GPU computing). The scope moved to a new AI-native platform unit, named Meridian Sextant. Recorded as MIC-DEC-002.
- World models kept out of scope: their commercial home is physical AI, so they sit in a separate Physical AI lab on the technology radar (working assumption).
- Two externally generated analyses, one on viability and one listing risks, were checked claim by claim against primary sources.
  - Confirmed: Bedrock agent guardrails do not screen tool calls; the Indian IT sector's AI revenue is growing on a weakening base (Jefferies downgrade, February 2026).
  - Corrected: that Indian ICT providers are automatically DORA critical providers (designation is an assessment; the first list, November 2025, named 19 providers); the MIT "95% of pilots fail" figure (it measures a lack of measurable profit-and-loss impact, and its method is contested); GraphRAG's USD 33,000 indexing cost (outdated).
  - Unsupported: a 40–60% cost premium for confidential computing.
  - Result: MIC-DEC-003, proposed.
- Roadmap additions from verified precedents: an agent registry, which Microsoft's 2026 Cyber Pulse report recommends as the first step; and "earned autonomy", modelled on Morgan Stanley's FIXR reconciliation agents, which clear familiar cases automatically and escalate the rest.
- Compiled a private owner's briefing book (v0.1) holding the whole picture, with every statement tagged as decided, working assumption, proposed or open. It is a reading copy and is not committed.

**22 September 2026 — Week 1: account security and tooling**

- Design, before the hands-on work: Sextant gained a fifth client regulated in India (MIC-DEC-004), and the group's other industries were stated (Sextant itself is financial-services only). The briefing book moved to v0.2.

- Checked credits and plan status. The console shows the free plan ends **28 February 2027**, which is the teardown deadline. After the AWS Budgets activity, credits remaining read USD 145.75.
- Locked root with a passkey. An attempt to add a second MFA device failed because the session pre-dated the first device: AWS requires an MFA-authenticated session to change MFA settings.
- Deleted the legacy user, created `mitchell-admin` with MFA through a group, and activated IAM billing access.
- Created the credit-excluding budget; its first alert fired immediately.
- Cleaned up tutorial leftovers in Mumbai.
- Installed the toolchain. `code`, `aws` and `terraform` were not found until a full restart refreshed the Windows PATH, and the Microsoft Store "python" alias had to be disabled.
- Signed the CLI in with `aws login`, with no keys stored anywhere.
- Decisions made during the build: MIC-DEC-007 (single-account lab) and MIC-DEC-008 (lab identity). All eight decision records and this index were committed and pushed the same day.

**23 September 2026 — Scope, residency and the first model test**

- Rewrote the scope as MIC-SCP-001 version 2.0, moved it out of the README into `00_Scope`, and replaced the README with a short front page.
- Accepted MIC-DEC-003. Recorded MIC-DEC-009 (US clients' data in a US region, as a contract choice) and MIC-DEC-010 (residency by jurisdiction, including the Pune access exception and the CERT-In log split).
- Captured and redacted the evidence screenshots, using solid boxes rather than blur.
- Tested Bedrock in Mumbai: the inference options confirmed the jurisdiction design, but every invocation was blocked at account level (EV-010, F-06). The console region reset to N. Virginia twice during testing; the default region is to be pinned.
- Practice: completed flaws.cloud Level 1 (an S3 bucket listable by anyone), which shaped the account-wide public-access block planned for the Terraform build.

**24 September 2026 — First Terraform build and a CloudTrail audit**

- Built, attacked and destroyed an S3 bucket from code (EV-011): the flaws.cloud flaw from 23 September, prevented and proven. The AWS provider (v6.66.0) read the `aws login` session directly, with no access keys.
- Lesson learned: exported short-lived credentials take priority over the login session and fail once they expire. Removed them with `unset` and signed in again. Credentials are not exported into the terminal any more.
- Reconciled the root-activity record against CloudTrail (EV-012) and corrected it (F-08).
- Decision recorded: infrastructure code lives in `07_Infrastructure`, and state files are never committed (MIC-DEC-011).
- Working method written down as MIC-MTH-002.

## Open actions

- [x] Add a backup authenticator-app MFA device to root (22 Sep)
- [x] Delete the unused `DemoS3Access` group (22 Sep)
- [x] Delete the tutorial key pair in Mumbai (22 Sep)
- [x] Confirm the tutorial key pair's local `.pem` file is deleted (24 Sep)
- [ ] Set an account alias
- [ ] Confirm `Owner` and `Project` tags on `mitchell-admin` and on the budget
- [ ] Set the CLI default region permanently: `aws configure set region ap-south-1`
- [x] Capture and add the screenshots for EV-001, EV-003, EV-004, EV-005, EV-006 and EV-009 (23 Sep)
- [x] Pin the console's default region to Mumbai (24 Sep)
- [ ] Bedrock access (F-06): re-test after 1 October; decide on a fallback by 15 October
- [ ] Strip all rules from the default security groups, via Terraform (planned)
- [ ] Run `aws logout` at the end of each working day
- [ ] After every root session, reconcile the root-activity record against CloudTrail
---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
