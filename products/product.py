from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name: str, price: int):
        self.id = None
        self.created_at = None
        self.name = name
        self.price = price

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def display_info(self) -> None:
        raise NotImplementedError