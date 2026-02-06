import json
id_delete = int(input("Enter product ID delete: "))
with open("products.json", "r", encoding="utf-8") as f: 
    data = json.load(f)
new_data = [dt for dt in data if dt["id"] != id_delete]
with open("products.json", "w", encoding="utf-8") as f:
    json.dump(new_data, f, indent=4, ensure_ascii=False)
print("Item remove successfully.")
