variable "location" {
  type        = string
  description = "The location for the resources"
}

variable "resource_group_name" {
  type        = string
  description = "The name of the resource group"
}

variable "storage_account_name" {
  type        = string
  description = "The name of the storage account"
}

variable "application_insights_name" {
  type        = string
  description = "The name of the Application Insights"
}

variable "key_vault_name" {
  type        = string
  description = "The name of the Key Vault"
}

variable "ml_workspace_name" {
  type        = string
  description = "The name of the Machine Learning workspace"
}

variable "account_tier" {
  description = "The performance tier of the storage account"
  type        = string
  default     = "Standard"
}

variable "account_replication_type" {
  description = "The replication type of the storage account"
  type        = string
  default     = "LRS"
}
