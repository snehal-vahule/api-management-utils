import pydantic
import typing

from ansible_collections.nhsd.apigee.plugins.module_utils.models.apigee.apidoc import ApigeeApidoc


class DeployApidoc(pydantic.BaseModel):
    api_catalog_item: ApigeeApidoc
    organization: typing.Literal["nhsd-nonprod", "nhsd-prod"]
    access_token: str
