# https://www.terraform.io/docs/configuration/providers.html
# https://www.terraform.io/docs/providers/oci/index.html
provider "oci" {
  tenancy_ocid = var.tenancy_ocid
  user_ocid = var.user_ocid
  region = var.region
  fingerprint = var.fingerprint
  private_key_path = var.private_key_path
}