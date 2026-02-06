import json
import sys
input_file = sys.argv[1]
output_file = "result.json"
with open(input_file, "r", encoding="utf-8") as f:
    products = json.load(f)
total = 0
for row in products: 
    total += row["price"]*row["stock"]
result = {"Total_inventory_value": total}
with open(output_file, "w", encoding = "utf-8") as f: 
    json.dump(result, f, indent = 2)
print("Done. Total value: ", total)