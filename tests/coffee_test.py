import pytest
from coffee_shop_challenge.coffee import Coffee
from coffee_shop_challenge.customer import Customer
from coffee_shop_challenge.order import Order

def test_coffee_name_valid():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_name_invalid():
    with pytest.raises(ValueError):
        Coffee("ab")  # Too short
    with pytest.raises(ValueError):
        Coffee(123)  # Wrong type

def test_coffee_immutable_name():
    coffee = Coffee("Latte")
    with pytest.raises(AttributeError):
        coffee.name = "Espresso"

def test_coffee_orders():
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    order = Order(customer, coffee, 5.0)
    assert coffee.orders() == [order]

def test_coffee_customers():
    coffee = Coffee("Latte")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    Order(customer1, coffee, 5.0)
    Order(customer2, coffee, 4.0)
    assert set(coffee.customers()) == {customer1, customer2}

def test_num_orders():
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    Order(customer, coffee, 5.0)
    Order(customer, coffee, 4.0)
    assert coffee.num_orders() == 2

def test_average_price():
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    Order(customer, coffee, 5.0)
    Order(customer, coffee, 3.0)
    assert coffee.average_price() == 4.0