az login

templateFile="./personalizedeploy.json"
parameterFile="./personalizedeploy.parameters.json"

read -p 'Resource Group Name: ' resourceGroupName

echo "creating resource group..."
az group create \
--name $resourceGroupName \
--location "eastus"
echo "resource group created"

python clean.py

python updateparams.py

echo "deploying"
read -p 'Deployment Name: ' deployName

az deployment group create \
--name $deployName \
--resource-group $resourceGroupName \
--template-file $templateFile \
--parameters $parameterFile 
#acrName=acrscripttest2

echo "deployment complete"
