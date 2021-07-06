#!/bin/bash

export NAME='canary-api-utils-pr-331'
export status_endpoint_response=`curl -s -o /dev/null -w '%{http_code}' -H "apikey: 3fed41a7-1de3-4e03-980b-5945a4c06c86" https://internal-dev.api.service.nhs.uk/canary-api-utils-pr-331/_status`
export ping_endpoint_response=`curl -s -o /dev/null -w '%{http_code}' -H "apikey: 3fed41a7-1de3-4e03-980b-5945a4c06c86" https://internal-dev.api.service.nhs.uk/canary-api-utils-pr-331/_ping`

if [[ "$NAME" == *"-pr-"* ]]; then
export is_pull_request=true
fi

if [[ $status_endpoint_response == '200' ]]; then
if [[ $is_pull_request ]]; then
    echo "status is ok and is pull request"
else
    echo "status is ok, enable_status_monitoring=true"
fi
else
if [[ $is_pull_request ]]; then
    echo "status is no ok and is pull request"
    echo "WARNING: Please add a _status endpoit to your proxy before releasing"
else
    "ERROR: Your proxy doesnt have a _status endpoint therefore we can't monitor this proxy therefore it should not be released"
    exit 1
fi
fi

if [[  $ping_endpoint_response == "200" ]]; then
if [[ $is_pull_request ]]; then
    echo 'ping is ok and is pull request'
else
    echo "enable_ping_monitoring=true"
fi
else
echo "enable_ping_monitoring=false"
fi