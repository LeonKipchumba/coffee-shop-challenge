import pytest
from ..customer import Customer
from ..coffee import Coffee
from ..order import Order

def test_customer_name_valid():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_name_invalid_type():
    with pytest.raises(ValueError):
        Customer(123)

def test_customer_name_invalid_length():
    with pytest.raises(ValueError):
        Customer("")  # Too short
    with pytest.raises(ValueError):
        Customer("A" * 16)  # Too long

def test_customer_orders():
    customer = Customer("Bob")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert customer.orders() == [order]

def test_customer_coffees():
    customer = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    Order(customer, coffee1, 5.0)
    Order(customer, coffee2, 3.0)
    assert set(customer.coffees()) == {coffee1, coffee2}

def test_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 4.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.0

def test_most_aficionado():
    coffee = Coffee("Latte")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    Order(customer1, coffee, 5.0)
    Order(customer1, coffee, 3.0)
    Order(customer2, coffee, 4.0)
    assert Customer.most_aficionado(coffee) == customer1