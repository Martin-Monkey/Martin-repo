# Task problem s velkým blokem if-else

# Rozhraní pro objednávku
from abc import ABC, abstractmethod


class Order(ABC):
    @abstractmethod
    def process(self):
        pass


# Standardní objednávka
class StandardOrder(Order):
    def process(self):
        print("Processing standard order...")


# Expresní objednávka
class ExpressOrder(Order):
    def process(self):
        print("Processing express order...")


# Neznámý typ objednávky
class UnknownOrder(Order):
    def process(self):
        print("Unknown order type!")


# FactoryClass pro vytváření objednávek
class OrderFactory:
    @staticmethod
    def create_order(order_type: str) -> Order:
        if order_type == "standard":
            return StandardOrder()
        elif order_type == "express":
            return ExpressOrder()
        else:
            return UnknownOrder()


# Product class pro správu produktů
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


# class notifikace
class Notification:
    def notify(self, message: str):
        print(f"Notification: {message}")


if __name__ == "__main__":
    # Factory metod pro vytvoření objednávky
    order_type = "standard"  # Může být i "express" nebo jiný
    order = OrderFactory.create_order(order_type)

    # Zpracování objednávky
    print(f"Processing order: {order_type}")
    order.process()
