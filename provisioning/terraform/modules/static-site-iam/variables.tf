variable "bucket_name" {
  description = "Name of the S3 bucket in the form of a domain name"
  type        = string
}

variable "bucket_arn" {
  description = "ARN of the S3 bucket"
  type        = string
}

variable "ci_user_name" {
  description = "IAM user name for CI/CD"
  type        = string
}
