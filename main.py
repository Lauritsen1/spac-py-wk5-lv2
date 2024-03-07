import os

from db import Connection
from product_factory import ProductFactory
from inventory import Inventory

def main():
    db = Connection('localhost', 'root', 'password')

    inventory = Inventory()
    product_factory = ProductFactory()

    product1 = product_factory.create_product('Laptop', 'Thinkpad', 3000)
    inventory.add_product(product1)
    product2 = product_factory.create_product('Laptop', 'Macbook', 10000)
    inventory.add_product(product2)
    product3 = product_factory.create_product('TV', 'Samsung 75 4K QLED', 15000)
    inventory.add_product(product3)

    while True:
        print("\nMain Menu:")
        print("1. Create Product")
        print("2. View Products")
        print("3. Close")

        selection = int(input("Enter your selection: "))

        if selection == 1:
            print("\nCreate Product:")
            for _type in product_factory.product_types.keys():
                print(_type)
            product_type = input("Enter product type: ")
            product_name = input("Enter product name: ")
            product_price = float(input("Enter product price: "))
            product = product_factory.create_product(product_type, product_name, product_price)
            inventory.add_product(product)
            print(f"Product '{product_name}' of type '{product_type}' with price {product_price} created.")
        elif selection == 2:
            print("\nView Products:")
            inventory.display_all()
        elif selection == 3:
            print("\nClosing the system...")
            break
        else:
            print("\nInvalid selection. Please enter a number between 1 and 3.")


if __name__ == '__main__':
    main()