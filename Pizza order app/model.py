class Pizza:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price
        self.toppings = []

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

