from datetime import datetime
from uuid import uuid4

from tabulate import tabulate

from .product import Product

class TV(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)
        self.id = uuid4()
        self.created_at = datetime.now()
    
    def __str__(self) -> str:
        return self.name
    
    def display_info(self) -> None:
        data = [
            ['id', self.id], 
            ['name', self.name], 
            ['price', self.price], 
            ['created_at', self.created_at.strftime('%Y-%m-%d %H:%M')]]
        table = tabulate(data, tablefmt='simple_grid')
        print(table)