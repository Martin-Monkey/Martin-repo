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

# Funkce ovládání uživatelem
def device_control():
    # instance jednotlivých zařízení
    coffee_machine = CoffeeMachine(name="Kávovar")
    blender = Blender(name="Mixér")
    meat_grinder = MeatGrinder(name="Mlýnek na maso")

    while True:
        print("\n--- Hlavní menu ---")
        print("1. Ovládat Kávovar")
        print("2. Ovládat Mixér")
        print("3. Ovládat Mlýnek na maso")
        print("4. Konec")

        choice = input("Vyberte číslo (1-4): ")

        if choice == '1':
            coffee_machine_menu(coffee_machine)
        elif choice == '2':
            blender_menu(blender)
        elif choice == '3':
            meat_grinder_menu(meat_grinder)
        elif choice == '4':
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


def coffee_machine_menu(coffee_machine):
    while True:
        print("\n--- Menu Kávovaru ---")
        print("1. Zapnout Kávovar")
        print("2. Vypnout Kávovar")
        print("3. Připravit kávu")
        print("4. Nastavit typ kávy")
        print("5. Zpět")

        choice = input("Vyberte číslo (1-5): ")

        if choice == '1':
            coffee_machine.turn_on()
        elif choice == '2':
            coffee_machine.turn_off()
        elif choice == '3':
            coffee_machine.make_coffee()
        elif choice == '4':
            coffee_type = input("Zadejte nový typ kávy (např. Espresso, Latte): ")
            coffee_machine.set_coffee_type(coffee_type)
        elif choice == '5':
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


def blender_menu(blender):
    while True:
        print("\n--- Menu Mixéru ---")
        print("1. Zapnout Mixér")
        print("2. Vypnout Mixér")
        print("3. Mixovat")
        print("4. Nastavit rychlost mixování")
        print("5. Zpět")

        choice = input("Vyberte číslo (1-5): ")

        if choice == '1':
            blender.turn_on()
        elif choice == '2':
            blender.turn_off()
        elif choice == '3':
            blender.blend()
        elif choice == '4':
            try:
                speed = int(input("Zadejte rychlost mixování (1-5): "))
                blender.set_speed(speed)
            except ValueError:
                print("Neplatná rychlost, musí to být číslo mezi 1 a 5.")
        elif choice == '5':
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


def meat_grinder_menu(meat_grinder):
    while True:
        print("\n--- Menu Mlýnku na maso ---")
        print("1. Zapnout Mlýnek na maso")
        print("2. Vypnout Mlýnek na maso")
        print("3. Mletí masa")
        print("4. Nastavit rychlost mletí")
        print("5. Zpět")

        choice = input("Vyberte číslo (1-5): ")

        if choice == '1':
            meat_grinder.turn_on()
        elif choice == '2':
            meat_grinder.turn_off()
        elif choice == '3':
            meat_grinder.grind_meat()
        elif choice == '4':
            try:
                speed = int(input("Zadejte rychlost mletí (1-3): "))
                meat_grinder.set_grinding_speed(speed)
            except ValueError:
                print("Neplatná rychlost, musí to být číslo mezi 1 a 3.")
        elif choice == '5':
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


# Spuštění programu
if __name__ == "__main__":
    device_control()
