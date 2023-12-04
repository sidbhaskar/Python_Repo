class Item:
    pay_rate = 0.8  # the pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity: int):
        # validator
        assert price >= 0, f"Price {price} is not greater then 0"
        assert quantity >= 0, f"quantity {quantity} is not greater then 0"

        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to perform
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item('Phone', 100, 5)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 3)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)

