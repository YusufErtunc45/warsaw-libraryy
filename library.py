class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"Book '{book.title}' not found in the library.")

    def add_patron(self, patron):
        self.patrons.append(patron)

    def remove_patron(self, patron):
        if patron in self.patrons:
            self.patrons.remove(patron)
        else:
            print(f"Patron '{patron.name}' not found in the library.")

    def list_books(self):
        return [str(book) for book in self.books]

    def list_patrons(self):
        return [str(patron) for patron in self.patrons]

    def __str__(self):
        return f"Library(Name: {self.name}, Books: {len(self.books)}, Patrons: {len(self.patrons)})"