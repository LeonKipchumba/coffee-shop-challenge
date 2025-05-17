import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def test_valid_order(self):
        c = Customer("Jane")
        coffee = Coffee("Cappuccino")
        o = Order(c, coffee, 5.0)
        self.assertEqual(o.customer, c)
        self.assertEqual(o.coffee, coffee)
        self.assertEqual(o.price, 5.0)

    def test_invalid_price(self):
        c = Customer("Jane")
        coffee = Coffee("Espresso")
        with self.assertRaises(ValueError):
            Order(c, coffee, 0.5)
        with self.assertRaises(ValueError):
            Order(c, coffee, 11.0)
        with self.assertRaises(TypeError):
            Order(c, coffee, "five")

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            Order("not_a_customer", Coffee("Mocha"), 5.0)
        with self.assertRaises(TypeError):
            Order(Customer("Joe"), "not_a_coffee", 5.0)

if __name__ == '__main__':
    unittest.main()
