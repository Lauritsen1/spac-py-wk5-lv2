from tabulate import tabulate

from db import Connection
from products import Product

db = Connection()

class Inventory:
    def __init__(self):
        self.products: list[Product] = []
        self.load_products()

    def load_products(self) -> None:
        rows = db._cursor.execute('SELECT id, name, category, price, created_at FROM products').fetchall()
        for row in rows:
            product = Product(row[0], row[1], row[2], row[3], row[4])
            self.products.append(product)

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def display_all(self) -> None:
        data = []
        for product in self.products:
            data.append([product.id, product.name, product.category, product.price, product.created_at.strftime('%Y-%m-%d %H:%M')])
        table = tabulate(data, headers=['ID', 'Name', 'Category', 'Price', 'Created At'], tablefmt='simple_grid')
        print(table)

    def display_by_category(self, category: str) -> None:
        data = filter(lambda product: product.category == category, self.products)
        test = []
        for product in data:
            test.append([product.id, product.name, product.category, product.price, product.created_at.strftime('%Y-%m-%d %H:%M')])
        table = tabulate(test, headers=['ID', 'Name', 'Category', 'Price', 'Created At'], tablefmt='simple_grid')
        print(table)
