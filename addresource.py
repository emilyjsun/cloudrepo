import json

#reading what exists
file = open("personalizedeploy.json", "r")
store = json.loads(file.read())
file.close()


# print(store)
resourceObj = store["resources"]
paramObj = store["parameters"]
varObj = store["variables"]
outputObj = store["outputs"]

# print(resourceObj)
# print(paramObj)
# print(varObj)
# print(outputObj)

resourceList = ["StorageAccount", "ContainerRegistry", "PostgreSQLFlexible", "Kubernetes", "Done"]
servicesList = []


service = ""

while(service != "Done"):
    print("Options: ", end='')
    print(', '.join(resourceList))
    service = input("Pick a Service: ")

    #adds storage account resource
    if(service == "StorageAccount"):
        resourceList.remove("StorageAccount")
        servicesList.append("StorageAccount")
        paramObj.update({
            "storageName": {
            "type": "string",
            "minLength": 3,
            "maxLength": 24
            },
            "storageSKU": {
            "type": "string",
            "defaultValue": "Standard_LRS",
            "allowedValues": [
                "Standard_LRS",
                "Standard_GRS",
                "Standard_RAGRS",
                "Standard_ZRS",
                "Premium_LRS",
                "Premium_ZRS",
                "Standard_GZRS",
                "Standard_RAGZRS"
            ]
            },
            "location": {
            "type": "string",
            "defaultValue": "[resourceGroup().location]"
            }
        })

        resourceObj.append({
        "type": "Microsoft.Storage/storageAccounts",
            "apiVersion": "2021-09-01",
            "name": "[parameters('storageName')]",
            "location": "[parameters('location')]",
            "sku": {
                "name": "[parameters('storageSKU')]"
            },
            "kind": "StorageV2",
            "properties": {
                "supportsHttpsTrafficOnly": True
            } 
        })
        outputObj.update({
        "storageEndpoint": {
            "type": "object",
            "value": "[reference(parameters('storageName')).primaryEndpoints]"
        }
        })
    #adds container registry service
    elif(service == "ContainerRegistry"):
        resourceList.remove("ContainerRegistry")
        servicesList.append("ContainerRegistry")
        paramObj.update({
        "acrName": {
        "type": "string",
        "maxLength": 50,
        "minLength": 5
        },
        "acrAdminUserEnabled": {
        "type": "bool",
        "defaultValue": False,
        },
        "location": {
        "type": "string",
        "defaultValue": "[resourceGroup().location]",
        },
        "acrSku": {
        "type": "string",
        "defaultValue": "Basic",
        "allowedValues": [
            "Basic",
            "Standard",
            "Premium"
        ]
        }
        })
        resourceObj.append({
        "type": "Microsoft.ContainerRegistry/registries",
        "apiVersion": "2019-12-01-preview",
        "name": "[parameters('acrName')]",
        "location": "[parameters('location')]",
        "tags": {
            "displayName": "Container Registry",
            "container.registry": "[parameters('acrName')]"
        },
        "sku": {
            "name": "[parameters('acrSku')]"
        },
        "properties": {
            "adminUserEnabled": "[parameters('acrAdminUserEnabled')]"
        }
        })
        outputObj.update({
        "acrLoginServer": {
        "type": "string",
        "value": "[reference(resourceId('Microsoft.ContainerRegistry/registries', parameters('acrName'))).loginServer]"
        }
        })
    #add postgresql flexible server    
    elif(service == "PostgreSQLFlexible"):
        resourceList.remove("PostgreSQLFlexible")
        servicesList.append("PostgreSQLFlexible")
        paramObj.update({
            "administratorLogin": {
            "type": "string"
        },
        "administratorLoginPassword": {
            "type": "secureString"
        },
        "location": {
            "type": "string",
            "defaultValue": "[resourceGroup().location]"
        },
        "serverName": {
            "type": "string"
        },
        "serverEdition": {
            "type": "string",
            "defaultValue": "GeneralPurpose"
        },
        "skuSizeGB": {
            "type": "int",
            "defaultValue": 128
        },
        "dbInstanceType": {
            "type": "string",
            "defaultValue": "Standard_D4ds_v4"
        },
        "haMode": {
            "type": "string",
            "defaultValue": "ZoneRedundant"
        },
        "availabilityZone": {
            "type": "string",
            "defaultValue": "1"
        },
        "version": {
            "type": "string",
            "defaultValue": "12"
        },
        "virtualNetworkExternalId": {
            "type": "string",
            "defaultValue": ""
        },
        "subnetName": {
            "type": "string",
            "defaultValue": ""
        },
        "privateDnsZoneArmResourceId": {
            "type": "string",
            "defaultValue": ""
        }
        })
        resourceObj.append({
            "type": "Microsoft.DBforPostgreSQL/flexibleServers",
            "apiVersion": "2021-06-01",
            "name": "[parameters('serverName')]",
            "location": "[parameters('location')]",
            "sku": {
            "name": "[parameters('dbInstanceType')]",
            "tier": "[parameters('serverEdition')]"
            },
            "properties": {
            "version": "[parameters('version')]",
            "administratorLogin": "[parameters('administratorLogin')]",
            "administratorLoginPassword": "[parameters('administratorLoginPassword')]",
            "network": {
                "delegatedSubnetResourceId": "[if(empty(parameters('virtualNetworkExternalId')), json('null'), json(format('{0}/subnets/{1}', parameters('virtualNetworkExternalId'), parameters('subnetName'))))]",
                "privateDnsZoneArmResourceId": "[if(empty(parameters('virtualNetworkExternalId')), json('null'), parameters('privateDnsZoneArmResourceId'))]"
            },
            "highAvailability": {
                "mode": "[parameters('haMode')]"
            },
            "storage": {
                "storageSizeGB": "[parameters('skuSizeGB')]"
            },
            "backup": {
                "backupRetentionDays": 7,
                "geoRedundantBackup": "Disabled"
            },
            "availabilityZone": "[parameters('availabilityZone')]"
            }
        })
    elif(service == "Kubernetes"):
        resourceList.remove("Kubernetes")
        servicesList.append("Kubernetes")
        paramObj.update({
        "clusterName": {
        "type": "string",
        "defaultValue": "aks101cluster"
      },
      "location": {
        "type": "string",
        "defaultValue": "[resourceGroup().location]"
      },
      "dnsPrefix": {
        "type": "string"
      },
      "osDiskSizeGB": {
        "type": "int",
        "defaultValue": 0,
        "maxValue": 1023,
        "minValue": 0
      },
      "agentCount": {
        "type": "int",
        "defaultValue": 3,
        "maxValue": 50,
        "minValue": 1
      },
      "agentVMSize": {
        "type": "string",
        "defaultValue": "Standard_D2s_v3"
      },
      "linuxAdminUsername": {
        "type": "string"
      },
      "sshRSAPublicKey": {
        "type": "string"
      }
        })
        resourceObj.append({
                    "type": "Microsoft.ContainerService/managedClusters",
        "apiVersion": "2020-09-01",
        "name": "[parameters('clusterName')]",
        "location": "[parameters('location')]",
        "identity": {
          "type": "SystemAssigned"
        },
        "properties": {
          "dnsPrefix": "[parameters('dnsPrefix')]",
          "agentPoolProfiles": [
            {
              "name": "agentpool",
              "osDiskSizeGB": "[parameters('osDiskSizeGB')]",
              "count": "[parameters('agentCount')]",
              "vmSize": "[parameters('agentVMSize')]",
              "osType": "Linux",
              "mode": "System"
            }
          ],
          "linuxProfile": {
            "adminUsername": "[parameters('linuxAdminUsername')]",
            "ssh": {
              "publicKeys": [
                {
                  "keyData": "[parameters('sshRSAPublicKey')]"
                }
              ]
            }
          }
        }
        })
        outputObj.update({
        "controlPlaneFQDN": {
        "type": "string",
        "value": "[reference(resourceId('Microsoft.ContainerService/managedClusters', parameters('clusterName'))).fqdn]"
      }
        })
    elif(service == "Done"):
        break
    else:
        print("invalid")

store["resources"] = resourceObj
store["parameters"] = paramObj
store["variables"] = varObj
store["outputs"] = outputObj

with open("personalizedeploy.json", 'w') as json_file:
    json.dump(store, json_file, 
                        indent=4,  
                        separators=(',',': '))

json_file.close()

