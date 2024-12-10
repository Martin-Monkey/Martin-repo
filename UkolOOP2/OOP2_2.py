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
    

# Funkce pro zobrazení aktuálního času s dekoratérem
@add_asterisks
def display_time():
    current_time = time.strftime("%H:%M")  # Získání aktuálního času
    return current_time

# Zavolání funkce
display_time()