import typing

import pydantic

from ansible_collections.nhsd.apigee.plugins.module_utils.models.apigee.product import (
    ApigeeProduct,
)


class DeployProduct(pydantic.BaseModel):
    organization: typing.Literal["nhsd-nonprod", "nhsd-prod"]
    access_token: str
    product: ApigeeProduct
