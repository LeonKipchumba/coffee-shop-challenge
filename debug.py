from customer import Customer
from coffee import Coffee
from order import Order

# Create some customers and coffees
c1 = Customer("John")
c2 = Customer("Alice")
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

# Create some orders
o1 = c1.create_order(coffee1, 4.5)
o2 = c1.create_order(coffee2, 5.0)
o3 = c2.create_order(coffee1, 6.0)

# Inspect customer data
print(f"{c1.name} has ordered: {[coffee.name for coffee in c1.coffees()]}")
print(f"{coffee1.name} has {coffee1.num_orders()} orders")
print(f"Average price of {coffee1.name}: {coffee1.average_price():.2f}")

# Bonus: Most aficionado
aficionado = Customer.most_aficionado(coffee1)
print(f"Most aficionado for {coffee1.name}: {aficionado.name if aficionado else 'None'}")
