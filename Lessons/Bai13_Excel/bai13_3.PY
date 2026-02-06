import sys
import json
input_data = sys.argv[1]
output_data = "output.json"
with open(input_data, "r", encoding = "utf-8") as f: 
    data = json.load(f)
total = data["price"] * data["quantity"]
result = {"Total": total}
with open(output_data, "w", encoding= "utf-8") as f:
    json.dump(result, f, indent=2)
print("Total: ", total)
