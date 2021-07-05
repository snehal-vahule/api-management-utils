#!/bin/bash

export STATUS='200'
export PING='200'
export NAME='personal-demographics/FHIR/R4-pr-625'

# if [[ $NAME == *"-pr-"* ]]; then
# echo "It's a pull request"
# export is_pull_request=true
# fi

# if [[ $STATUS == "200" ]]; then
#     echo "STATUS_PRESENT=true"
# else 
# echo "STATUS_PRESENT=false" 
# fi

# if [[ $PING == "200" ]]; then
#     echo "PING_PRESENT=true"
# else 
#     echo "PING_PRESENT=false" 
# fi

# if [[  $is_pull_request ]]; then
#     echo "is boolean"
# fi


# if [[ "${{ parameters.apigee_environment }}" == "prod" ]]; then
# export status_endpoint_response=`curl -s -o /dev/null -w '%{http_code}' -H "apikey: $(MONITORING_API_KEY)" https://api.service.nhs.uk/${{ parameters.service_base_path }}/_status`
# export ping_endpoint_response=`curl -s -o /dev/null -w '%{http_code}' -H "apikey: $(MONITORING_API_KEY)" https://api.service.nhs.uk/${{ parameters.service_base_path }}/_ping`
# else
# export status_endpoint_response=`curl -s -o /dev/null -w '%{http_code}' -H "apikey: $(MONITORING_API_KEY)" https://${{ parameters.apigee_environment }}.api.service.nhs.uk/${{ parameters.service_base_path }}/_status`
# export ping_endpoint_response=`curl -s -o /dev/null -w '%{http_code}' -H "apikey: $(MONITORING_API_KEY)" https://${{ parameters.apigee_environment }}.api.service.nhs.uk/${{ parameters.service_base_path }}/_ping`
# fi

if [[ "$NAME" == *"-pr-"* ]]; then
export is_pull_request=true
fi

if [[ $status_endpoint_response == "200" ]]; then
if [[ $is_pull_request ]]; then
    echo do nothing
else
    echo "enable_status_monitoring=true"
fi
else
if [[ $is_pull_request ]]; then
    echo "WARNING: Please add a _status endpoit to your proxy before releasing"
else
    "ERROR: Your proxy doesnt have a _status endpoint therefore we can't monitor this proxy therefore it should not be released"
    exit 1
fi
fi

if [[  $ping_endpoint_response == "200" ]]; then
if [[ $is_pull_request ]]; then
    echo do nothing
else
    echo "enable_ping_monitoring=true"
fi
else
echo "enable_ping_monitoring=false"
fi