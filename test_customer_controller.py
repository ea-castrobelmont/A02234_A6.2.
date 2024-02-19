'''
Test suite for customers
'''

import unittest
import json
import os
from customer_creation import CustomerController
from db_controller import Database
from customer import Customer
from definitions import ROOT_DIR


def file_exists(directory, filename):
    '''
    Method for asserting if a file exists
    '''
    file_path = os.path.join(directory, filename)
    return os.path.exists(file_path)


class TestCustomerController (unittest.TestCase):

    '''
    Class for testing customer methods
    '''

    database_controller = None
    controller = None

    folder_path = os.path.join(ROOT_DIR, 'db')
    file_path = os.path.join(folder_path, 'customers.json')

    def setUp(self):
        '''
        Set up the test
        '''
        self.database_controller = Database()
        self.controller = CustomerController(
            db_controller=self.database_controller
        )

    def test_create_customer(self):
        '''
        test if the create method correctly creates a new customer
        '''
        customer_name = 'Estefania Castro'
        customer = self.controller.create_customer(customer_name)
        customer_data = {}

        with open(self.file_path, mode='r', encoding='utf8') as file:
            customer_data = json.load(file)

        self.assertIsInstance(customer, Customer)
        self.assertEqual(customer.get_id(), 1)
        self.assertListEqual(customer_data, [{'name': customer_name, 'id': 1}])

    def test_it_does_not_create_same_customer_twice(self):
        '''
        Test same hotel is not created twice
        '''
        # 1. Arrange
        customer_name = 'Estefania CVastro'
        self.controller.create_customer(customer_name)

        # 2. Act
        result = self.controller.create_customer(customer_name)

        # 3. Assert

        self.assertFalse(result)

    def test_delete_customer1(self):
        '''
        Test the delete customer method
        '''
        # 1. Arrange
        customer = self.controller.create_customer('Estefania Castro')
        # Let's confirm that our db is not empty
        with open(self.file_path, mode='r', encoding='utf8') as file:
            customer_data = json.load(file)
            self.assertEqual(1, len(customer_data))

        # 2. Act
        result = self.controller.delete_customer(customer)

        # 3. Assert
        self.assertTrue(result)

        with open(self.file_path, mode='r', encoding='utf8') as file:
            customer_data = json.load(file)
            self.assertEqual(0, len(customer_data))

    def test_it_modifies_a_customer(self):
        '''
        Test if modified customer info is stored to db
        '''
        # 1. Arrange

        customer_name = 'Abigail'
        new_name = 'Belmont'
        customer = self.controller.create_customer(customer_name)
        customer.set_name(new_name)

        # 2. Act
        result = self.controller.update_customer()

        with open(self.file_path, mode='r', encoding='utf8') as file:
            customer_data = json.load(file)

        # 3. Assert

        self.assertTrue(result)
        self.assertEqual(new_name, customer_data[0]['name'])

    def test_it_displays_customer_info_correctly(self):
        '''
        Test if customer info is displayed correctly
        '''
        # Arrange
        customer = Customer(1, 'Abigail')

        expected = f'\nCustomer Id: {customer.get_id()}' \
            f'\nCustomer Name: {customer.get_name()}'

        # Act
        result = self.controller.display_customer_info(customer)

        # Assert
        self.assertEqual(expected, result)

    def test_it_displays_customer_info_correctly(self):
        '''
        Test if customer info is displayed correctly
        '''
        # Arrange
        customer = Customer(1, 'Abigail')

        # Modificar el nombre del cliente para que contenga un símbolo
        customer.set_name('Abigail*')

        expected = f'\nCustomer Id: {customer.get_id()}' \
            f'\nCustomer Name: {customer.get_name()}'

        # Act
        result = self.controller.display_customer_info(customer)

        # Assert
        self.assertEqual(expected, result)


    def tearDown(self):
        '''
        Clean up database
        '''
        self.controller.drop_table()


if __name__ == '__main__':
    unittest.main()
