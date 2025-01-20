# model.py

class Pizza:
    def __init__(self, name, size, price, toppings=None):
        self.name = name
        self.size = size
        self.price = price
        self.toppings = toppings or []

    def add_topping(self, topping):
        self.toppings.append(topping)
        self.price += topping.price

    def __str__(self):
        return f"{self.size} {self.name} with {', '.join(map(str, self.toppings))} - ${self.price:.2f}"


class Topping:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


class Order:
    def __init__(self):
        self.pizzas = []
        self.total = 0

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)
        self.total += pizza.price

    def __str__(self):
        return "\n".join(map(str, self.pizzas)) + f"\nTotal: ${self.total:.2f}"


class Sales:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.orders = 0
            cls._instance.total_sales = 0
        return cls._instance

    def record_sale(self, amount):
        self.orders += 1
        self.total_sales += amount

    def show_sales(self):
        return f"Total Orders: {self.orders}, Total Sales: ${self.total_sales:.2f}"


class PaymentStrategy:
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card."


class CashPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} in Cash."



def create_pizzas():
    pizzas = [
        Pizza("Margherita", "Small", 5.00, [Topping("Tomato", 0.5), Topping("Cheese", 1)]),
        Pizza("Pepperoni", "Medium", 7.00, [Topping("Pepperoni", 2), Topping("Cheese", 1)]),
        Pizza("Vegetarian", "Large", 8.00, [Topping("Mushrooms", 1), Topping("Olives", 1), Topping("Peppers", 1)]),
        Pizza("Hawaiian", "Medium", 7.50, [Topping("Ham", 2), Topping("Pineapple", 1)]),
        Pizza("BBQ Chicken", "Large", 9.00, [Topping("BBQ Sauce", 1), Topping("Chicken", 2)])
    ]
    return pizzas
