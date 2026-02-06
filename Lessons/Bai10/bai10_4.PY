import json
name_to_find = input("Enter name to find: ").strip().lower()
with open("products.json", "r", encoding="utf-8") as f: 
    data = json.load(f)
found = False
for dt in data: 
    if dt["name"].strip().lower() == name_to_find:
        print("ID: ", dt["id"], " - ", dt["name"], " - ", dt["price"])
        found = True
        break
if not found: 
    print("Not found!")