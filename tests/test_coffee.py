import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def test_coffee_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("A")
        with self.assertRaises(TypeError):
            Coffee(123)

        c = Coffee("Mocha")
        self.assertEqual(c.name, "Mocha")
        with self.assertRaises(AttributeError):
            c.name = "Latte"  # Immutable

    def test_orders_and_customers(self):
        coffee = Coffee("Americano")
        c1 = Customer("Alice")
        c2 = Customer("Bob")
        c1.create_order(coffee, 4.0)
        c2.create_order(coffee, 5.0)

        self.assertEqual(len(coffee.orders()), 2)
        self.assertEqual(set(coffee.customers()), {c1, c2})

    def test_aggregate_methods(self):
        coffee = Coffee("Cappuccino")
        self.assertEqual(coffee.num_orders(), 0)
        self.assertEqual(coffee.average_price(), 0)

        c = Customer("Tester")
        c.create_order(coffee, 5.0)
        c.create_order(coffee, 7.0)

        self.assertEqual(coffee.num_orders(), 2)
        self.assertEqual(coffee.average_price(), 6.0)

if __name__ == '__main__':
    unittest.main()
