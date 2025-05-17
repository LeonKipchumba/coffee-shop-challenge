import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    def test_valid_order(self):
        customer = Customer("Alice")
        coffee = Coffee("Mocha")
        order = Order(customer, coffee, 7.0)

        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 7.0)

    def test_invalid_order_price(self):
        customer = Customer("Bob")
        coffee = Coffee("Americano")
        with self.assertRaises(ValueError):
            Order(customer, coffee, 11.0)  # Above max

        with self.assertRaises(ValueError):
            Order(customer, coffee, 0.5)  # Below min

    def test_type_checks(self):
        coffee = Coffee("Flat White")
        with self.assertRaises(TypeError):
            Order("not-a-customer", coffee, 3.0)

        customer = Customer("Greg")
        with self.assertRaises(TypeError):
            Order(customer, "not-a-coffee", 3.0)

if __name__ == '__main__':
    unittest.main()
