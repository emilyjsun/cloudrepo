import json

#reading what exists
file = open("personalizedeploy.json", "r")
store = json.loads(file.read())
file.close()

#function that adds modifications
# def modify(data):
#     file = open("personalizedeploy.json", "w")
#     file.write(data)
#     file.close()

print(store)
resourceObj = store["resources"]

print(resourceObj)

resourceObj.append({
   "type": "Microsoft.Storage/storageAccounts",
      "apiVersion": "2021-09-01",
      "name": "{provide-unique-name}",
      "location": "eastus",
      "sku": {
        "name": "Standard_LRS"
      },
      "kind": "StorageV2",
      "properties": {
        "supportsHttpsTrafficOnly": True
      } 
})

store["resources"] = resourceObj

with open("personalizedeploy.json", 'w') as json_file:
    json.dump(store, json_file, 
                        indent=4,  
                        separators=(',',': '))

json_file.close()



# import json
# def modifystore(data):
#     file = open("test.json","w")
#     file.write(data)
#     file.close()
# file = open("test.json","r")
# data = json.loads(file.read())
# file.close()
# print(data)
# data.pop("firstName")
# new = json.dumps(data)
# modifystore(new)
# print(data)


# import json
# def modifystore(data):
#     file = open("test.json","w")
#     file.write(data)
#     file.close()
# file = open("test.json","r")
# data = json.loads(file.read())
# file.close()
# print(data)
# data["phoneNumbers"][1]["number"]="+91 XXXXXXXXXX"
# new = json.dumps(data)
# modifystore(new)
# print(data)