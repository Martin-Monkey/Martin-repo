
class UI:
    @staticmethod
    def show_main_menu():
        print("1. Create Order")
        print("2. Pay")
        print("3. Show Sales")
        print("4. Show Pizzas")
        print("5. Exit")

    @staticmethod
    def show_pizzas(pizzas):
        print("\nAvailable Pizzas:")
        for i, pizza in enumerate(pizzas, 1):
            print(f"{i}. {pizza}")

    @staticmethod
    def show_order_summary(order):
        print("\nYour Order:")
        print(order)

    @staticmethod
    def show_payment_method():
        print("\nSelect payment method:")
        print("1. Credit Card")
        print("2. Cash")
