from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
order1 = alice.create_order(latte, 5.0)
order2 = alice.create_order(espresso, 3.0)
order3 = bob.create_order(latte, 4.5)

# Test relationships and aggregates
print(f"Alice's orders: {len(alice.orders())}")  # Should be 2
print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")  # Should be ['Latte', 'Espresso']
print(f"Latte's customers: {[customer.name for customer in latte.customers()]}")  # Should be ['Alice', 'Bob']
print(f"Latte's number of orders: {latte.num_orders()}")  # Should be 2
print(f"Latte's average price: {latte.average_price()}")  # Should be 4.75
print(f"Most aficionado for Latte: {Customer.most_aficionado(latte).name}")  # Should be 'Alice'