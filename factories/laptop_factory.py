from .factory import Factory
from products.laptop import Laptop

class LaptopFactory(Factory):
    def create_product(self, name: str, price: float) -> Laptop:
        return Laptop(name, price)