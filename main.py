from Book import Book
import csv


print("__Reserverings Systeem__")
user = input("Subscriber press 1 | Librarian fill in password")

while user == "1":
    print("Welcome Subscriber!")
    bookSearch = input("Search for a book by title, author or ISBN \nif you want to cancel enter QUIT ")
    if bookSearch == "":
        print("BOOK INFO, AVAILABILITY")
        availability = True
        if availability:
            purchase = input("press 1 to loan the book \npress 2 to search for another book")
            if purchase == "1":
                print("congratulations you loaned the book ")
    elif bookSearch == "QUIT":
        user = "0"

while user == "password123":
    print("Welcome Librarian!")
    librarianAction = input("press 1 to add a book \npress 2 to add a customer "
                            "\npress 3 to make a back up \nto quit enter QUIT")
    if librarianAction == "1":
        input("details of the new book item")
    elif librarianAction == "2":
        input("details of the new customer")
    elif librarianAction == "3":
        input("make a back up")
    elif librarianAction == "QUIT":
        user = "0"



