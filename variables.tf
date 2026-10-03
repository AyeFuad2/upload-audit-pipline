variable "aws_region" {
  description = "AWS Region for the upload audit pipeline."
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name prefix for the upload audit resources."
  type        = string
  default     = "upload-audit"
}