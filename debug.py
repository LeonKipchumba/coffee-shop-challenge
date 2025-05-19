from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
c1 = Customer("Alice")
c2 = Customer("Bob")

# Create coffee types
latte = Coffee("Latte")
mocha = Coffee("Mocha")

# Create some orders
c1.create_order(latte, 4.5)
c1.create_order(mocha, 5.5)
c2.create_order(latte, 6.0)

# Output expected behavior
print(c1.orders())                 # [Order(customer=Alice, coffee=Latte, price=4.5), Order(customer=Alice, coffee=Mocha, price=5.5)]
print(c1.coffees())                # [Coffee('Latte'), Coffee('Mocha')]
print(latte.customers())          # [Customer('Alice'), Customer('Bob')]
print(latte.average_price())      # 5.25
print(Customer.most_aficionado(latte).name)  # Alice
