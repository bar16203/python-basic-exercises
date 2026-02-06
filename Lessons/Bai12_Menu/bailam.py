import json

def load_data():
    with open("products.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data): 
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def show_products(data):
    for p in data: 
        print(f"ID: {p['id']} | {p['name']} | Price: {p['price']} | Stock: {p['stock']}")

def add_products(data): 
    new_id = int(input("Enter ID: "))
    name = input("Enter name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock: "))
    if price <= 0 or stock < 0:
        print("Invaled Proce or Stock")
        return

    for p in data: 
        if p["id"] == new_id:
            print("ID already exists")
            return
    data.append(
        {
        "id": new_id, 
        "name": name, 
        "price": price, 
        "stock": stock
        }
    )
    save_data(data)
    print("Product added successfully")

def delete_product(data):
    delete_id = int(input("Enter ID to delete: "))
    new_data = [p for p in data if p["id"] != delete_id]
    if len(new_data) == len(data):
        print("ID not found")
    else: 
        save_data(new_data)
        print("Deleted successfully")

def update_price(data):
    update_id = int(input("Enter ID to update: "))
    for p in data: 
        if p["id"] == update_id:
            new_price = float(input("Enter new price: "))
            if new_price <= 0:
                print("Invalid price")
                return
            p["price"] = new_price
            save_data(data)
            print("Update successfully")
            return
    print("ID not found")

def found_product(data):
    found_name = input("Enter the name you are looking for: ").strip().lower()
    for p in data: 
        if p["name"].strip().lower() == found_name:
            print(f"ID: {p['id']} | {p['name']} | Price: {p['price']} | Stock: {p['stock']}")
            return
    print("Name not found")

def increase_product(data):
    X = int(input("Enter X: "))
    for p in data: 
        p['price'] += p['price']*X/100
    save_data(data)
    print("Price increase successfully")

def menu(): 
    print("\n==== PRODUCT MANAGEMENT ====")
    print("1. Show products")
    print("2. Add product")
    print("3. Delete product")
    print("4. Update product price")
    print("5. Seach by name")
    print("6. Price increase X%")
    print("0. Exit")

while True:
    data = load_data()
    menu()
    choice = int(input("Choice: "))

    if choice == 1:
        show_products(data)
    elif choice == 2: 
        add_products(data)
    elif choice == 3:
        delete_product(data)
    elif choice == 4:
        update_price(data)
    elif choice == 5:
        found_product(data)
    elif choice == 6:
        increase_product(data)
    elif choice == 0:
        print("Bye!")
        break
    else: 
        print("Invalid choice")