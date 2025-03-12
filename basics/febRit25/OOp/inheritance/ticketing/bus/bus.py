"""
This module will have information about bus types that atre used for booking 

    """
from ticketing.base.bookable import Bookable
class Bus(Bookable):
    """
    This represents a bus during tickets booking
    """

    def __init__(self , Operator, name, registration_number,category):
        """
        This is initializer for the bus
        Args: 
         operator (str): bus operator like APSRTC, TSRTC(buses),orange 
         name(str): vehicle number
         registratio_number(str): registration number
        """
    self.operator =Operator
    self.name= name
    self.registration_number=registration_number
    self.seats=dict()

    def set_seats(self,rows,columns):
        """
        This creates the default seat structure
        Args:
        count (_type_):_description_
        rows (_type_):_description_
        columns (_type_):_description_
       """
        for row_index in range (1,rows+1):
            for col_index in range(1, columns+1):
                self.seat(  #dictionary has method-> update will insert specified item in dictionary
                    id=f"{row_index}_{col_index}"
                )
                self.seats.update({seat.get_seat_number,seat})
    
    def book_ticket(self,seat_number, price): 
        """
        _summary_
        Args:
            seat_number (_type_):_description_
            price(_type_):_description_

        """
        self.seats.get(seat_number).book()

    