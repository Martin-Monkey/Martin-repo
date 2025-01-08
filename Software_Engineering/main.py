"""class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0 or age >= 130:
            raise ValueError("Age must be between 0 and 130")
        self._age = age

    def display(self):
        print(f"{self.name} {self.last_name} {self.age}")

    def input_data(self):
        self.name = input("Enter name: ")
        self.last_name = input("Enter last name: ")
        self.age = int(input("Enter age: "))


obj = User("Bill", "Windows", 34)
obj.display()
obj.input_data()
obj.display()"""

#Lepší verze

class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0 or age >= 130:
            raise ValueError("Age must be between 0 and 130")
        self._age = age

class Console:
    @staticmethod
    def display(obj):
        print(f"{obj.name} {obj.last_name} {obj.age}")

    @staticmethod
    def input():
        name = input("Input name: ")
        last_name = input("Input last name: ")
        age = int(input("Input age: "))
        return User(name, last_name, age)

# Vytvoření objektu User a zobrazení jeho údajů
obj = User("Bill", "Windows", 34)
Console.display(obj)

# Získání údajů od uživatele a vytvoření nového objektu User
obj = Console.input()
Console.display(obj)
