# MIC-DEC-011 — Where infrastructure code lives, and state is never committed

| Field | Value |
|---|---|
| ID | MIC-DEC-011 |
| Status | Accepted |
| Decided | 24 September 2026 |
| Recorded | 24 September 2026 |
| Author | Mitchell Swapnil Chatterjee |
| Related | MIC-DEC-008, MIC-EVD-001 (EV-011), MIC-MTH-002 |

## Context

The first Terraform exercise produced three kinds of file: the code (`main.tf`), a provider lock file, and **state** (`terraform.tfstate`). State records everything Terraform manages and can contain sensitive values, such as resource identifiers, and in later builds possibly secrets. The repository is public. The existing folders `00` to `06` hold documents, not code.

## Decision

- Infrastructure code lives in **`meridian-infotech/07_Infrastructure/`**: `labs/` for exercises that are built, tested and destroyed; a platform folder for Sextant's own code once the build begins.
- A **`.gitignore`** in that folder excludes state, local provider caches, saved plans, variable files and crash logs, so they cannot be committed by accident.
- The **provider lock file is committed**, so every run uses the same provider versions. Terraform and provider versions are pinned in code.
- Changes are applied from a **saved, reviewed plan** (`terraform plan -out`, then `terraform apply` on that plan).
- Terraform runs as `mitchell-admin` through the `aws login` session. No access keys, and no credentials exported into the terminal.

## Alternatives considered

- **Keep code outside the repository.** Rejected: code is the strongest evidence that controls are designed in, and hiding it loses that.
- **Commit state for convenience.** Rejected: publishing state is a well-known way that secrets and infrastructure details leak.

## Consequences

- Lab exercises keep their state locally and are destroyed after testing, so their state holds nothing.
- The platform build will need **remote state**: an encrypted, versioned, non-public S3 bucket with state locking, created in October.
- Checkov will scan everything in `07_Infrastructure` once the CI pipeline exists.
---

> **Disclosure.** Meridian Infotech Consultancy Ltd, Meridian Sextant and every named client are fictional. This is a simulated, self-directed portfolio exercise, not work for a real client or employer. Where a record describes the AWS lab environment, that environment is real and operated personally by the author.
