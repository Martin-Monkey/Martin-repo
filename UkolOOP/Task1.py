class Car:
    def __init__(self, model=None, year=None, manufacturer=None, engine_capacity=None, color=None, price=None):
        """
        Konstruktor třídy Car, který inicializuje hodnoty pro jednotlivé atributy.
        """
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def input_data(self):
        """
        Metoda pro zadání údajů o autě od uživatele.
        """
        self.model = input("Enter car model: ")
        self.year = int(input("Enter year of manufacture: "))
        self.manufacturer = input("Enter manufacturer: ")
        self.engine_capacity = float(input("Enter engine capacity (in liters): "))
        self.color = input("Enter car color: ")
        self.price = float(input("Enter car price: "))

    def output_data(self):
        """
        Metoda pro zobrazení údajů o autě.
        """
        print(f"Car model: {self.model}")
        print(f"Year of manufacture: {self.year}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Engine capacity: {self.engine_capacity} liters")
        print(f"Car color: {self.color}")
        print(f"Price: {self.price} USD")

    # Přístupové metody (gettery)
    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_capacity(self):
        return self.engine_capacity

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    # Nastavovací metody (settery)
    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_engine_capacity(self, engine_capacity):
        self.engine_capacity = engine_capacity

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price


# Příklad použití třídy Car:

# Vytvoříme instanci třídy Car
my_car = Car()

# Umožníme uživateli zadat data o autě
my_car.input_data()

# Zobrazíme zadané údaje
print("\nCar Details:")
my_car.output_data()

# Můžeme také použít přístupové metody k získání jednotlivých atributů
print("\nAccessing data via getter methods:")
print(f"Model: {my_car.get_model()}")
print(f"Year of manufacture: {my_car.get_year()}")
print(f"Manufacturer: {my_car.get_manufacturer()}")
print(f"Engine capacity: {my_car.get_engine_capacity()}")
print(f"Color: {my_car.get_color()}")
print(f"Price: {my_car.get_price()}")
