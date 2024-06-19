from book import Book
from librarian import Librarian
from library import Library
from patron import Patron


library = Library("Central Library")
librarian = Librarian("John Doe", 1)
patron = Patron("Jane Smith", 2)

book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")

librarian.add_book(library, book1)
librarian.add_book(library, book2)
librarian.add_patron(library, patron)

patron.borrow_book(book1)
patron.return_book(book1)

print(library.list_books())
print(library.list_patrons())