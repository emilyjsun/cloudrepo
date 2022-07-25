import json
from addresource import servicesList

file = open("personalizedeploy.parameters.json", "r")
store = json.loads(file.read())
file.close()


# print(store)
paramObj = store["parameters"]
# print(servicesList)
    


for s in servicesList:
    # print(s)
    if(s == "StorageAccount"):
        storageName = input("Storage Name: ")
        paramObj.update({
            "storageName": {
            "value": storageName
        }
        })
    elif(s == "ContainerRegistry"):
        acrName = input("Container Registry Name: ")
        paramObj.update({
            "acrName": {
            "value": acrName
        }
        })
    elif(s == "PostgreSQLFlexible"):
        serverName = input("Server Name: ")
        adminLogin = input("Administrator Login: ")
        adminPassword = input("Administrator Password: ")
        paramObj.update({
            "serverName": {
            "value": serverName
            },
            "administratorLogin": {
                "value": adminLogin
            },
            "administratorLoginPassword": {
                "value": adminPassword
            }

        })
    elif(s == "Kubernetes"):
        clusterName = input("Cluster Name: ")
        prefix = input("DNS Prefix: ")
        user = input("Linux Admin Username:" )
        ssh = input("ssh RSA Public Key: ")
        paramObj.update({
            "clusterName": {
            "value": clusterName
            },
            "dnsPrefix": {
                "value": prefix
            },
            "linuxAdminUsername": {
                "value": user
            },
            "sshRSAPublicKey": {
                "value": ssh
            }

        })
    else:
        print("invalid")



store["parameters"] = paramObj
with open("personalizedeploy.parameters.json", 'w') as json_file:
    json.dump(store, json_file, 
                        indent=4,  
                        separators=(',',': '))

json_file.close()

