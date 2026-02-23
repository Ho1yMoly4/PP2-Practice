import json

with open("sample-data.json", "r") as f:
    data = json.load(f)

for user in data["users"]:
    print(user["name"], user["age"])
