# Required by the OCI Provider
variable "tenancy_ocid" {}
 
variable "user_ocid" {}
variable "fingerprint" {}
variable "private_key_path" {}
variable "compartment_ocid" {}
 
variable "ssh_public_key_file" {
  default = "~/.ssh/id_rsa.pub"
}
 
variable "region" {
  default = "uk-london-1"
}
 
# Choose an Availability Domain
variable "availability_domain" {
  default = "3"
}
 
variable "internet_gateway_enabled" {
  default = "true"
}
 
variable "worker_ol_image_name" {
  default = "Oracle-Linux-7.6"
}
 
variable "oke" {
  type = map(string)
 
  default = {
    name             = "oke"
    version          = "v1.18.10"
    shape            = "VM.Standard2.1"
    nodes_per_subnet = 1
  }
}
 
variable "network_cidrs" {
  type = map(string)
 
  default = {
    vcnCIDR               = "10.0.0.0/16"
    workerSubnetAD1       = "10.0.10.0/24"
    workerSubnetAD2       = "10.0.11.0/24"
    workerSubnetAD3       = "10.0.12.0/24"
    LoadBalancerSubnetAD1 = "10.0.20.0/24"
    LoadBalancerSubnetAD2 = "10.0.21.0/24"
    LoadBalancerSubnetAD3 = "10.0.22.0/24"
  }
}
