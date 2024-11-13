# main.py
from auth import User
from inventory import Product, Inventory

def main():
    inventory = Inventory()
    print("Welcome to Inventory Management System (IMS)")

    # User Authentication
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = User(username, password)

    if not user.role:
        print("Invalid credentials. Exiting...")
        return

    print(f"Login successful! Role: {user.get_role()}\n")

    while True:
        print("1. Add Product (Admin only)")
        print("2. View Products")
        print("3. Search Products")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1" and user.is_admin():
            product_id = input("Product ID: ")
            name = input("Product Name: ")
            category = input("Category: ")
            price = float(input("Price: "))
            stock_quantity = int(input("Stock Quantity: "))
            product = Product(product_id, name, category, price, stock_quantity)
            inventory.add_product(product)

        elif choice == "2":
            products = inventory.view_all_products()
            for product in products:
                print(product)

        elif choice == "3":
            name = input("Search by Name (leave blank to skip): ")
            category = input("Search by Category (leave blank to skip): ")
            results = inventory.search_product(name=name, category=category)
            for result in results:
                print(result)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option or insufficient permissions.")

if __name__ == "__main__":
    main()
