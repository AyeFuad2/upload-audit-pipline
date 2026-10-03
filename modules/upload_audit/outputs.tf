output "upload_bucket_name" {
  description = "Name of the S3 upload bucket."
  value       = aws_s3_bucket.uploads.id
}

output "audit_table_name" {
  description = "Name of the DynamoDB audit table."
  value       = aws_dynamodb_table.audit.name
}

