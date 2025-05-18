import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    def test_order_attributes(self):
        customer = Customer("Jane")
        coffee = Coffee("Americano")
        order = Order(customer, coffee, 4.0)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 4.0)

        with self.assertRaises(ValueError):
            Order(customer, coffee, 0.5)
