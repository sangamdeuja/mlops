variable "workspace_name" {
  type = string
}

variable "resource_group_name" {
  type = string
}

variable "location" {
  type = string
}


variable "storage_account_id" {
  type        = string
  description = "The ID of the Storage Account linked to AML workspace"
}

variable "key_vault_id" {
  type        = string
  description = "The ID of the Key Vault linked to AML workspace"
}

variable "application_insights_id" {
  type        = string
  description = "The ID of the Application Insights linked to AML workspace"
}


