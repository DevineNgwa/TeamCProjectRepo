output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}

output "vnet_name" {
  value = azurerm_virtual_network.vnet.name
}

output "application_gateway_public_ip" {
  value = azurerm_public_ip.appgw_public_ip.ip_address
}

output "sql_server_fqdn" {
  value = azurerm_sql_server.sqlserver.fully_qualified_domain_name
}

output "bastion_public_ip" {
  value = azurerm_public_ip.bastion_ip.ip_address
}

output "web_vmss_name" {
  value = azurerm_linux_virtual_machine_scale_set.web_vmss.name
}

output "business_vmss_name" {
  value = azurerm_linux_virtual_machine_scale_set.business_vmss.name
}