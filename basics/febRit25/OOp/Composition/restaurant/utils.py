"""This class represents address related classes
"""

class Address:
    def __init__(self, roadno, street, area, pincode, city):
        self.roadno=roadno
        self.steeet=street
        self.area=area
        self.pincode=pincode
        self.city=city
    def __str__(self):
        return f"{self.roadno},{self.street},{self.area},{self.pincode},{self.city}"
    
            