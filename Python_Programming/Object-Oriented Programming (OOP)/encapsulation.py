# encapsulation.py

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount!")

# Creating an account and accessing balance
account = BankAccount(1000)
print(f"Initial balance: {account.get_balance()}")

account.set_balance(1200)
print(f"Updated balance: {account.get_balance()}")

# Trying to set an invalid balance
account.set_balance(-500)
