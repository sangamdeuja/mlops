// Outputs to display information about created resources
output "resource_group_name" {
  value = module.resource_group.resource_group_name
}

output "storage_account_name" {
  value = module.storage_account.storage_account_name
}
