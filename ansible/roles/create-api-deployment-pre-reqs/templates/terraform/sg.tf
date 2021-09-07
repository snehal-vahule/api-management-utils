
resource "aws_security_group" "api-deployment" {

  vpc_id      = data.terraform_remote_state.account.outputs.account_vpc.id
  name        = "api-${local.env_service_id}"
  description = "api-${local.env_service_id} specific rules"

  tags = {
    Name   = "api-${local.env_service_id}"
    source = "terraform"
    api-service = var.service_id
    api-environment = var.apigee_environment
  }
}
