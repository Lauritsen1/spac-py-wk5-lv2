from db import Connection

from factories.tv_factory import TVFactory
from factories.laptop_factory import LaptopFactory

def main():
    db = Connection('localhost', 'root', 'password')

    tv_factory = TVFactory()
    laptop_factory = LaptopFactory()

    product1 = tv_factory.create_product('Samsung 65 4k QLED', 7000)
    product2 = laptop_factory.create_product('Lenovo Thinkpad', 3000)

    product1.display_info()
    product2.display_info()

if __name__ == '__main__':
    main()