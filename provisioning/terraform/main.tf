terraform {
  required_version = "~> 1.9"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.27"
    }
  }

  # Source: https://gitlab.data.bas.ac.uk/WSF/terraform-remote-state
  backend "s3" {
    bucket = "bas-terraform-remote-state-prod"
    key    = "v2/BAS-METADATA-STANDARDS/terraform.tfstate"
    region = "eu-west-1"
  }
}

provider "aws" {
  region = "eu-west-1"
}

# Alias for resources that require the 'us-east-1' region, which is used as a control region by AWS for some services.
provider "aws" {
  alias  = "us-east-1"
  region = "us-east-1"
}

# Source: https://gitlab.data.bas.ac.uk/WSF/bas-core-domains
data "terraform_remote_state" "BAS-CORE-DOMAINS" {
  backend = "s3"

  config = {
    bucket = "bas-terraform-remote-state-prod"
    key    = "v2/BAS-CORE-DOMAINS/terraform.tfstate"
    region = "eu-west-1"
  }
}

resource "aws_iam_user" "gitlab-ci" {
  name = "bas-gitlab-ci-bas-metadata-standards"
}

variable "static_site_ref" {
  type        = string
  default     = "v0.4.0"
  description = "Static site module version."
}

module "resources_test" {
  source = "git::https://github.com/felnne/tf-aws-static-site.git?ref=${var.static_site_ref}"

  providers = {
    aws.us-east-1 = aws.us-east-1
  }

  site_name                         = "metadata-resources-testing.data.bas.ac.uk"
  route53_zone_id                   = data.terraform_remote_state.BAS-CORE-DOMAINS.outputs.DATA-BAS-AC-UK-ID
  cloudfront_comment                = "BAS Metadata Standards resources (Testing)"
  cloudfront_enable_default_caching = false

  tags = {
    Name         = "metadata-resources-testing"
    X-Project    = "BAS Metadata Standards"
    X-Managed-By = "Terraform"
  }
}
module "resources_test_iam" {
  source = "./modules/static-site-iam"

  bucket_name  = module.resources_test.s3_bucket_name
  bucket_arn   = module.resources_test.s3_bucket_arn
  ci_user_name = aws_iam_user.gitlab-ci.name
}

module "resources_prod" {
  source = "git::https://github.com/felnne/tf-aws-static-site.git?ref=${var.static_site_ref}"

  providers = {
    aws.us-east-1 = aws.us-east-1
  }

  site_name                         = "metadata-resources.data.bas.ac.uk"
  route53_zone_id                   = data.terraform_remote_state.BAS-CORE-DOMAINS.outputs.DATA-BAS-AC-UK-ID
  cloudfront_comment                = "BAS Metadata Standards resources"
  cloudfront_enable_default_caching = false

  tags = {
    Name         = "metadata-resources"
    X-Project    = "BAS Metadata Standards"
    X-Managed-By = "Terraform"
  }
}
module "resources_prod_iam" {
  source = "./modules/static-site-iam"

  bucket_name  = module.resources_prod.s3_bucket_name
  bucket_arn   = module.resources_prod.s3_bucket_arn
  ci_user_name = aws_iam_user.gitlab-ci.name
}

module "docs_test" {
  source = "git::https://github.com/felnne/tf-aws-static-site.git?ref=${var.static_site_ref}"

  providers = {
    aws.us-east-1 = aws.us-east-1
  }

  site_name                         = "metadata-standards-testing.data.bas.ac.uk"
  route53_zone_id                   = data.terraform_remote_state.BAS-CORE-DOMAINS.outputs.DATA-BAS-AC-UK-ID
  cloudfront_comment                = "BAS Metadata Standards (Testing)"
  cloudfront_enable_default_caching = false

  tags = {
    Name         = "metadata-standards-testing"
    X-Project    = "BAS Metadata Standards"
    X-Managed-By = "Terraform"
  }
}
module "docs_test_iam" {
  source = "./modules/static-site-iam"

  bucket_name  = module.docs_test.s3_bucket_name
  bucket_arn   = module.docs_test.s3_bucket_arn
  ci_user_name = aws_iam_user.gitlab-ci.name
}

module "docs_prod" {
  source = "git::https://github.com/felnne/tf-aws-static-site.git?ref=${var.static_site_ref}"

  providers = {
    aws.us-east-1 = aws.us-east-1
  }

  site_name                         = "metadata-standards.data.bas.ac.uk"
  route53_zone_id                   = data.terraform_remote_state.BAS-CORE-DOMAINS.outputs.DATA-BAS-AC-UK-ID
  cloudfront_comment                = "BAS Metadata Standards"
  cloudfront_enable_default_caching = true

  tags = {
    Name         = "metadata-standards"
    X-Project    = "BAS Metadata Standards"
    X-Managed-By = "Terraform"
  }
}
module "docs_prod_iam" {
  source = "./modules/static-site-iam"

  bucket_name  = module.docs_prod.s3_bucket_name
  bucket_arn   = module.docs_prod.s3_bucket_arn
  ci_user_name = aws_iam_user.gitlab-ci.name
}
