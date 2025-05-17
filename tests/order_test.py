import pytest
from ..order import Order
from ..customer import Customer
from ..coffee import Coffee

def test_order_valid():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_invalid_customer():
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order("Alice", coffee, 5.0)

def test_order_invalid_coffee():
    customer = Customer("Alice")
    with pytest.raises(ValueError):
        Order(customer, "Latte", 5.0)

def test_order_invalid_price():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  # Too low
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)  # Too high
    with pytest.raises(ValueError):
        Order(customer, coffee, "5.0")  # Wrong type

def test_price_immutable():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    with pytest.raises(AttributeError):
        order.price = 6.0