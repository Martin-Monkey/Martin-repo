import json
import pickle

# 1. Třída Student
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Grades: {self.grades}"


# 2. Uložení objektu do souboru
def save_to_json(student, filename):
    with open(filename, 'w') as f:
        json.dump(student.__dict__, f)

def save_to_pickle(student, filename):
    with open(filename, 'wb') as f:
        pickle.dump(student, f)

# 3. Načtení objektu ze souboru
def load_from_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        return Student(data['name'], data['age'], data['grades'])

def load_from_pickle(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# Příklad použití
student1 = Student("Martin Sestak", 20, [1, 2, 1, 3])

# Uložení do souborů
save_to_json(student1, "student.json")
save_to_pickle(student1, "student.pkl")

# Načtení z JSON a Pickle
student_from_json = load_from_json("student.json")
student_from_pickle = load_from_pickle("student.pkl")

# Výpis obsahů
print("Načtený student z JSON:")
print(student_from_json)

print("Načtený student z Pickle:")
print(student_from_pickle)

mport
csv

# Otevření CSV souboru
with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Přečte všechny řádky a vypíše je
    for row in reader:
        print(row)