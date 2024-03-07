from tabulate import tabulate

from products import Product

class Inventory:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def display_all(self) -> None:
        data = []
        for product in self.products:
            data.append([product.id, product.name, product.price, product.created_at.strftime('%Y-%m-%d %H:%M')])
        table = tabulate(data, headers=['ID', 'Name', 'Price', 'Created At'], tablefmt='simple_grid')
        print(table)

    def display_by_type(self, product_type) -> None:
        data = [[product.id, product.name, product.price, product.created_at.strftime('%Y-%m-%d %H:%M')] for product in self.products if isinstance(product, product_type)]
        table = tabulate(data, headers=['ID', 'Name', 'Price', 'Created At'], tablefmt='simple_grid')
        print(table)