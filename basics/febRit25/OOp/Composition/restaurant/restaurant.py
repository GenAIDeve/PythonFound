"""This module will have restaurant related classes

"""
from restaurant.food import menu, Fooditem
class Restaurant:
    """ 
    THis represents the restaurant
    """
    def __init__(self, name):
        """
        initial
        Args:
            name(str):name

        """
        self.name=name
        self.address=none # none has no vlaue no located memory
        self.menu = menu()
        self.menu.add_item( Fooditem(1,"pasta",250,"specials"))
        self.update_address(self,address):
    

    def update_address(self, address):
        """update the address
        Args:
            address (str): address_details
        """
        self.address=address
    def add_food_items(self ,* item):
        """Add food
        Args:item (str): fooditem

        """
        for item in items:

            self.menu.add_item(item)
        


        