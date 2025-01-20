# controller.py

from model import Pizza, Topping, Order, Sales, CashPayment, CreditCardPayment, create_pizzas
from view import UI

class MainController:
    def __init__(self):
        self.sales = Sales()
        self.order = None
        self.pizzas = create_pizzas()

    def create_order(self):
        self.order = Order()
        UI.show_pizzas(self.pizzas)
        choice = int(input("Select pizza (1-5): ")) - 1
        pizza = self.pizzas[choice]
        self.order.add_pizza(pizza)
        UI.show_order_summary(self.order)

    def process_payment(self):
        UI.show_payment_method()
        method_choice = int(input("Choose payment method: "))
        if method_choice == 1:
            payment_method = CreditCardPayment()
        elif method_choice == 2:
            payment_method = CashPayment()
        else:
            print("Invalid option.")
            return
        print(payment_method.pay(self.order.total))
        self.sales.record_sale(self.order.total)

    def show_sales(self):
        print(self.sales.show_sales())
