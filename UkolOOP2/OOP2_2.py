# Zobrazení aktuálního času / Task 1

import time

# hvězdičkový dekoratér
def add_asterisks(func):
    def wrapper():
        print('*' * 25)
        result = func()
        print(result)
        print('*' * 25)
    return wrapper

# Task 2 -> # Další dekoratér - přidá text před výstup času
def add_text_to_output(func):
     def wrapper():
         result = func()  # Zavolání původní funkce
         return f"Aktuální čas je: {result}"  # Přidání textu před výstup
     return wrapper

# Použití obou dekorátorů
@add_asterisks
@add_text_to_output
def display_time():
    current_time = time.strftime("%H:%M")  # Získání aktuálního času
    return current_time

# Zavolání funkce
display_time()