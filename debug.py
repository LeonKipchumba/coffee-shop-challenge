from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Customers create orders
alice.create_order(latte, 4.5)
alice.create_order(espresso, 5.0)
bob.create_order(latte, 3.5)
bob.create_order(latte, 6.0)

# Print orders for Alice
print("Alice's Orders:")
for order in alice.orders():
    print(f"  {order.coffee.name} - ${order.price}")

# Print unique coffees ordered by Alice
print("Coffees ordered by Alice:", [coffee.name for coffee in alice.coffees()])

# Print all customers who ordered Latte
print("Customers who ordered Latte:", [customer.name for customer in latte.customers()])

# Print total number of orders for Latte
print("Latte Order Count:", latte.num_orders())

# Print average price for Latte
print("Latte Average Price:", latte.average_price())

# Debug total orders stored
print("All Orders:")
for o in Order.all_orders:
    print(f"{o.customer.name} ordered {o.coffee.name} for ${o.price}")
