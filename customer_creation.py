'''
Creating new customers class
'''


from db_controller import Database
from customer import Customer


class CustomerController:
    '''
    Customer Controller Class
    '''

    customers = []
    customers_database = None
    TABLE_NAME = 'customers'

    def __init__(self, db_controller: Database):
        self.customers_database = db_controller

    def create_customer(self, customer_name: str) -> bool | Customer:
        '''
        Method for creating a new customer
        '''
        search_result = self.customers_database.find_by(
            self.TABLE_NAME, 'name', customer_name)

        if (search_result and
                search_result['name'] == customer_name):
            return False

        customer = Customer(name=customer_name)

        if self.customers_database.create(customer, self.TABLE_NAME):
            return customer

        return False

    def update_customer(self) -> bool:
        '''
        Updates a customer
        '''
        return self.customers_database.update(self.TABLE_NAME)

    def delete_customer(self, customer: Customer) -> bool:
        '''
        Deletes a customer
        '''
        return self.customers_database.delete(customer, self.TABLE_NAME)

    def hydrate(self, data: dict) -> Customer:
        '''
        Hydrates an object with data
        obtained from database
        '''
        return Customer(customer_id=data['id'],
                        name=data['customer_name'])

    def display_customer_info(self, customer: Customer) -> str:
        '''
        Displays a customer information
        '''
        return f'\nCustomer Id: {customer.get_id()}' \
            f'\nCustomer Name: {customer.get_name()}'

    # pragma: no cover
    def drop_table(self) -> True:
        '''
        Drops customer table from db
        '''
        return self.customers_database.drop_table(self.TABLE_NAME)
