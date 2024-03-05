from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name: str, price: float, currency: str):
        self.name = name
        self.price = price
        self.currency = currency # New property

    @abstractmethod
    def get_name(self) -> str:
         pass
    
    @abstractmethod
    def get_price(self) -> float:
        pass

class Factory(ABC):
    @abstractmethod
    def create_product(self):
        pass

class Electronic(Product):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.warranty: str = '2 Years'

    def __str__(self) -> str:
        return self.name

    def get_name(self) -> str:
        return self.name
    
    def get_price(self) -> float:
        return self.price
    
    def get_warranty(self) -> str:
        return self.warranty
    
class Clothing(Product):
    def __init__(self, size: str, **kwargs):
        super().__init__(**kwargs)
        self.size: str = size

    def __str__(self) -> str:
        return self.name

    def get_name(self) -> str:
        return self.name
    
    def get_price(self) -> float:
        return f'{self.price} Kr'
    
    def get_size(self) -> str:
        return self.size
    
class ElectronicFactory(Factory):
    def create_product(self, name: str, price: float) -> Electronic:
        return Electronic(name, price)

class ClothingFactory(Factory):
    def create_product(self, name: str, price: float, size: str) -> Clothing:
        return Clothing(name, price, size)

def main():
    electronic_factory = ElectronicFactory()
    clothing_factory = ClothingFactory()

    product1 = electronic_factory.create_product('TV', 4000)
    product2 = clothing_factory.create_product('T-Shirt', 99.99, 'M')

    print('--------------------')
    print(product1.get_name())
    print(product1.get_price())
    print(product1.get_warranty())
    print('--------------------')
    print(product2.get_name())
    print(product2.get_price())
    print(product2.get_size())
    print('--------------------')


if __name__ == '__main__':
    main()