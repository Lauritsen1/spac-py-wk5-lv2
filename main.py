from abc import ABC, abstractmethod
import uuid
from datetime import datetime
from db import Connection
from tabulate import tabulate

class Product(ABC):
    def __init__(self, name: str, price: float):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return self.name
    
    def display_info(self) -> str:
        data = [
            ['id', self.id], 
            ['name', self.name], 
            ['price', self.price], 
            ['created_at', self.created_at.strftime('%Y-%m-%d %H:%M')]]
        table = tabulate(data, tablefmt='simple_grid')
        return table

class TShirt(Product):
    pass

class Hoodie(Product):
    pass

class Hat(Product):
    pass

class ProductFactory:
    def create_product(self, product_type, name, price):
        if product_type == "tshirt":
            return TShirt(name, price)
        elif product_type == "hoodie":
            return Hoodie(name, price)
        elif product_type == "hat":
            return Hat(name, price)
        else:
            raise ValueError(f"Error: Product type {product_type} not found.")

class InventoryManager:
    def __init__(self):
        self.product_factory = ProductFactory()

    def create_product(self, product_type, name, price):
        return self.product_factory.create_product(product_type, name, price)

def main():
    manager = InventoryManager()

    db = Connection(host='localhost', user='root', password='password')

    product1 = manager.create_product("tshirt", "T-shirt", 19.99)
    product2 = manager.create_product("hoodie", "Hoodie", 39.99)
    product3 = manager.create_product("hat", "Hat", 9.99)

    print(product1.display_info())
    print(product2.display_info())
    print(product3.display_info())

if __name__ == '__main__':
    main()