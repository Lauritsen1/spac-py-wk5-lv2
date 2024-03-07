from db import Connection

from pick import pick

from product_factory import ProductFactory

def main():
    db = Connection('localhost', 'root', 'password')

    inventory = ProductFactory()

    title = 'Main Menu'
    options = ['Create Product', 'View Products', 'Close']
    option, index = pick(options, title, indicator='>')

    if index == 0:
        title = 'Select product to create'
        options = list(inventory.product_types.keys())
        option, index = pick(options, title, indicator='>')

        if option in inventory.product_types.keys():
            title = f'Create Product: {option}'
            print(title)
            name = input('Name: ')
            price = input('Price: ')
            product = inventory.create_product(option, name, price)
            product.display_info()

    elif index == 1:
        title = option
        options = ['All', 'Search', *inventory.product_types.keys()]
        option, index = pick(options, title, indicator='>')
    
    if index == 2:
        return


if __name__ == '__main__':
    main()