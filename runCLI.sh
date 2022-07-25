az login

templateFile="./personalizedeploy.json"

echo "creating resource group..."
az group create \
--name bashresourcegrouptest \
--location "eastus"
echo "resource group created"

python addresource.py

echo "deploying"

az deployment group create \
--name usingbash \
--resource-group bashresourcegrouptest \
--template-file $templateFile \
--parameters storageName=bashstoragetest1 
#acrName=acrscripttest2

echo "deployment complete"
