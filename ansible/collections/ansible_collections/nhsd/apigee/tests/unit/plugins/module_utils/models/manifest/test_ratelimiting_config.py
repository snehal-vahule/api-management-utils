import pytest

from ansible_collections.nhsd.apigee.plugins.module_utils.models.apigee.rate_limiting_config import (
    RateLimitingConfig,
)

def test_missing_values_are_not_exported():
    input_dict = {"quota": {"enabled": True}, "spikeArrest": {"enabled": False}}

    ratelimiting = RateLimitingConfig(**input_dict)

    # For it's brief Class-typed existance these things are None.
    assert ratelimiting.quota.interval is None
    assert ratelimiting.quota.limit is None
    assert ratelimiting.quota.timeunit is None
    assert ratelimiting.spikeArrest.ratelimit is None
    
    output_dict = ratelimiting.dict()

    assert output_dict == input_dict
