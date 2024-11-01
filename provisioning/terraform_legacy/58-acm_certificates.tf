#
# This file is used to define TLS Server Certificates used by various AWS resources

#    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *
#
# Certificates
#
#    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *

# metadata-standards.data.bas.ac.uk
#
# This resource implicitly depends on the 'aws_s3_bucket.bas-metadata-standards-production' resource
# This resource relies on the AWS Terraform provider ('us-east-1' alias) being previously configured
#
# AWS source: http://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html
# Terraform source: https://www.terraform.io/docs/providers/aws/r/acm_certificate.html
resource "aws_acm_certificate" "bas-metadata-standards-production" {
  provider = "aws.us-east-1"

  domain_name       = "${aws_s3_bucket.bas-metadata-standards-production.bucket}"
  validation_method = "DNS"

  tags {
    Name         = "metadata-standards.data.bas.ac.uk"
    X-Project    = "BAS Metadata Standards"
    X-Managed-By = "Terraform"
  }
}

#    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *
#
# Certificate validation records (Route53)
#
#    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *

# metadata-standards.data.bas.ac.uk
#
# This resource implicitly depends on the 'aws_acm_certificate.bas-metadata-standards-production' resource
# This resource explicitly depends on outputs from the the 'terraform_remote_state.BAS-CORE-DOMAINS' data source
# This resource relies on the AWS Terraform provider being previously configured
#
# AWS source: http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rrsets-working-with.html
# Terraform source: https://www.terraform.io/docs/providers/aws/r/route53_record.html
#
# Tags are not supported by this resource
resource "aws_route53_record" "bas-metadata-standards-production-cert" {
  zone_id = "${data.terraform_remote_state.BAS-CORE-DOMAINS.DATA-BAS-AC-UK-ID}"

  name = "${aws_acm_certificate.bas-metadata-standards-production.domain_validation_options.0.resource_record_name}"
  type = "${aws_acm_certificate.bas-metadata-standards-production.domain_validation_options.0.resource_record_type}"
  ttl  = 60

  records = [
    "${aws_acm_certificate.bas-metadata-standards-production.domain_validation_options.0.resource_record_value}",
  ]
}

#    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *
#
# Certificate validations
#
#    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *    *

# metadata-standards.data.bas.ac.uk
#
# This resource may take a significant time (~30m) to create whilst domain validation is completed
#
# This resource implicitly depends on the 'aws_acm_certificate.bas-metadata-standards-production' resource
# This resource implicitly depends on the 'aws_route53_record.bas-metadata-standards-production-cert' resource
# This resource relies on the AWS Terraform provider ('us-east-1' alias) being previously configured
#
# AWS source: https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html
# Terraform source: https://www.terraform.io/docs/providers/aws/r/acm_certificate_validation.html
#
# Tags are not supported by this resource
resource "aws_acm_certificate_validation" "bas-metadata-standards-production" {
  provider = "aws.us-east-1"

  certificate_arn         = "${aws_acm_certificate.bas-metadata-standards-production.arn}"
  validation_record_fqdns = ["${aws_route53_record.bas-metadata-standards-production-cert.fqdn}"]
}
