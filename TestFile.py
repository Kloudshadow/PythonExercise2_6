"""
Program Title: Library Class
Editor(s): Benjamin Burgess
Last Edited: 2/25/25

Library System:
Design a Book class with attributes like title, author, isbn, and availability.
Create a Library class that can add, remove, and search for books, and manage book loans.
"""

# Class for individual books, which have a title, author name, an isbn number, and a boolean stating whether they are currently available in the library.
class Book:
    #Name: __init__
    #Purpose: __init__ creates a new book object with the book's name, author, isbn number, and availability determined from parameters.
    #Input: String title, String author, int isbn, boolean availability
    #Output: none
    def __init__(self, title, author, isbn, availability):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability



# Class for a collection of books in a library system from the perspective of a single user, allowing them to add and remove books from the library as well as simulate taking out loans.
class Library:
    def __init__(self):
        self.book_list = []
        self.loan_list = []

    def add_book(self, book):
        self.book_list.append(book)
        #book.library_index = len(self.book_list) - 1

    def remove_book(self, title):
        for book in self.book_list:
            if(book.title == title):
                self.book_list.remove(book)
                print(f"Removed {book.title}")
                break


    def describe_books(self):
        print("LIBRARY::")
        for book in self.book_list:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Availability: {book.availability}")
        print("")

    def describe_loans(self):
        print("LOANS::")
        for book in self.loan_list:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        #print("")


    #book_index is returned so search_book() can be easily used as the first step of taking out a loan. 
    def search_book(self, title):
        book_index = -1
        for i in range(0, len(self.book_list)):
            if(self.book_list[i].title == title):
                book_index = i
                print(f"{title} is in the library system. Availability: {self.book_list[i].availability}")
        if(book_index == -1):
            print(f"{title} is not in the library system.")

        return book_index
    
    #This function is very similar to 'search_book()', except print statements are removed. 
    def get_library_index(self, title):
        book_index = -1
        for i in range(1, len(self.book_list)):
            if(self.book_list[i].title == title):
                book_index = i

        return book_index
    
    #Need to check availability for take_loan
    def take_loan(self, title):
        book_index = self.search_book(title)
        if(book_index > 0 and self.book_list[book_index].availability == True):
            self.loan_list.append(self.book_list[book_index])
            self.book_list[book_index].availability = False
            print(f"Checked out {self.book_list[book_index].title} by {self.book_list[book_index].author}")
        #Situation when book exists in the system but is checked out.
        elif(book_index > 0 and self.book_list[book_index].availability == False):
            print("Loan unsuccessful. The book you requested exists in the library system, but is currently on loan to someone else.")
        #Situation when book doesn't exist in system
        else:
            print("Loan unsuccessful. The book you requested does not exist in the library system.")

        print("")

            
    def return_loan(self, title):
        #The "not present" value for loan_index must be -1, as 0 is a valid index. 
        loan_index = -1
        library_index = self.get_library_index(title)
        for i in range(0, len(self.loan_list)):
            if(self.loan_list[i].title == title):
                loan_index = i
                #The book wasn't removed from the library list, so all we need to do is
                #change its availability back to 'True'
                #self.add_book(title)
                self.book_list[library_index].availability = True
                self.loan_list.remove(self.loan_list[i])
                print(f"{title} has been returned from your loans")
        if(loan_index == -1):
            print(f"{title} is not in your loans.")
        print("")


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
main_library.search_book("I Cheerfully Refuse")

main_library.take_loan("Black Holes")
main_library.describe_loans()

print("Testing checking out an absent book:")
main_library.take_loan("Black Holes")

main_library.describe_books()

main_library.return_loan("Black Holes")
main_library.describe_loans()

main_library.describe_books()




