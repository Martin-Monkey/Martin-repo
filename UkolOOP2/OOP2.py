# Ovládání Kávovaru, mixéru a mlýnku s použitím dědičnosti OOP


class Device:
    def __init__(self, name, is_on=False):
        self.name = name  # Název zařízení
        self.is_on = is_on  # Stav zařízení, zda je zapnuto nebo vypnuto

    def turn_on(self):
        """Zapne zařízení."""
        self.is_on = True
        print(f"{self.name} je zapnuté.")

    def turn_off(self):
        """Vypne zařízení."""
        self.is_on = False
        print(f"{self.name} je vypnuté.")

    def get_status(self):
        """Vrátí stav zařízení."""
        return "zapnuto" if self.is_on else "vypnuto"


# Příprava kávy
class CoffeeMachine(Device):
    def __init__(self, name, is_on=False, coffee_type="Espresso"):
        super().__init__(name, is_on)
        self.coffee_type = coffee_type  # Typ kávy, který kávovar připraví

    def make_coffee(self):

        if self.is_on:
            print(f"Připravuji {self.coffee_type} kávu.")
        else:
            print("Kávovar není zapnutý. Nejprve ho zapněte.")

    def set_coffee_type(self, coffee_type):
        """Nastaví typ kávy."""
        self.coffee_type = coffee_type
        print(f"Typ kávy nastaven na {self.coffee_type}.")


