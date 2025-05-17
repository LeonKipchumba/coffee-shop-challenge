import unittest
from customer import Customer
from coffee import Coffee

class TestCoffee(unittest.TestCase):
    def test_valid_name(self):
        c = Coffee("Latte")
        self.assertEqual(c.name, "Latte")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Coffee("A")
        with self.assertRaises(TypeError):
            Coffee(123)

    def test_num_orders_and_average(self):
        cust = Customer("Amy")
        latte = Coffee("Latte")
        cust.create_order(latte, 5.0)
        cust.create_order(latte, 3.0)
        self.assertEqual(latte.num_orders(), 2)
        self.assertEqual(latte.average_price(), 4.0)

if __name__ == '__main__':
    unittest.main()
