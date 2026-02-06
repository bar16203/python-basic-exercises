import json 

data = [
    {"id": 1,
     "name": "Laptop",
     "price": 15000000, 
     "stock": 10},
     {
         "id": 2,
         "name": "Mouse", 
         "price": 300000,
         "stock": 50
     },
     {
         "id": 3,
         "name": "Notebook",
         "price": 20000,
         "stock": 100
     }
]

#11.1 Tìm sản phẩm có name = "Laptop"
name_find = "Laptop"
for dt in data:
    if dt["name"].lower() == name_find.lower():
        print(dt)
        break

#11.2 Lọc tất cả sản phẩm có stock >= 50
stockGreaterThan_50 = [dt for dt in data if dt["stock"] >= 50]
print(stockGreaterThan_50)

#11.3 Cập nhật price = 500000 cho sản phẩm có id = 2
for dt in data:
    if dt["id"] ==2:
        dt["price"] = 500000
print(data)

#11.4 Xóa sản phẩm có price < 50000
data = [dt for dt in data if dt["price"] >= 50000]
print(data)

#11.5 Kiểm tra id = 5 có tồn tại hay không
exists = False
for dt in data:
    if dt["id"] == 5:
        exists = True
        break
print(exists)

#11.6 thêm sản phẩm mới nhưng Không trùng id price > 0 và stock >=0
new_product = {"id": 4, "name": "keybroad", "price": 900000, "stock": 2}
check_data = False
if new_product["price"] <= 0 or new_product["stock"] < 0:
    check_data = True
for dt in data: 
    if dt["id"] == new_product["id"]:
        check_data = True
        break
if check_data: 
    print("The data value is incorrect, please check again.")
else: 
    data.append(new_product)
    print(data)

#11.7 Tính tổng số lượng sản phẩm có trong kho
total = 0
for dt in data:
    total += dt["stock"]
print(total)

# Ghi dữ liệu vào file Json
with open("products.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent  =4, ensure_ascii = False)