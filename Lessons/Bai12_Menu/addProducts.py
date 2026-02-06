data = [
  {"id": 1, "name": "Laptop", "price": 1500, "stock": 10},
  {"id": 2, "name": "Mouse", "price": 20, "stock": 50}
]

import json

with open("products.json", "w", encoding= "utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
