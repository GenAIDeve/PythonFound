"""This module represent food item
"""


class Fooditem:
    def __init__(self, id,name,price,category):
        self.id=id
        self.name
        self.price=price
        self.category=category

    def __str__(self):
        return f"{self.name},{self.price},{self.category}"
class menu:    
    def __init__(self):
        self.items = []

    def add_item(self , food_item):
        self.items.append(food_item) 
        """THis item add food item
        Args:
            food_item (str): item name

        """ 
        self.items.append(food_item) 


    def get_all_items(self):
        """Get all items of menu
        """
        for item in self.items:
            print(item)


            