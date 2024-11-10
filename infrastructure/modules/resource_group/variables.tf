variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
}

variable "location" {
  description = "The Azure region for the resource group"
  type        = string
  default     = "northeurope"
}
