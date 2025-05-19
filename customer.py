from coffee import Coffee  # Needed for isinstance check in most_aficionado

class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    def __repr__(self):
        return f"Customer('{self.name}')"

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("Argument must be a Coffee instance.")
        
        customer_order_counts = {}

        for order in coffee.orders():
            customer = order.customer
            customer_order_counts[customer] = customer_order_counts.get(customer, 0) + 1

        if not customer_order_counts:
            return None

        return max(customer_order_counts, key=customer_order_counts.get)
