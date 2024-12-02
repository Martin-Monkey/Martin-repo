class TemperatureConverter:
    # Sledování počtu převodů
    conversion_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """
        Převod z Celsia na Fahrenheita.
        Formula: (Celsius * 9/5) + 32 = Fahrenheit
        """
        TemperatureConverter.conversion_count += 1
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """
        Převod z Fahrenheita na Celsia.
        Formula: (Fahrenheit - 32) * 5/9 = Celsius
        """
        TemperatureConverter.conversion_count += 1
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius

    @staticmethod
    def get_conversion_count():
        """
        Vrátí počet provedených převodů.
        """
        return TemperatureConverter.conversion_count


# Funkce pro zadání teploty uživatelem
def get_user_input():
    print("Teplotní Konvertor")
    print("1: Celsius na Fahrenheit")
    print("2: Fahrenheit na Celsius")

    choice = input("Zvol konverzi (1 or 2): ")

    if choice == "1":
        celsius = float(input("Vlož teplotu v Celsius: "))
        fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C se rovná {fahrenheit}°F")
    elif choice == "2":
        fahrenheit = float(input("Vlož teplotu v Fahrenheit: "))
        celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F se rovná {celsius}°C")
    else:
        print("Zlá volba. Prosím zvolte z možnosti 1 nebo 2.")

    # Získám počet provedených převodů
    print(f"Počet provedených konverzí: {TemperatureConverter.get_conversion_count()}")

get_user_input()