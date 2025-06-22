# inheritance.py

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# Creating objects of base and derived classes
animal = Animal("Generic Animal")
dog = Dog("Buddy")

animal.speak()
dog.speak()
