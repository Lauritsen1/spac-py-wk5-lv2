from enum import Enum

from db import Connection
from product_factory import ProductFactory
from inventory import Inventory

class Category(Enum):
    TV = 'TV'
    LAPTOP = 'Laptop'
    PHONE = 'Phone'

items = [
        {'name': 'Lenovo Thinkpad', 'category': 'Laptop', 'price': 3000},
        {'name': 'Macbook Pro', 'category': 'Laptop', 'price': 15000},
        {'name': 'Samsung 75 4K QLED', 'category': 'TV', 'price': 13000},
        {'name': 'LG 65 LED', 'category': 'TV', 'price': 5000},
        {'name': 'iPhone 12', 'category': 'Phone', 'price': 7000},
        {'name': 'Samsung Galaxy S21', 'category': 'Phone',  'price': 8000},
    ]

def main():
    inventory = Inventory()
    product_factory = ProductFactory()

    with Connection() as cursor:
        for item in items:
            product = product_factory.create_product(item['name'], item['category'], item['price'])
            cursor.execute('INSERT INTO products(id, name, category, price, created_at) VALUES(?, ?, ?, ?, ?)', (str(product.id), product.name, product.category, product.price, product.created_at))
            inventory.add_product(product)

    inventory.display_all()

    # inventory.display_by_category(Category.TV.value)


if __name__ == '__main__':
    main()