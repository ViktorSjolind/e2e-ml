# End-to-End Example for Deploying ML models
Intended as simple process for demonstrating end-to-end flow.

A production solution would include e.g. security mechanisms on multiple levels

# Deploy Infrastructure
## Setup local environment
az login

az extension add --name containerapp --upgrade

az provider register --namespace Microsoft.App

az provider register --namespace Microsoft.OperationalInsights


$RESOURCE_GROUP = ''

$LOCATION = ''

$CONTAINER_APPS_ENVIRONMENT = ''

$CONTAINER_APPS = ''

$CONTAINER_REGISTRY = ''



## Deploy Resources

az group create --name $RESOURCE_GROUP --location $LOCATION

az containerapp env create --name $CONTAINER_APPS_ENVIRONMENT \
    --resource-group $RESOURCE_GROUP --location $LOCATION

az containerapp create --name $CONTAINER_APPS --resource-group $RESOURCE_GROUP \
    --environment $CONTAINER_APPS_ENVIRONMENT \
    --image mcr.microsoft.com/azuredocs/containerapps-helloworld:latest \
    --target-port 80 --ingress 'external' --query properties.configuration.ingress.fqdn

az acr create --resource-group $RESOURCE_GROUP --name $CONTAINER_REGISTRY --sku Basic

# Pipeline
You need to setup environmental variables, service connections and the appropriate permissions in Azure. 
