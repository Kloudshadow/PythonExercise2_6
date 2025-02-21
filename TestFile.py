"""

Classes to work on: Library (with accompanying book class), Simple Game (if time)
"""


class Book:
    def __init__(self, title, author, isbn, availability):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability



class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)

    


