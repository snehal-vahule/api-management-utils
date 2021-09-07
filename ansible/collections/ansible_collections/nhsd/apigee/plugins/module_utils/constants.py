import typing

APIGEE_BASE_URL = "https://api.enterprise.apigee.com/v1/"
APIGEE_DAPI_URL = "https://apigee.com/dapi/api/"

APIGEE_ORG_TO_ENV = {
    "nhsd-nonprod": [
        "internal-dev",
        "internal-dev-sandbox",
        "internal-qa",
        "internal-qa-sandbox",
        "ref",
    ],
    "nhsd-prod": ["dev", "int", "sandbox", "prod"],
}


def portal_uri(org: typing.Literal["nhsd-nonprod", "nhsd-prod"]) -> str:
    portal_ids = {
        "nhsd-nonprod": "nhsd-nonprod-developerportal",
        "nhsd-prod": "nhsd-prod-developerportal",
    }
    if org not in portal_ids:
        raise ValueError(f"Invalid organization name {org}")
    return f"https://apigee.com/portals/api/sites/{portal_ids[org]}/apidocs"



