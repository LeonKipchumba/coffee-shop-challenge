import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def test_coffee_name(self):
        c = Coffee("Espresso")
        self.assertEqual(c.name, "Espresso")
        with self.assertRaises(ValueError):
            Coffee("Jo")

    def test_coffee_orders_and_customers(self):
        coffee = Coffee("Cappuccino")
        customer1 = Customer("Alex")
        customer2 = Customer("Sam")
        Order(customer1, coffee, 5.0)
        Order(customer2, coffee, 6.0)
        self.assertEqual(coffee.num_orders(), 2)
        self.assertIn(customer1, coffee.customers())
        self.assertGreater(coffee.average_price(), 0)
