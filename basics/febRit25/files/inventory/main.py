    """This module will be entry poinyt of the app

    """
from models.product import Product


inventory = dict(str,Product)
def add_product(product: Product)->None:
    inventory[product.id] = product


def add_item_to_inventory(product: Product)->None:





    """
    Purpose: 
    """
    
# end def
def create_inventory(add_item_to_inventory):
    while True:
        print("enter the item added to the inventory")
        id =input("Enter the number:  ")
        name = ("Enter the product name : ")
        price = float ("Enter the price: ")
        quantity = int("Enter the quantity: ")  
        product = Product(name, price, quantity, id)
        add_item_to_inventory(product)
        print("Do you want to add another item?")
        choice =input("Enter yes or no: ")

        if choice.lower() != 'yes':
            break
#-----------------------------------------------------
# just commenting for now this was the first step

#if__name__ == '__main__':
#    dell_keyboards = Product('Dell Keyboard', 20, 50, 1)
##except OutOfStockException as e:
   # print(f"the current stock available is {dell_keyboards.quantity}")
  #  print("sales not proceed")
# The code in inventory/store/__init__.py will not run because of the typo in the if statement. The correct code should be:
#print(dell_keyboards)
#--------------------------------------------------------

create_inventory(add_item_to_inventory)
  



def sell_item():
    id = input("Enter the id of the product:  ")
    quantity = int(input("Enter the item for sales:  "))
    Product = inventory[id]
    Product.sale(quantity)

 sell_item()
    print(inventory)

