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
    #Name: __init__
    #Purpose: __init__ creates a new library object with two empty lists, one intended to hold books in the library system, and the other intended to hold the books on loan to the user.
    #Input: none
    #Output: none
    def __init__(self):
        self.book_list = []
        self.loan_list = []

    #Name: add_book
    #Purpose: add_book add on a new book object to the end of the current library's book_list. 
    #Input: Book object to be added
    #Output: none
    def add_book(self, book):
        self.book_list.append(book)
        #book.library_index = len(self.book_list) - 1

    #Name: remove_book
    #Purpose: remove_book searches for any book with the provided title in the library's book_list and removes them.
    #Input: String title of the book to be removed
    #Output: Print statement displaying to the user the removed book. 
    def remove_book(self, title):
        for book in self.book_list:
            if(book.title == title):
                self.book_list.remove(book)
                print(f"Removed {book.title}")
                break

    #Name: describe_books
    #Purpose: describe_books prints out the attributes of each book in the library's book_list, allowing the user to see all books currently in the library system.
    #Input: none
    #Output: Print statements (one line for each book) of the title, author, isbn number, and availability of each book in the current book_list. 
    def describe_books(self):
        print("LIBRARY::")
        for book in self.book_list:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Availability: {book.availability}")
        print("")

    #Name: describe_loans
    #Purpose: describe_loans prints out the attributes (except availability) of each book in the library's loan_list, allowing the user to see all books they have checked out.
    #Input: none
    #Output: Print statements (one line for each book) of the title, author, and isbn number of each book in the current loan_list. 
    def describe_loans(self):
        print("LOANS::")
        for book in self.loan_list:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
        #print("")


    #Name: search_book
    #Purpose: search_book checks the current book_list to see if a book by the specified title exists. If it does, the index of the book in book_list is returned, and if it does not -1 is returned. A print statement detailing whether the book is in the system is also run.
    #Input: Title of book to check book_list for.
    #Output: int book_index, print statement informing the user of the result of the check.
    def search_book(self, title):
        book_index = -1
        for i in range(0, len(self.book_list)):
            if(self.book_list[i].title == title):
                book_index = i
                print(f"{title} is in the library system. Availability: {self.book_list[i].availability}")
        if(book_index == -1):
            print(f"{title} is not in the library system.")

            #book_index is returned so search_book() can be easily used as the first step of taking out a loan. 
        return book_index
    
    #Name: get_library_index
    #Purpose: get_library_index checks the current book_list to see if a book by the specified title exists. If it does, the index of the book in book_list is returned, and if it does not -1 is returned. 
    #Input: Title of book to check book_list for.
    #Output: int book_index
    #This function is very similar to 'search_book()', except print statements are removed. This is useful for minimizing clutter in the console. 
    def get_library_index(self, title):
        book_index = -1
        for i in range(1, len(self.book_list)):
            if(self.book_list[i].title == title):
                book_index = i

        return book_index
    

    #Name: take_loan
    #Purpose: Allows the user to check out one of the books, making it unavailable in the library system and adding it to the loan_list for
        # the library class. 
    #Input: String title of book to check out
    #Output: print statement either printing information about the book that was checked out, or why the book couldn't be checked out.
    def take_loan(self, title):
            #Gets the index of the desired book in the library's book_list, so information about the book can be referenced.
        book_index = self.search_book(title)
            #If the book exists in the system and the book is available, then the checkout procedes
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

    #Name: return_loan
    #Purpose: return_loan removes a book from loan_list and gives it back to the library, setting the availability of the book returned back to True
    #Input: String title of book currently in loan_list to be returned.
    #Output: Print statement either confirming the return or stating that the title entered isn't in the loan list. 
    def return_loan(self, title):
        #loan_index is the index of the book being returned in loan_list, while library_index is the index of the same book in book_list. 
        #The "not present" value for loan_index must be -1, as 0 is a valid index. 
        loan_index = -1
        library_index = self.get_library_index(title)
        for i in range(0, len(self.loan_list)):
                #If the book exists in the loan list, then make it available again in book_list and remove it from loan list
            if(self.loan_list[i].title == title):
                loan_index = i
                self.book_list[library_index].availability = True
                self.loan_list.remove(self.loan_list[i])
                print(f"{title} has been returned from your loans")
            #If the book is not in loan_list, print a message telling the user
        if(loan_index == -1):
            print(f"{title} is not in your loans.")
        print("")


#MAIN
#Creates the library bobject
main_library = Library()

#Sets information for books
book1 = Book("The Lord of the Rings", "Tolkien", 8991148177578, True)
book2 = Book("I Cheerfully Refuse", "Enger", 4906172209419, False)
book3 = Book("Black Holes", "Forshaw, Cox", 7672344800463, True)

#Adds books to library
main_library.add_book(book1)
main_library.add_book(book2)
main_library.add_book(book3)

#Tests removing books and searching the library

main_library.describe_books()
main_library.remove_book("The Lord of the Rings")
main_library.describe_books()
main_library.search_book("The Lord of the Rings")
main_library.search_book("I Cheerfully Refuse")

#Tests taking and returning loans from the library

main_library.take_loan("Black Holes")
main_library.describe_loans()
print("Testing checking out an absent book:")
main_library.take_loan("Black Holes")
main_library.describe_books()
main_library.return_loan("Black Holes")
main_library.describe_loans()
main_library.describe_books()




