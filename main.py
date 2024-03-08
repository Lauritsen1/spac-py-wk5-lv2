from db import Connection
from product_factory import ProductFactory
from inventory import Inventory

items = [
        {'type': 'Laptop', 'name': 'Lenovo Thinkpad', 'price': 3000},
        {'type': 'Laptop', 'name': 'Macbook Pro', 'price': 15000},
        {'type': 'TV', 'name': 'Samsung 75 4K QLED', 'price': 13000},
        {'type': 'TV', 'name': 'LG 65 LED', 'price': 5000},
        {'type': 'Phone', 'name': 'iPhone 12', 'price': 7000},
        {'type': 'Phone', 'name': 'Samsung Galaxy S21', 'price': 8000},
    ]

def main():
    db = Connection('localhost', 'root', '1234')

    inventory = Inventory()
    product_factory = ProductFactory()

    for item in items:
        product = product_factory.create_product(item['type'], item['name'], item['price'])
        inventory.add_product(product)

    inventory.display_all()


if __name__ == '__main__':
    main()