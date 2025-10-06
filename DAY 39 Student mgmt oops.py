class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks  # list of 3 subject marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A'
        elif avg >= 75:
            return 'B'
        elif avg >= 60:
            return 'C'
        else:
            return 'D'

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average():.2f}, Grade: {self.grade()}")

# Example usage
s1 = Student("Kavya", 101, [88, 92, 79])
s1.display()
