
from controller import MainController
from view import UI
from file_manager import Parser

def run():
    controller = MainController()
    while True:
        UI.show_main_menu()
        choice = input("Select option: ")

        if choice == '1':
            controller.create_order()
        elif choice == '2':
            if controller.order:
                controller.process_payment()  # Platba
                Parser.save_order(controller.order, 'order.json')
                print("Order saved to file.")
            else:
                print("No order created.")
        elif choice == '3':
            controller.show_sales()
        elif choice == '4':
            UI.show_pizzas(controller.pizzas)
        elif choice == '5':
            print("Děkujeme, přiďte zas!")
            break

if __name__ == "__main__":
    run()
