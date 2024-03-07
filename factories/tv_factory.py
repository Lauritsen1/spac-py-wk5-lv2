from .factory import Factory
from products.tv import TV

class TVFactory(Factory):
    def create_product(self, name: str, price: float) -> TV:
        return TV(name, price)