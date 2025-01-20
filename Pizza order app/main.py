# main.py

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
                controller.process_payment()
            else:
                print("No order created.")
        elif choice == '3':
            controller.show_sales()
        elif choice == '4':
            Parser.save_order(controller.order, 'order.json')
            print("Order saved to file.")
        elif choice == '5':
            print("Goodbye!")
            break

if __name__ == "__main__":
    run()
