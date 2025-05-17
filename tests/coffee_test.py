import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def test_create_coffee(self):
        coffee = Coffee("Latte")
        self.assertEqual(coffee.name, "Latte")
        with self.assertRaises(ValueError):
            Coffee("Hi")  # Too short

    def test_num_orders_and_average_price(self):
        coffee = Coffee("Espresso")
        customer1 = Customer("John")
        customer2 = Customer("Jane")
        customer1.create_order(coffee, 4.0)
        customer2.create_order(coffee, 6.0)

        self.assertEqual(coffee.num_orders(), 2)
        self.assertAlmostEqual(coffee.average_price(), 5.0)

    def test_customers_unique(self):
        coffee = Coffee("Cappuccino")
        customer = Customer("Chris")
        customer.create_order(coffee, 5.0)
        customer.create_order(coffee, 5.5)

        self.assertEqual(len(coffee.customers()), 1)
        self.assertIn(customer, coffee.customers())

if __name__ == '__main__':
    unittest.main()
