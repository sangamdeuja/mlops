terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.9.0"
    }
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_client_config" "current" {
}

module "resource_group" {
  source              = "./modules/resource_group"
  resource_group_name = var.resource_group_name
  location            = var.location
}

module "storage_account" {
  source               = "./modules/storage_account"
  storage_account_name = var.storage_account_name
  resource_group_name  = var.resource_group_name
  location             = var.location
  depends_on           = [module.resource_group]
}

module "application_insight" {
  source                    = "./modules/application_insight"
  application_insights_name = var.application_insights_name
  resource_group_name       = var.resource_group_name
  location                  = var.location
  depends_on                = [module.resource_group]
}

module "key_vault" {
  source              = "./modules/key_vault"
  key_vault_name      = var.key_vault_name
  resource_group_name = var.resource_group_name
  location            = var.location
  depends_on          = [module.resource_group]
}

module "mlworkspace" {
  source                  = "./modules/mlworkspace"
  workspace_name          = var.ml_workspace_name
  resource_group_name     = var.resource_group_name
  location                = var.location
  application_insights_id = module.application_insight.application_insights_id
  key_vault_id            = module.key_vault.key_vault_id
  storage_account_id      = module.storage_account.storage_account_id
  depends_on              = [module.resource_group]

}
