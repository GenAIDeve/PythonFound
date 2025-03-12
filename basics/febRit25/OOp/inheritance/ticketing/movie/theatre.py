from ticketing.base.bookable import Bookable
class Movietheatre(Bookable):

    """
       This class i can write any type of bookiin fliht, hotel, restaurant, movie
    Args: 
        Bookable (_type_):description

    """
    #overriding calling from parent class iheritance
    def book_ticket(self, seat_number, price):
        return super().book_ticket(seat_number, price)
    
