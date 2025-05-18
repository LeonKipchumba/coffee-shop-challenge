from order import Order

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string with 1 to 15 characters.")

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        customers = {}
        for order in Order.all:
            if order.coffee == coffee:
                customers[order.customer] = customers.get(order.customer, 0) + order.price
        return max(customers, key=customers.get) if customers else None
