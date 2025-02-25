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

    def describe_books(self):
        for book in self.book_list:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Availability: {book.availability}")

    def remove_book(self, title):
        for book in self.book_list:
            if(book.title == title):
                self.book_list.remove(book)
                print(f"Removed {book.title}")
                break


#MAIN
print("Doing a bit of testing real fast.")

main_library = Library()

book1 = Book("The Lord of the Rings", "Tolkien", 8991148177578, True)
book2 = Book("I Cheerfully Refuse", "Enger", 4906172209419, False)
book3 = Book("Black Holes", "Forshaw, Cox", 7672344800463, True)

main_library.add_book(book1)
main_library.add_book(book2)
main_library.add_book(book3)

main_library.describe_books()

main_library.remove_book("The Lord of the Rings")

main_library.describe_books()

    


