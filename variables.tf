variable "resource_group_name" {
  description = "Name of the resource group"
  default     = "TeamCResourcegroup"
}

variable "location" {
  description = "Azure region to deploy resources"
  default     = "Brazil South"
}

variable "vnet_name" {
  description = "Name of the virtual network"
  default     = "TeamCVnet"
}

variable "vmss_sku" {
  description = "SKU for the Virtual Machine Scale Sets"
  default     = "Standard_B1s"
}

variable "web_vmss_instances" {
  description = "Number of instances in the Web Tier VMSS"
  default     = 2
}

variable "business_vmss_instances" {
  description = "Number of instances in the Business Tier VMSS"
  default     = 2
}

variable "admin_password" {
  description = "Admin password for VMs"
  sensitive   = true
}

variable "sql_admin_login" {
  description = "Admin username for SQL Server"
}

variable "sql_admin_password" {
  description = "Admin password for SQL Server"
  sensitive   = true
}