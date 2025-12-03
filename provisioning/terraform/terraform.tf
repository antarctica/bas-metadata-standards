## Core
##

terraform {
  required_version = "~> 1.9"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  # Remote state backend
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

# Alias for use with resources or data-sources that require the 'us-east-1' region,
# which is used as a control region by AWS for some services.
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


resource "aws_route53_record" "docs" {
  zone_id = data.terraform_remote_state.BAS-CORE-DOMAINS.outputs.DATA-BAS-AC-UK-ID

  name = "metadata-standards"
  type = "CNAME"
  ttl  = 300

  records = [
    "haproxy0.nerc-bas.ac.uk",
  ]
}

resource "aws_iam_user" "gitlab-ci" {
  name = "bas-gitlab-ci-bas-metadata-standards"
}

module "resources_test" {
  source = "./modules/static-site"

  providers = {
    aws.us-east-1 = aws.us-east-1
  }

  bucket_name        = "metadata-resources-testing.data.bas.ac.uk"
  route53_zone_id    = data.terraform_remote_state.BAS-CORE-DOMAINS.outputs.DATA-BAS-AC-UK-ID
  cloudfront_comment = "BAS Metadata Standards resources (Testing)"
  ci_user_name       = aws_iam_user.gitlab-ci.name

  tags = {
    Name         = "metadata-resources-testing"
    X-Project    = "BAS Metadata Standards"
    X-Managed-By = "Terraform"
  }
}

module "resources_prod" {
  source = "./modules/static-site"

  providers = {
    aws.us-east-1 = aws.us-east-1
  }

  bucket_name        = "metadata-resources.data.bas.ac.uk"
  route53_zone_id    = data.terraform_remote_state.BAS-CORE-DOMAINS.outputs.DATA-BAS-AC-UK-ID
  cloudfront_comment = "BAS Metadata Standards resources"
  ci_user_name       = aws_iam_user.gitlab-ci.name

  tags = {
    Name         = "metadata-resources"
    X-Project    = "BAS Metadata Standards"
    X-Managed-By = "Terraform"
  }
}


  }


  }
}

