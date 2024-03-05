import uuid

class Product:
    def __init__(self, name: str, price: float):
        self.id = uuid.uuid4()
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return self.name
    
class ProductFactory:
    def create_product(self, name, price):
        return Product(name, price)

class Category:
    def __init__(self, name: str):
        self.id = uuid.uuid4()
        self.name = name
        self.product_factory = ProductFactory()

    def __str__(self) -> str:
        return self.name

    def create_product(self, name, price):
        return self.product_factory.create_product(name, price)


class CategoryFactory:
    def create_category(self, name):
        return Category(name)
    
    
class InventoryManager:
    def __init__(self):
        self.category_factory = CategoryFactory()
        self.categories = {}

    def register_category(self, category_name):
        self.categories[category_name] = self.category_factory.create_category(category_name)

    def create_product(self, category_name, name, price):
        category = self.categories.get(category_name)
        if category:
            return category.create_product(name, price)
        else:
            raise ValueError(f"Error: Category {category_name} not found.")

    
def main():
    manager = InventoryManager()

    # Registering categories
    manager.register_category("electronics")
    manager.register_category("clothing")
    manager.register_category("other_stuff")

    # Creating products
    product1 = manager.create_product("electronics", "Smartphone", 999.99)
    product2 = manager.create_product("clothing", "T-shirt", 19.99)
    product3 = manager.create_product("other_stuff", "Book", 9.99)

    # Displaying products
    print(product1)
    print(product2)
    print(product3)

if __name__ == '__main__':
    main()