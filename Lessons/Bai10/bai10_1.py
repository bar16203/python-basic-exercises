import  json
products = [
    {"id": 1, "name": "Laptop", "price": 1500}, 
    {"id": 2, "name": "Mouse", "price": 20}
]
with open("products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=4, ensure_ascii=False)