output "aws_region" {
  description = "AWS Region containing the pipeline."
  value       = var.aws_region
}

output "upload_bucket_name" {
  description = "Name of the S3 upload bucket."
  value       = module.upload_audit.upload_bucket_name
}

output "audit_table_name" {
  description = "Name of the DynamoDB audit table."
  value       = module.upload_audit.audit_table_name
}

