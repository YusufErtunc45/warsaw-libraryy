class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"Book(Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available})"
