import pytest

CANARY_API = {
    "guid": "96836235-09a5-4064-9220-0812765ebdd7",
    "name": "canary-api",
    "spec_guids": ["0af08cfb-6835-47b5-867c-95d41ef849b5"],
}


@pytest.fixture()
def canary_guid():
    yield CANARY_API["guid"]


@pytest.fixture()
def canary_spec_guids():
    yield CANARY_API["spec_guids"]


@pytest.fixture()
def invalid_guid():
    """A guid that's not in the (mock) registry."""
    yield "e1650537-76a0-4d30-83ab-947577ed88fd"


@pytest.fixture(autouse=True)
def mock_api_registry(monkeypatch):
    def _mock_api_registry_get(name: str):
        if name == CANARY_API["name"]:
            print("HELLO")
            return CANARY_API
        else:
            raise ValueError(f"No API named {name} found.")

    monkeypatch.setattr(
        "ansible_collections.nhsd.apigee.plugins.module_utils.paas.api_registry.get",
        _mock_api_registry_get,
    )
