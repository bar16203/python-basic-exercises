import json
with open("products.json", "r", encoding="utf-8") as f:
    data = json.load(f)
pd_id = int(input("Enter product ID: "))
pd_name = input("Enter product name: ")
pd_price = int(input("Enter product price: "))
new_product = {
    "id": pd_id, 
    "name": pd_name, 
    "price": pd_price
}
data.append(new_product)
with open("products.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent= 4, ensure_ascii=False)