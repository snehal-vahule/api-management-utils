#!/usr/bin/env python

"""
purge_incorrect_env_vars.py

Takes data from monitoring and value to be removed, and removes offending entires.

Usage:
  purge_incorrect_env_vars.py [-v <value> | --value=<value>]
  purge_incorrect_env_vars.py (-h | --help)

Options:
  -h --help                        Show this screen.
  -v <value> | --value=<value>     String value to be removed
"""

import json
import requests
import os
from docopt import docopt

TOKEN = os.getenv('TOKEN')


def delete_offending_entires(json_data, offending_str):
	for api in json_data:
		for env in json_data[api]:
			for line in json_data[api][env]:
				if offending_str in line:
					print(line)


def main(args):
    input_value = str(args["--value"])

    
    org_name = "nhsd-nonprod"
    env_name = "internal-dev"
    map_name = "monitoring-sd-service"
    entry_name = "entries"
    url = f"https://api.enterprise.apigee.com/v1/organizations/{org_name}/environments/{env_name}/keyvaluemaps/{map_name}/entries/{entry_name}"
    auth = f"Bearer {TOKEN}"
    resp = requests.get(url, headers = {"Authorization": auth})

    json_data = json.loads(resp.text).get('value')
    json_data = json.loads(json_data)


    delete_offending_entires(json_data, input_value)



if __name__ == "__main__":
     main(docopt(__doc__, version="1"))
