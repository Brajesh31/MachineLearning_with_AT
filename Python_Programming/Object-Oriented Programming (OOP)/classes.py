# classes.py

# Defining a simple class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object and calling methods
person = Person("John", 30)
person.introduce()
