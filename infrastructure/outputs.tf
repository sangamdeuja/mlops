// Outputs to display information about created resources
output "resource_group_name" {
  value = module.storage_module.resource_group_name
}

output "storage_account_name" {
  value = module.storage_module.storage_account_name
}
