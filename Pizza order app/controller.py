from model import Pizza, Topping, Order, Sales, CashPayment

class MainController:
    def __init__(self):
        self.sales = Sales()
        self.order = None

    def create_order(self):
        self.order = Order()
        pizza = Pizza("Margherita", "Medium", 8)
        self.order.add_pizza(pizza)
        topping = Topping("Olives", 1)
        pizza.add_topping(topping)

    def process_payment(self):
        payment_method = CashPayment()  # Můžete změnit na CreditCardPayment pro jiný způsob platby
        print(payment_method.pay(self.order.total))
        self.sales.record_sale(self.order.total)

    def show_sales(self):
        print(self.sales.show_sales())

