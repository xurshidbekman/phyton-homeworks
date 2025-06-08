# farm model
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        return f"{self.name} the {self.species} is eating."

    def sleep(self):
        return f"{self.name} the {self.species} is sleeping."

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Cow")

    def make_sound(self):
        return f"{self.name} says 'Moo!'"

class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name, "Sheep")

    def make_sound(self):
        return f"{self.name} says 'Baa!'"

class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Chicken")

    def make_sound(self):
        return f"{self.name} says 'Cluck!'"

# Example Usage
cow = Cow("Bessie")
sheep = Sheep("Dolly")
chicken = Chicken("Chickpea")

print(cow.eat())
print(sheep.sleep())
print(chicken.make_sound())
# bamk aplication
import json

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Insufficient funds or invalid amount."

    def get_details(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = str(len(self.accounts) + 1)
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        return f"Account created successfully: {self.accounts[account_number].get_details()}"

    def view_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_details()
        return "Account not found."

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            result = self.accounts[account_number].deposit(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            result = self.accounts[account_number].withdraw(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def save_to_file(self):
        with open("accounts.json", "w") as f:
            json.dump({acc: vars(self.accounts[acc]) for acc in self.accounts}, f)

    def load_from_file(self):
        try:
            with open("accounts.json", "r") as f:
                data = json.load(f)
                self.accounts = {acc: Account(**data[acc]) for acc in data}
        except FileNotFoundError:
            self.accounts = {}

# Example Usage
bank = Bank()
print(bank.create_account("Alice", 100))
print(bank.deposit("1", 50))
print(bank.withdraw("1", 30))
print(bank.view_account("1"))
