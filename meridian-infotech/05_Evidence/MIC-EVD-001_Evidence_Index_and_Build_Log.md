# MIC-EVD-001 — Evidence Index and Build Log

| Field | Value |
|---|---|
| ID | MIC-EVD-001 |
| Status | Living document |
| First entry | 22 September 2026 |
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
| EV-001 | 22 Sep 2026 | Root user protected by a passkey MFA device; no root access keys, CloudFront key pairs or X.509 signing certificates | 8.2, 8.5 | Screenshot | To add |
| EV-002 | 22 Sep 2026 | Legacy generic IAM user `UserA` deleted | 5.16, 5.18 | Log entry below | Recorded |
| EV-003 | 22 Sep 2026 | Named admin `mitchell-admin` created with console access; permissions granted only through the `Administrators` group; MFA assigned | 5.16, 5.18, 8.2, 8.5 | Screenshot | To add |
| EV-004 | 22 Sep 2026 | IAM access to billing information activated by root, so that daily cost work never requires root | 8.2 | Screenshot | To add |
| EV-005 | 22 Sep 2026 | Budget `sextant-monthly-gross-spend`: USD 5 monthly, unblended cost, **credits excluded**, alerts at 80% actual and 100% forecast; the actual-cost alert fired immediately | 8.16 (supporting) | Screenshot | To add |
| EV-006 | 22 Sep 2026 | Mumbai clean-up: internet-facing launch-wizard security group `blog01` deleted; no EC2 instances remain; no `rds!` secrets in Secrets Manager | 8.9, 8.20 | Screenshot | To add |
| EV-007 | 22 Sep 2026 | Workstation toolchain installed with winget from publishers' own download sources, each installer hash verified | 8.19 | Text below | Recorded |
| EV-008 | 22 Sep 2026 | Keyless CLI access: `aws login` session for `mitchell-admin`; `~/.aws/config` holds a login session and no access keys; no `credentials` file exists | 5.17, 8.5 | Text below | Recorded |

### EV-007 — Toolchain versions (Git Bash, 22 Sep 2026)

```text
git version 2.55.0.windows.3
code 1.138.0 (x64)
Python 3.14.7
aws-cli/2.36.50 Python/3.14.6 Windows/11 exe/AMD64
Terraform v1.16.2 on windows_amd64
```

Each package was installed with `winget install`, which reported "Successfully verified installer hash" for VS Code, Python, the AWS CLI and Terraform. Downloads came from `vscode.download.prss.microsoft.com`, `python.org`, `awscli.amazonaws.com` and `releases.hashicorp.com`. Terraform 1.16.3 was available upstream but not yet in the winget catalogue; the version will be pinned in code.

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
| F-04 | A tutorial EC2 key pair still exists in Mumbai | Open, see below |
| F-05 | The opt-in region Asia Pacific (Hyderabad) is enabled on the account | Kept for now; noted in MIC-DEC-005 |

## Root user activity record

| Date | Purpose | Why root was required |
|---|---|---|
| 22 Sep 2026 | Assign root MFA | Only root can manage root's own MFA |
| 22 Sep 2026 | Delete `UserA`; create `mitchell-admin` and the `Administrators` group | No other administrator existed yet |
| 22 Sep 2026 | Activate IAM access to billing information | This setting can only be changed by root |

## Build log

**22 September 2026 — Week 1: account security and tooling**

- Checked credits and plan status. The console shows the free plan ends **28 February 2027**, which is the teardown deadline. After the AWS Budgets activity, credits remaining read USD 145.75.
- Locked root with a passkey. An attempt to add a second MFA device failed because the session pre-dated the first device: AWS requires an MFA-authenticated session to change MFA settings.
- Deleted the legacy user, created `mitchell-admin` with MFA through a group, and activated IAM billing access.
- Created the credit-excluding budget; its first alert fired immediately.
- Cleaned up tutorial leftovers in Mumbai.
- Installed the toolchain. `code`, `aws` and `terraform` were not found until a full restart refreshed the Windows PATH, and the Microsoft Store "python" alias had to be disabled.
- Signed the CLI in with `aws login`, with no keys stored anywhere.
- Decisions recorded: MIC-DEC-007 (single-account lab) and MIC-DEC-008 (lab identity).

## Open actions

- [ ] Add a backup authenticator-app MFA device to root
- [ ] Delete the unused `DemoS3Access` group (full S3 access, no members)
- [ ] Delete the tutorial key pair in Mumbai and its local `.pem` file (F-04)
- [ ] Set an account alias
- [ ] Confirm `Owner` and `Project` tags on `mitchell-admin` and on the budget
- [ ] Set the CLI default region permanently: `aws configure set region ap-south-1`
- [ ] Capture and add the screenshots for EV-001, EV-003, EV-004, EV-005 and EV-006
- [ ] Strip all rules from the default security groups, via Terraform (planned)
- [ ] Run `aws logout` at the end of each working day
---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
