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


# Použití mixéru
class Blender(Device):
    def __init__(self, name, is_on=False, speed=1):
        super().__init__(name, is_on)
        self.speed = speed  # Rychlost mixování (1-5)

    def blend(self):

        if self.is_on:
            print(f"Mixuji na rychlosti {self.speed}.")
        else:
            print("Mixér není zapnutý. Nejprve ho zapněte.")

    def set_speed(self, speed):
        """Nastaví rychlost mixování (1-5)."""
        if 1 <= speed <= 5:
            self.speed = speed
            print(f"Rychlost mixéru nastavena na {self.speed}.")
        else:
            print("Rychlost musí být mezi 1 a 5.")


# Použití mlýnku na maso
class MeatGrinder(Device):
    def __init__(self, name, is_on=False, grinding_speed=1):
        super().__init__(name, is_on)
        self.grinding_speed = grinding_speed  # Rychlost mletí (1-3)

    def grind_meat(self):

        if self.is_on:
            print(f"Meleme maso na rychlosti {self.grinding_speed}.")
        else:
            print("Mlýnek na maso není zapnutý. Nejprve ho zapněte.")

    def set_grinding_speed(self, grinding_speed):
        """Nastaví rychlost mletí masa (1-3)."""
        if 1 <= grinding_speed <= 3:
            self.grinding_speed = grinding_speed
            print(f"Rychlost mletí nastavena na {self.grinding_speed}.")
        else:
            print("Rychlost mletí musí být mezi 1 a 3.")


