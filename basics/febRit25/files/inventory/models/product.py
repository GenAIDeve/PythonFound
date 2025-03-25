class Product():
    def __init__(self, name, price,quantity,id):
        self.name = name
        self.price = price
        self.quantiy=0
        self.id=0

    @staticmethod
    def create(line):
        if line.stars_with(""):
        details = linesplit(',')
        return Product(details[0], float(details[1]), int(details[2]), int(details[3]))

    
    def  sale (self,count:int):
        """

        Args:
            count (int): _description_
            Raises:
                OutOfStockException: when the quantity is less than the count
        """

        if self.quantity < count:
            raise OutOfStockException("we dont have enough stock")
    
        self.quantity -= count
    def purchase(self, count:int):
        """Purchase

        Args:
            count (int): _description_
        """
        self.quantity += count

    def __str__(self):
        return f'{self.name}, {self.price}, {self.quantity},{self.id}'
class OutOfStockException(Exception):
    pass   