az login

templateFile="./personalizedeploy.json"
parameterFile="./personalizedeploy.parameters.json"

echo "creating resource group..."
az group create \
--name paramsgroup \
--location "eastus"
echo "resource group created"

python updateparams.py

echo "deploying"

az deployment group create \
--name testingwithparams \
--resource-group paramsgroup \
--template-file $templateFile \
--parameters $parameterFile 
#acrName=acrscripttest2

echo "deployment complete"
