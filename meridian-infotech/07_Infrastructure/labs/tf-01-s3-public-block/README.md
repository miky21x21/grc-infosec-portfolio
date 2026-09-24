# Lab 01 — An S3 bucket strangers cannot list

**Date:** 24 September 2026 · **Evidence:** MIC-EVD-001, EV-011 · **Status:** built, tested, destroyed

## Why

On 23 September, the public practice challenge flaws.cloud showed an S3 bucket that let any stranger list its contents, which exposed a "secret" file whose only protection was an obscure name. This lab builds the opposite: a bucket whose protections are written in code, and then attacks it with the same command.

## What the code builds

| Resource | Control |
|---|---|
| `random_id` | A random suffix, so the bucket name cannot be guessed |
| `aws_s3_bucket` | Created in Mumbai, with `Owner`, `Project` and `ManagedBy` tags applied to everything |
| `aws_s3_bucket_public_access_block` | Blocks every route to public access |
| `aws_s3_bucket_versioning` | Keeps old versions, so mistakes can be undone |
| `aws_s3_bucket_server_side_encryption_configuration` | Encryption at rest, stated in code |

S3 already blocks public access and encrypts new buckets by default. The code states these controls anyway, because defaults can change, and written intent can be reviewed and scanned.

## How to run it

```bash
aws login --region ap-south-1
terraform init
terraform plan -out tfplan
terraform apply tfplan
aws s3 ls s3://BUCKET-NAME --no-sign-request --region ap-south-1   # expect AccessDenied
aws s3 ls s3://BUCKET-NAME --region ap-south-1                     # expect success
terraform destroy
```

## Result

The anonymous listing was refused, the owner's succeeded, and the bucket was destroyed in the same session. `force_destroy = true` is set for this lab only, so the bucket can be removed even if it holds files.
