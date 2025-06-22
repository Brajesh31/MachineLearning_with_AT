# polymorphism.py

# Base class
class Bird:
    def fly(self):
        print("Bird is flying.")

# Derived class
class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying.")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly.")

# Polymorphic behavior
def test_flight(bird):
    bird.fly()

# Testing with different bird types
sparrow = Sparrow()
penguin = Penguin()

test_flight(sparrow)
test_flight(penguin)
