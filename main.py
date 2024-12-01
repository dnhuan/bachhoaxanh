import json

with open("allStores.json", "r") as f:
    allStores = json.load(f)


allIds = []
for provinceData in allStores["data"]["provinces"]:
    allIds.append(provinceData["id"])

print(allIds)
