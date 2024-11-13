# inventory.py

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __repr__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock_quantity}"

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id not in self.products:
            self.products[product.product_id] = product
            print(f"Product {product.name} added successfully!")
        else:
            print("Product ID already exists!")

    def view_all_products(self):
        return list(self.products.values())

    def search_product(self, name=None, category=None):
        result = []
        for product in self.products.values():
            if (name and name.lower() in product.name.lower()) or (category and category.lower() in product.category.lower()):
                result.append(product)
        return result
