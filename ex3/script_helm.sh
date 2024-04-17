helm repo add --force-update port-labs https://port-labs.github.io/helm-charts
helm upgrade --install my-jira-integration port-labs/port-ocean \
        --set port.clientId="WL92dw5KSobwoBwLOa7UTgMob8gBgB8G"  \
        --set port.clientSecret="lBbnVGRDRejTA3p0yLrHEYxROSuSaheqvJORZPj2duPkDruIIsqpo6fN273oFx4o"  \
        --set port.baseUrl="https://api.getport.io"  \
        --set initializePortResources=true  \
        --set scheduledResyncInterval=120 \
        --set integration.identifier="my-jira-integration"  \
        --set integration.type="jira"  \
        --set integration.eventListener.type="POLLING"  \
        --set integration.config.jiraHost="https://edenb.atlassian.net/"  \
        --set integration.secrets.atlassianUserEmail="edenb54321@gmail.com"  \
        --set integration.secrets.atlassianUserToken="ATATT3xFfGF0jgEU9ErmZWMnYLHrwMeE3vnp6TIlEwS4FiiZM8ueSkeWaqz3LAp4wMtS_iT-mnFVHWWiDzZ9JQ5_vjJSZ-mbJwhMJ-gIoHIk6qPfUWYAl3JNqyI7bJ3N7eYw2fL7TcE_j6f1r6q369_YnzI9_haiZrge0X5POjy1jTCSgdPyrg8=23E4A509"