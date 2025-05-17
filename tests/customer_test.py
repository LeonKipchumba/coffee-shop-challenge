import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_create_customer(self):
        customer = Customer("John")
        self.assertEqual(customer.name, "John")
        with self.assertRaises(ValueError):
            customer.name = "A" * 16  # Invalid name length

    def test_create_order(self):
        customer = Customer("John")
        coffee = Coffee("Espresso")
        order = customer.create_order(coffee, 5.0)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.0)

    def test_most_aficionado(self):
        coffee = Coffee("Latte")
        customer1 = Customer("John")
        customer2 = Customer("Alice")
        customer1.create_order(coffee, 3.0)
        customer2.create_order(coffee, 5.0)
        self.assertEqual(Customer.most_aficionado(coffee), customer2)

if __name__ == '__main__':
    unittest.main()
