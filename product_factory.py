from inspect import getmembers, isclass, isabstract
import products

class ProductFactory:
    product_types = {}

    def __init__(self):
        self.load_products()

    def load_products(self) -> None:
        members = getmembers(products, lambda m: isclass(m) and not isabstract(m))
        for name, _type in members:
            if isclass(_type) and issubclass(_type, products.Product):
                self.product_types[name] = _type

    def create_product(self, name, category, price, *args, **kwargs) -> products.Product:
        if category in self.product_types:
            return self.product_types[category](name, category, price, *args, **kwargs)
        else:
            raise ValueError(f"Invalid product type: {category}")