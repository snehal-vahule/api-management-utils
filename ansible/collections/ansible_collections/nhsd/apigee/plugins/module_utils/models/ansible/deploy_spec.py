import pydantic
import typing

from ansible_collections.nhsd.apigee.plugins.module_utils.models import apigee


class DeploySpec(pydantic.BaseModel):
    spec: apigee.spec.ApigeeSpec
    organization: typing.Literal["nhsd-nonprod", "nhsd-prod"]
    access_token: str
