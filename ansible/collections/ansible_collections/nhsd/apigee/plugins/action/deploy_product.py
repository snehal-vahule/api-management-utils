from ansible_collections.nhsd.apigee.plugins.module_utils.apigee_action import (
    ApigeeAction,
)
from ansible_collections.nhsd.apigee.plugins.module_utils.models.ansible.deploy_product import (
    DeployProduct,
)

APIGEE_BASE_URL = "https://api.enterprise.apigee.com/v1/"


class ActionModule(ApigeeAction):
    def run(self, tmp=None, task_vars=None):
        super(ActionModule, self).run(tmp, task_vars)
        args, errors = self.validate_args(DeployProduct)
        if errors:
            return errors

        diff_mode = self._play_context.diff
        check_mode = self._play_context.check_mode

        product = args.product
        organization = args.organization

        products_path = f"organizations/{organization}/apiproducts"
        current_path = products_path + f"/{product.name}"
        current_response = self.get(APIGEE_BASE_URL + current_path, args.access_token, status_code=[200, 404])
        if current_response.get("failed"):
            return current_response

        if current_response["response"]["status_code"] == 200:
            # Already exists
            current_product = current_response["response"]["body"]
            update_method = "PUT"
            update_path = current_path
            update_status_code = [200]
        elif current_response["response"]["status_code"] == 404:
            # Does not exist
            current_product = {}
            update_method = "POST"
            update_path = products_path
            update_status_code = [201]

        before = current_product
        after = product.dict()

        # These are generated by apigee outside our control so it
        # makes no sense to include them in the delta.
        keys_to_ignore = [
            "lastModifiedAt",
            "apiResources",
            "createdAt",
            "createdBy",
            "lastModifiedBy",
        ]
        delta = self.delta(
            before,
            after,
            keys_to_ignore=keys_to_ignore,
        )
        result = {"product": after, "changed": True if delta else False}

        #  Include full diff details if ansible-playbook --diff flag passed.
        if diff_mode:
            result["diff"] = [
                {
                    "before_header": before.get("name", ""),
                    "before": {
                        k: v for k, v in before.items() if k not in keys_to_ignore
                    },
                    "after_header": after.get("name", ""),
                    "after": {
                        k: v for k, v in after.items() if k not in keys_to_ignore
                    },
                }
            ]

        if not delta or check_mode:
            # Do not make any changes to apigee and exit.
            return result

        # POST/PUT the product
        new_response = self.request(
            update_method,
            APIGEE_BASE_URL + update_path,
            args.access_token,
            json=after,
            status_code=update_status_code,
        )
        if new_response.get("failed"):
            return new_response

        result["product"] = new_response["response"]["body"]
        if diff_mode:
            result["diff"][0]["after"]: {
                k: v for k, v in result["product"].items() if k not in keys_to_ignore
            }

        return result
