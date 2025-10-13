class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}. Remaining Balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        print(f"Current Balance: {self.__balance}")

# Example usage
acc = Account("Kavya", 1000)
acc.get_balance()
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(1500)

