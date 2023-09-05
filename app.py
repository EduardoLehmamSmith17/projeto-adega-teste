class Product:
    def __init__(self, id, name, category, price, quantity):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

class ProductManager:
    def __init__(self):
        self.products = []
        self.current_id = 1

    def create_product(self, name, category, price, quantity):
        product = Product(self.current_id, name, category, price, quantity)
        self.products.append(product)
        self.current_id += 1
        return product

    def get_product(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None

    def update_product(self, id, name, category, price, quantity):
        product = self.get_product(id)
        if product:
            product.name = name
            product.category = category
            product.price = price
            product.quantity = quantity
            return product
        return None

    def delete_product(self, id):
        product = self.get_product(id)
        if product:
            self.products.remove(product)
            return True
        return False
