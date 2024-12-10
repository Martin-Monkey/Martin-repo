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



