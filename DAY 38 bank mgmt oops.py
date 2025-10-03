class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount")

    def display(self):
        print(f"Account No: {self.account_number}, Name: {self.name}, Balance: {self.balance}")


# Example usage
acc1 = BankAccount(101, "Kavya", 1000)
acc1.display()
acc1.deposit(500)
acc1.withdraw(300)
acc1.withdraw(1500)   # test insufficient balance
