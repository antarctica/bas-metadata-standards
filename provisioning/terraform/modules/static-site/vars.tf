variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
}

variable "route53_zone_id" {
  description = "Route53 zone ID for DNS records"
  type        = string
}

variable "cloudfront_comment" {
  description = "Comment for the CloudFront distribution"
  type        = string
}

variable "ci_user_name" {
  description = "IAM user name for CI/CD"
  type        = string
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default     = {}
}
