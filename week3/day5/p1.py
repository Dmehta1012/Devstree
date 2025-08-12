class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = int(copies)
        self.available_copies = int(copies)
    
    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False
    
    def return_book(self):
        if self.available_copies < self.copies:
            self.available_copies += 1

    def __str__(self):
        return f"{self.title} by {self.author} (Available: {self.available_copies}/{self.copies})" 


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow(self, book):
        if book.borrow_book():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}'")
    
    def __str__(self):
        return f"Member: {self.name}, Borrowed: {[b.title for b in self.borrowed_books]}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            print(book)

    def display_members(self):
        print("\nLibrary Members:")
        for member in self.members:
            print(member)


# ===== Example Usage =====
library = Library()

# Add books
book1 = Book("Python Programming", "Devarsh Mehta", 3)
book2 = Book("Data Science 101", "Jay Patil", 2)
library.add_book(book1)
library.add_book(book2)

# Add members
member1 = Member("Alice", 1)
member2 = Member("Bob", 2)
library.add_member(member1)
library.add_member(member2)

# Borrow books
member1.borrow(book1)
member2.borrow(book1)
member2.borrow(book2)

# Return book
member1.return_book(book1)

# Display current status
library.display_books()
library.display_members()
