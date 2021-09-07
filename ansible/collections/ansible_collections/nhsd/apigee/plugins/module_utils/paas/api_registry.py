import requests
import json


from ansible_collections.nhsd.apigee.plugins.module_utils.paas import urls 


def get(name: str):
    url = urls.api_registry() + f"/api/{name}"
    resp = requests.get(url)

    if resp.status_code != 200:
        try:
            detail = resp.json()["detail"]
        except json.decoder.JSONDecodeError:
            detail = resp.content.decode()
        raise ValueError(detail)
    return resp.json()
