#
# This file is used to define resources for managing permissions to resources related to this project

# Access Keys
#
# IAM Access Keys/Secrets MUST NOT be created through Terraform to ensure this project can be open-sourced later.
# Instead Access Keys/Secrets MAY be created through either the AWS Console or AWS APIs/SDKs.

#    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *
#
# Principles
#
#    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *

# Continuous Delivery Principle
#
# This resource relies on the AWS Terraform provider being previously configured.
#
# AWS source: https://aws.amazon.com/iam/
# Terraform source: https://www.terraform.io/docs/providers/aws/r/iam_user.html
resource "aws_iam_user" "bas-gitlab-ci-bas-metadata-standards" {
  name = "bas-gitlab-ci-bas-metadata-standards"
}

#    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *
#
# Policy definitions & assignments
#
#    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *

# Bucket management policy (Staging)
#
# Policy to manage the S3 bucket holding static website content
#
# Inline policy
#
# This resource implicitly depends on the 'aws_iam_user.bas-gitlab-ci-bas-metadata-standards' resource
# This resource relies on the AWS Terraform provider being previously configured.
#
# AWS source: http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies
# Terraform source: https://www.terraform.io/docs/providers/aws/r/iam_user_policy.html
#
# Tags are not supported by this resource
resource "aws_iam_user_policy" "bas-metadata-standards-staging-management-policy" {
  name   = "bas-metadata-standards-staging-management-policy"
  user   = "${aws_iam_user.bas-gitlab-ci-bas-metadata-standards.name}"
  policy = "${file("70-resources/iam/policies/inline/staging-bucket.json")}"
}

# Bucket management policy (Production)
#
# Policy to manage the S3 bucket holding static website content
#
# Inline policy
#
# This resource implicitly depends on the 'aws_iam_user.bas-gitlab-bas-metadata-standards' resource
# This resource relies on the AWS Terraform provider being previously configured.
#
# AWS source: http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies
# Terraform source: https://www.terraform.io/docs/providers/aws/r/iam_user_policy.html
#
# Tags are not supported by this resource
resource "aws_iam_user_policy" "bas-metadata-standards-production-management-policy" {
  name   = "bas-metadata-standards-production-management-policy"
  user   = "${aws_iam_user.bas-gitlab-ci-bas-metadata-standards.name}"
  policy = "${file("70-resources/iam/policies/inline/production-bucket.json")}"
}
