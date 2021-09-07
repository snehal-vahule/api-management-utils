from ansible_collections.nhsd.apigee.plugins.module_utils import constants


def org_from_env(environment) -> str:
    """Get nhsd apigee organization name from environment name."""
    for org, envs in constants.APIGEE_ORG_TO_ENV.items():
        if environment in envs:
            return org
    valid_envs = []
    for v in constants.APIGEE_ORG_TO_ENV.values():
        valid_envs = valid_envs + v
    raise ValueError(f"Unknown environment {environment}, valid environments are {valid_envs}")


class FilterModule:

    @staticmethod
    def filters():
        return {
            'org_from_env': org_from_env
        }
