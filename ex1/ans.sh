# extract the value of the key "spec.replicas" from the file k8s-deploy.json
ans_a=$(jq '.spec.replicas' ./k8s-deploy.json)
echo "Number of replicas: $ans_a"

# extract the value of the key "spec.strategy.type" from the file k8s-deploy.json
ans_b=$(jq '.spec.strategy.type' ./k8s-deploy.json)
echo "Strategy type: $ans_b"

# extract the value of the key "spec.strategy.rollingUpdate.maxSurge" from the file k8s-deploy.json
ans_c=$(jq '"\(.metadata.labels.service)-\(.metadata.labels.environment)"' ./k8s-deploy.json)
echo "Service and Environment: $ans_c"

# Main task
# Capture the output of the jq command into a variable and printing the array from issue-repsonse.json
output=$(jq -r '.fields.subtasks[].key' ./issue-repsonse.json)
echo "All issue IDs in a subtask:"
echo $output

