import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_customer_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")  # Too short
        with self.assertRaises(ValueError):
            Customer("A" * 16)  # Too long
        with self.assertRaises(TypeError):
            Customer(123)

        c = Customer("Alice")
        self.assertEqual(c.name, "Alice")

        c.name = "Bob"
        self.assertEqual(c.name, "Bob")

        with self.assertRaises(ValueError):
            c.name = "A" * 20

    def test_orders_and_coffees(self):
        c = Customer("Jane")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Espresso")
        c.create_order(coffee1, 5.0)
        c.create_order(coffee2, 6.5)
        c.create_order(coffee1, 4.5)

        self.assertEqual(len(c.orders()), 3)
        self.assertEqual(set(c.coffees()), {coffee1, coffee2})

if __name__ == '__main__':
    unittest.main()
