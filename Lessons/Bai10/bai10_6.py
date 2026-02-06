import json
products = []
with open("products.json", "r", encoding="utf-8") as f:
    data = json.load(f)
for dt in data: 
    dt["price"] = dt["price"] + dt["price"] * 10/100
    products.append(dt)
with open("products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=4, ensure_ascii=False)