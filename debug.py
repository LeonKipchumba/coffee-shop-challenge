from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
leon = Customer("Leon")
kevo = Customer("Kevo")

# Create coffee types
latte = Coffee("Latte")
mocha = Coffee("Mocha")

# Create some orders
leon.create_order(latte, 4.5)
leon.create_order(mocha, 5.5)
kevo.create_order(latte, 6.0)

# Output expected behavior
print(leon.orders())                 # [Order(customer=Leon, coffee=Latte, price=4.5), Order(customer=Leon, coffee=Mocha, price=5.5)]
print(leon.coffees())                # [Coffee('Latte'), Coffee('Mocha')]
print(latte.customers())            # [Customer('Leon'), Customer('Kevo')]
print(latte.average_price())        # 5.25
print(Customer.most_aficionado(latte).name)  # Leon
