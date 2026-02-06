import json
with open("products.json", "r", encoding="utf-8") as f:
    data = json.load(f)
for pd in data:
    print("ID:", pd["id"], " - ", pd["name"], " - ", pd["price"], " USD" )