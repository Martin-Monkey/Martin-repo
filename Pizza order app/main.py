from controller import MainController
from view import UI


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
            print("Goodbye!")
            break


if __name__ == "__main__":
    run()