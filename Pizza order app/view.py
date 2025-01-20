
class UI:
    @staticmethod
    def show_main_menu():
        print("1. Vytvořit objednávku")
        print("2. Platit")
        print("3. Zobrazit hotové objednávky")
        print("4. Zobrazit nabídku pizze")
        print("5. Konec")

    @staticmethod
    def show_pizzas(pizzas):
        print("\nNabídka pizze:")
        for i, pizza in enumerate(pizzas, 1):
            print(f"{i}. {pizza}")

    @staticmethod
    def show_order_summary(order):
        print("\nVaše objednávka:")
        print(order)

    @staticmethod
    def show_payment_method():
        print("\nZvolte platební metodu:")
        print("1. Creditní karta")
        print("2. Hotovost")
