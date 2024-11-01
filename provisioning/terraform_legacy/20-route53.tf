#
# This file is used to define resources for network resources used to define how users access content

# BAS Metadata standards alias (Production)
#
# This resource implicitly depends on the 'aws_cloudfront_distribution.bas-metadata-standards-production' resource
# This resource explicitly depends on outputs from the the 'terraform_remote_state.BAS-CORE-DOMAINS' data source
# This resource relies on the AWS Terraform provider being previously configured
#
# AWS source: http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rrsets-working-with.html
# Terraform source: https://www.terraform.io/docs/providers/aws/r/route53_record.html
#
# Tags are not supported by this resource
resource "aws_route53_record" "bas-metadata-standards-production" {
  zone_id = "${data.terraform_remote_state.BAS-CORE-DOMAINS.DATA-BAS-AC-UK-ID}"

  name = "metadata-standards"
  type = "CNAME"
  ttl  = 300

  records = [
    "${aws_cloudfront_distribution.bas-metadata-standards-production.domain_name}",
  ]
}
