import json

#clean template
file = open("personalizedeploy.json", "r")
store = json.loads(file.read())
file.close()

store = {
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {},
    "variables": {},
    "resources": [],
    "outputs":{}
}

with open("personalizedeploy.json", 'w') as json_file:
    json.dump(store, json_file, 
                        indent=4,  
                        separators=(',',': '))

json_file.close()


#clean parameters
file = open("personalizedeploy.parameters.json", "r")
store = json.loads(file.read())
file.close()

store = {
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {}
}

with open("personalizedeploy.parameters.json", 'w') as json_file:
    json.dump(store, json_file, 
                        indent=4,  
                        separators=(',',': '))

json_file.close()