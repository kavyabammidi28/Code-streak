class Book:
    def __init__(self, title, author, available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Available Copies: {self.available_copies}")

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"You borrowed '{self.title}'. Remaining copies: {self.available_copies}")
        else:
            print(f"'{self.title}' is currently unavailable.")

    def return_book(self):
        self.available_copies += 1
        print(f"You returned '{self.title}'. Available copies: {self.available_copies}")

# Example usage
b1 = Book("Python Basics", "Guido van Rossum", 2)
b1.display_info()
b1.borrow_book()
b1.borrow_book()
b1.borrow_book()  # unavailable
b1.return_book()
