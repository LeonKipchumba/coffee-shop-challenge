class Customer:
    _all = []

    def __init__(self, name):
        self.name = name
        Customer._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order._all if order.customer == self]

    def coffees(self):
        from coffee import Coffee
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        from order import Order
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from coffee import Coffee
        from order import Order
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        customer_spending = {}
        for order in coffee.orders():
            if order.customer not in customer_spending:
                customer_spending[order.customer] = 0
            customer_spending[order.customer] += order.price
        if not customer_spending:
            return None
        return max(customer_spending, key=customer_spending.get)