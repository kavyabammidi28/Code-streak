class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee: {self.name}, Base Salary: {self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_total_salary(self):
        return self.salary + self.bonus

class Manager(Employee):
    def __init__(self, name, salary, allowance):
        super().__init__(name, salary)
        self.allowance = allowance

    def calculate_total_salary(self):
        return self.salary + self.allowance

# Example usage
d = Developer("Kavya", 40000, 8000)
m = Manager("Riya", 50000, 10000)

d.display()
print("Total Salary (Developer):", d.calculate_total_salary())

m.display()
print("Total Salary (Manager):", m.calculate_total_salary())
