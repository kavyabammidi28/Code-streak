# ✅ Day 46: Multiple Inheritance (OOPs)
# Problem
# Create two classes Teacher and Student,
#  and a derived class TeachingAssistant that inherits from both.

class Teacher:
    def __init__(self, subject):
        self.subject = subject

    def teach(self):
        print(f"Teaching {self.subject}")

class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name} is studying hard!")

class TeachingAssistant(Teacher, Student):
    def __init__(self, name, subject):
        Teacher.__init__(self, subject)
        Student.__init__(self, name)

    def assist(self):
        print(f"{self.name} assists in {self.subject} class.")

# Example usage
ta = TeachingAssistant("Kavya", "Python")
ta.study()
ta.teach()
ta.assist()
