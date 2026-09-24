# Which versions this code needs, pinned so it never changes silently
terraform {
  required_version = ">= 1.16.0"
  required_providers {
    aws    = { source = "hashicorp/aws", version = "~> 6.0" }
    random = { source = "hashicorp/random", version = "~> 3.6" }
  }
}

# Mumbai, and every resource tagged automatically
provider "aws" {
  region = "ap-south-1"
  default_tags {
    tags = {
      Owner     = "mitchell"
      Project   = "meridian-sextant"
      ManagedBy = "terraform"
    }
  }
}

# A random suffix, so the bucket name can't be guessed
resource "random_id" "suffix" {
  byte_length = 3
}

resource "aws_s3_bucket" "lab" {
  bucket        = "sextant-tf01-${random_id.suffix.hex}"
  force_destroy = true # lab only: lets destroy remove it even if it holds files
}

# The fix for flaws.cloud: strangers get nothing
resource "aws_s3_bucket_public_access_block" "lab" {
  bucket                  = aws_s3_bucket.lab.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Keeps old versions of every file, so mistakes can be undone
resource "aws_s3_bucket_versioning" "lab" {
  bucket = aws_s3_bucket.lab.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Encryption at rest, stated in code
resource "aws_s3_bucket_server_side_encryption_configuration" "lab" {
  bucket = aws_s3_bucket.lab.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

output "bucket_name" {
  value = aws_s3_bucket.lab.bucket
}