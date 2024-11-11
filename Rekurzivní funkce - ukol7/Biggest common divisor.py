print("---Aplikace pro nalezení největšího společného dělitele dvou čísel---")
def biggest_comm_div(a, b):
    if b == 0:
        return a
    else:
        return biggest_comm_div(b, a % b)

a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))

print(f"Největší společný dělitel čísel {a} a {b} je {biggest_comm_div(a, b)}. ")
