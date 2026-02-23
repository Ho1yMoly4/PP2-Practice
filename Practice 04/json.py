#JSON Syntax

import json

__________________________________

#Parsing JSON (json.loads())

import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)
print(y["age"])

__________________________________

#Converting Python to JSON (json.dumps())

import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)
print(y)

__________________________________

#Writing JSON files

import json

data = {
    "name": "Alice",
    "age": 25,
    "active": True
}

with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

__________________________________

#Reading JSON files

import json

with open("output.json", "r") as f:
    data = json.load(f)

print(data["name"])
print(data["age"])

