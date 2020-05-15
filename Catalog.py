
import csv
from Book import Book
from Person import Person
from loanAdministration import LoanAdministration
from loanItem import loanItem

class Catalog:
    def __init__(self):
        self.__Books = []
        self.__Users = []
        self.__Administration = []
        self.__loanItems = []
        self.fillCatalog()
        self.fillUsers()
        self.fillAdministration()
        self.fillLoanItems()
        self.loggedInUser = None
        
    def returnBooks(self):
        return self.__Books

    def setBooks(self, books):
        self.__Books = books

    def returnUsers(self):
        return self.__Users

    def setUsers(self, users):
        self.__Users = users

    def printBooks(self):
        for book in self.__Books:
            print(book)

    def printUsers(self):
        for user in self.__Users:
            print(user)

    def reserveer_boek(self, loggedinUser, userId):
        books = self.filter()
        try:
            while len(books) > 1 or len(books) == 0:
                books = self.filter()
        except:
            books = self.filter()

        reserveren_boek = input("1) Reserveer het boek \n0) Reserveer het boek niet")
        if reserveren_boek == "1":
            for i in self.__loanItems:
                if i.getBookId() == books[0].getBookId():
                    if i.getAantal() > 0:
                        for x in self.__Books:
                            if x.getTitle() == books[0].getTitle() and x.getBookId() == books[0].getBookId():
                                i.reduceAantal()

                        
                        with open('LoanItems.csv', mode='w') as loanitemscsv:
                            fieldnames = ['bookId', 'aantal']
                            writer = csv.DictWriter(loanitemscsv, fieldnames=fieldnames)

                            writer.writeheader()
                            for p in self.__loanItems:
                                writer.writerow({'bookId': p.getBookId(), 'aantal': p.getAantal()})

                        #Add the book to Person localy
                        loggedinUser.addBookLoan(books[0].getBookId())
                        
                        #Add the book to Person in csv
                        with open(r'LoanAdministration.csv', 'a') as addLoan:
                            writer = csv.writer(addLoan)
                            writer.writerow({books[0].getBookId(), userId})
                        print("Het boek is toegevoegd aan uw geleende boeken")
                    else:
                        print("Het boek is niet meer op vooraad")
        else:
            start_keuze_gebruiker = input("3) Zoek opnieuw \n5) Terug naar menu") 
            if start_keuze_gebruiker == "3":
                self.reserveer_boek(loggedinUser, userId)
  

    def fillAdministration(self):
        with open('LoanAdministration.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.__Administration.append(LoanAdministration(row['userId'], row['loanId']))
    
    def fillLoanItems(self):
        with open('LoanItems.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.__loanItems.append(loanItem(row['bookId'], row['aantal']))

    def fillCatalog(self):
        with open('Catalog.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.__Books.append(Book(row["bookId"], row["title"], row["authorName"], row["authorAge"], row["ISBN"]))

    def fillUsers(self):
        with open('Person.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.__Users.append(Person(row["userId"], row["firstName"], row["lastName"], row["username"],
                                           row["password"], row["admin"]))

    def addBook(self):
        array = ["", "", 0, "", 0]
        PersonList = ['title', 'author name', 'author age', 'ISBN', 'aantal']
        count = 0
        for i in range(len(array)):
            if type(array[i]).__name__ == "str":
                while array[i] == "":
                    try:
                        array[i] = str(input("What's the " + PersonList[count] + "? "))
                    except:
                        print("something went wrong.")
            if type(array[i]).__name__ == "int":
                while array[i] == 0:
                    try:
                        array[i] = int(input("What's the " + PersonList[count] + "? "))
                    except:
                        print("something went wrong.")
            count += 1
        try:
            bookId = int(self.__Books[-1].getBookId()) + 1
        except:
            bookId = 0
        self.__Books.append(Book(bookId, array[0], array[1], array[2], array[3]))
        self.__loanItems.append(loanItem(bookId,array[4]))
        with open('LoanItems.csv', mode='w') as csv_file:
            fieldnames = ['bookId', 'aantal']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for i in self.__loanItems:
                writer.writerow({'bookId': i.getBookId(), 'aantal': i.getAantal()})

        with open('Catalog.csv', mode='w') as csv_file:
            fieldnames = ['bookId', 'title', 'authorName', 'authorAge', 'ISBN']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for i in self.__Books:
                writer.writerow({'bookId': i.getBookId(), 'title': i.getTitle(), 'authorName': i.getAuthor().getName(),
                                 'authorAge': i.getAuthor().getAge(), 'ISBN': i.getISBN()})

    def addPerson(self, admin = False):
        array = ["", "", "", "", admin]
        PersonList = ['First name', 'last name', 'username', 'password']
        for i in range(len(array)):
            while array[i] == "":
                try:
                    array[i] = str(input("What's the " + PersonList[i] + "? "))
                except:
                    print("something went wrong.")
        try:
            userId = int(self.__Users[-1].getUserId()) + 1
        except:
            userId = 0
        self.__Users.append(Person(userId, array[0], array[1], array[2], array[3], array[4]))
        with open('Person.csv', mode='w') as csv_file:
            fieldnames = ['userId', 'firstName', 'lastName', 'username', 'password', 'admin']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for i in self.__Users:
                writer.writerow({'userId': i.getUserId(), 'firstName': i.getFirstName(), 'lastName': i.getLastName(), 'username': i.getUsername(), 'password': i.getPassword(), 'admin': i.isAdmin()})

    def addPersonWithPermissions(self, admin=True):
        array = ["", "", "", "", admin]
        PersonList = ['First name', 'last name', 'username', 'password']
        for i in range(len(array)):
            while array[i] == "":
                try:
                    array[i] = str(input("What's the " + PersonList[i] + "? "))
                except:
                    print("something went wrong.")
        try:
            userId = int(self.__Users[:-1].getUserId()) + 1
        except:
            userId = 1
        self.__Users.append(Person(userId, array[0], array[1], array[2], array[3], array[4]))

#login
    def login(self):
        global existingUser
        existingUser = None
        answer = input("Do you have an account?(yes or no) ")
        if answer == 'yes':
            login = False
            username = input("Username: ")
            while existingUser == None:
                for i in self.__Users:
                    if i.getUsername() == username:
                        existingUser = i
                        break
                    else:
                        existingUser = None
                if existingUser == None:
                    username = input("Username not found, try again: ")
            password = input("Password: ")
            loggedIn = False
            while not loggedIn:
                if password == existingUser.getPassword():
                    self.loggedInUser = existingUser
                    loggedIn = True
                else:
                    password = input("Password was incorrect, try again:")
        elif answer == "no":
            self.addPerson()
        else:
            self.login()

    def filter(self):
        foundBooks = []
        searchTypes = ['Title', 'Author name', 'Author age', 'ISBN']
        for i in range(len(searchTypes)):
            print("Press", i + 1, "to search for", searchTypes[i])
        print("Press 5 to go back")
        choice = input("")
        running = True
        while running:
            if choice == "1":
                searchBook = input("Which book are you looking for by title? enter nothing to exit. ")
                count = 0
                if searchBook == "":
                    break

                for i in self.__Books:
                    if searchBook in i.getTitle():
                        print(i)
                        foundBooks.append(i)
                        count += 1
                if count == 0:
                    print("Nothing found")
                return foundBooks
            elif choice == "2":
                searchBook = input("Which book are you looking for by author name? enter nothing to exit. ")
                count = 0
                if searchBook == "":
                    break
                for i in self.__Books:
                    if searchBook in i.getAuthor().getName():
                        print(i)
                        foundBooks.append(i)
                        count += 1
                if count == 0:
                    print("Nothing found")
                return foundBooks
            elif choice == "3":
                searchBook = input("Which book are you looking for by author age? enter nothing to exit. ")
                count = 0
                if searchBook == "":
                    break
                for i in self.__Books:
                    if searchBook == str(i.getAuthor().getAge()):
                        print(i)
                        foundBooks.append(i)
                        count += 1
                if count == 0:
                    print("Nothing found")
                return foundBooks
            elif choice == "4":
                searchBook = input("Which book are you looking for by ISBN? enter nothing to exit. ")
                count = 0
                if searchBook == "":
                    break
                for i in self.__Books:
                    if searchBook == i.getISBN():
                        print(i)
                        foundBooks.append(i)
                        count += 1
                if count == 0:
                    print("Nothing found")
                return foundBooks
            elif choice == "5":
                running = False
            else:
                choice = input("Try again: ")

