from person import Person

class Patron(Person):
    def __init__(self, name, patron_id):
        super().__init__(name, patron_id)
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
        else:
            print(f"Book '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
        else:
            print(f"Book '{book.title}' is not borrowed by '{self.name}'.")

    def __str__(self):
        return f"Patron(Name: {self.name}, ID: {self.person_id}, Borrowed Books: {[book.title for book in self.borrowed_books]})"