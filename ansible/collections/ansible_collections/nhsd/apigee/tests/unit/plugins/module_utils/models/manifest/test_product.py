import pytest

from ansible_collections.nhsd.apigee.plugins.module_utils.models.apigee.product import (
    ApigeeProduct,
)


@pytest.mark.parametrize(
    "env,initial_approvalType,final_approvalType",
    [
        ("prod", "auto", "manual"),
        ("prod", "manual", "manual"),
        ("int", "auto", "auto"),
        ("int", "manual", "manual"),
    ],
)
def test_prod_cannot_have_auto_approvalType_on_products(
    env, initial_approvalType, final_approvalType
):
    raw_product = {
        "name": "test-service",
        "approvalType": initial_approvalType,
        "attributes": [
            {"name": "access", "value": "public"},
            {"name": "ratelimit", "value": "300pm"},
        ],
        "description": "testing our validators",
        "displayName": "Test Product",
        "environments": [env],
        "proxies": [f"identity-service-{env}"],
        "scopes": [
            "urn:nhsd:apim:app:level3:test-service",
            "urn:nhsd:apim:user-nhs-login:P9:test-service",
        ],
        "quota": "300",
        "quotaInterval": "1",
        "quotaTimeUnit": "minute",
    }
    product = ApigeeProduct(**raw_product)
    assert product.approvalType == final_approvalType
