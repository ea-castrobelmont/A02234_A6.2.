'''
Reservation Controller class
'''

from hotel import Hotel
from reservation import Reservation
from customer import Customer
from db_controller import Database


class ReservationController:
    '''
    Reservation Controller class
    '''

    reservations = []
    database_controller = None
    TABLE_NAME = 'reservations'

    # pragma: no cover
    def __init__(self, database_controller: Database) -> bool | Reservation:
        self.database_controller = database_controller

    def create_reservation(self, hotel: Hotel, customer: Customer):
        '''
        Creates a reservation
        '''

        reservation = Reservation(hotel=hotel, customer=customer)
        search_result = self.database_controller.find_by(
            self.TABLE_NAME, 'customer_id', customer.get_id())

        if (search_result and
                search_result['customer_id'] == customer.get_id()):
            return False

        if self.database_controller.create(reservation, self.TABLE_NAME):
            return reservation

        return False

    def cancel_reservation(self, reservation: Reservation):
        '''
        Cancels a reservation
        '''
        return self.database_controller.delete(reservation, self.TABLE_NAME)

    # pragma: no cover
    # Drop table already tested
    def drop_table(self) -> True:
        '''
        Drops reservations table from db
        '''
        return self.database_controller.drop_table(self.TABLE_NAME)
