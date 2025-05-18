import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_customer_name(self):
        c = Customer("Alex")
        self.assertEqual(c.name, "Alex")
        with self.assertRaises(ValueError):
            Customer("")

    def test_customer_orders_and_coffees(self):
        c = Customer("Liam")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Mocha")
        c.create_order(coffee1, 3.5)
        c.create_order(coffee2, 4.5)
        self.assertEqual(len(c.orders()), 2)
        self.assertIn(coffee1, c.coffees())
        self.assertIn(coffee2, c.coffees())
