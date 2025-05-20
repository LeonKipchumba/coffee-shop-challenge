import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    def test_order_initialization_and_validation(self):
        c = Customer("Jane")
        coffee = Coffee("Latte")

        with self.assertRaises(ValueError):
            Order(c, coffee, 0.5)

        with self.assertRaises(TypeError):
            Order("NotCustomer", coffee, 3.0)

        order = Order(c, coffee, 4.0)
        self
