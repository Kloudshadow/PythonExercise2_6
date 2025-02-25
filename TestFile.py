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
        self.loan_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def describe_books(self):
        print("LIBRARY::")
        for book in self.book_list:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Availability: {book.availability}")
        print("")

    def describe_loans(self):
        print("LOANS::")
        for book in self.loan_list:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        print("")


    def remove_book(self, title):
        for book in self.book_list:
            if(book.title == title):
                self.book_list.remove(book)
                print(f"Removed {book.title}")
                break


    #book_index is returned so search_book() can be easily used as the first step of taking out a loan. 
    def search_book(self, title):
        book_index = 0
        for i in range(1, len(self.book_list)):
            if(self.book_list[i].title == title):
                book_index = i
                print(f"{title} is in the library system. Availability: {self.book_list[i].availability}")
        if(book_index == 0):
            print(f"{title} is not in the library system.")

        return book_index
    
    def take_loan(self, title):
        book_index = self.search_book(title)
        if(book_index > 0):
            self.loan_list.append(self.book_list[book_index])
            self.book_list[book_index].availability = False
            print(f"Checked out {self.book_list[book_index].title} by {self.book_list[book_index].author}")
            
    #def return_loan(self)


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

main_library.search_book("The Lord of the Rings")
main_library.search_book("Black Holes")

main_library.take_loan("Black Holes")
main_library.describe_loans()

main_library.describe_books()


    


