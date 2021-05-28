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

@pytest.mark.parametrize(
    "name,env,initial_approvalType,final_approvalType",
    [
        ("canary-api-prod", "prod", "auto", "auto"),
        ("canary-api-prod", "prod", "manual", "manual"),
        ("non-exception-product", "prod", "auto", "manual"),
        ("non-exception-product", "prod", "manual", "manual"),
    ],
)
def test_manual_approval_exception_list_on_prod(
    name, env, initial_approvalType, final_approvalType
):
    raw_product = {
        "name": name,
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
