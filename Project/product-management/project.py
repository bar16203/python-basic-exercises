numberOfProduct = int(input("Enter number of product: "))
products = []
total = 0
for i in range(numberOfProduct):
    product = {}
    product["name"] = input("Enter product name: ")
    product["price"] = float(input("Enter product price: "))
    product["quantity"] = int(input("Enter product quantity: "))
    products.append(product)
maxprice = products[0]["price"]
for pd in products:
    print(pd["name"],"-",pd["price"],"-",pd["quantity"])
    total += (pd["price"] * pd["quantity"])
    if maxprice < pd["price"]:
        maxprice = pd["price"]
print("Total inventory value: ", total)
print("Most expensive: ", maxprice)
print("Products with quantity greater than 2:")
for pd in products:
    if pd["quantity"] > 2:
        print(pd["name"])