import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def test_valid_name(self):
        c = Customer("Alice")
        self.assertEqual(c.name, "Alice")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Customer("")  # too short
        with self.assertRaises(ValueError):
            Customer("A" * 20)  # too long
        with self.assertRaises(TypeError):
            Customer(123)  # not a string

    def test_create_order(self):
        c = Customer("Bob")
        coffee = Coffee("Latte")
        order = c.create_order(coffee, 4.0)
        self.assertIn(order, c.orders())
        self.assertIn(coffee, c.coffees())

    def test_unique_coffees(self):
        c = Customer("Tom")
        latte = Coffee("Latte")
        espresso = Coffee("Espresso")
        c.create_order(latte, 3.0)
        c.create_order(latte, 3.5)
        c.create_order(espresso, 4.0)
        self.assertEqual(len(c.coffees()), 2)

if __name__ == '__main__':
    unittest.main()
