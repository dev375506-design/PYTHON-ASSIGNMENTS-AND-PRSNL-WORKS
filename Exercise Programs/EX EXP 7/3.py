import json

data = {
    "name": "Dev",
    "age": 20,
    "marks": [85, 90, 88]
}

# Write JSON file
with open("data.json", "w") as f:
    json.dump(data, f)

# Read JSON file
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print("JSON Data:", loaded_data)