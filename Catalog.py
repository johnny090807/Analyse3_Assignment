import csv
from Book import Book
from Person import Person
class Catalog:
    def __init__(self):
        self.__Books = []
        self.__Users = []
        self.fillCatalog()
        self.fillUsers()
        loggedInUser = None

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
            print(book.getTitle(), "|", book.getAuthor().getName(), "|", book.getAuthor().getAge(), "|", book.getISBN())

    def printUsers(self):
        for user in self.__Users:
            print(user.getUserId(), user.getFirstName(), "|", user.getLastName())

    def fillCatalog(self):
        with open('Catalog.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.__Books.append(Book(row["title"], row["authorName"], row["authorAge"], row["ISBN"]))

    def fillUsers(self):
        with open('Person.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.__Users.append(Person(row["userId"], row["firstName"], row["lastName"], row["username"], row["password"], row["admin"]))

    def addBook(self):
        array = ["", "", 0, ""]
        PersonList = ['title', 'author name', 'author age', 'ISBN']
        count = 0
        for i in array:
            if type(i).__name__ == "str":
                while i == "":
                    try:
                        i = str(input("What's the " + PersonList[count] + "? "))
                    except:
                        print("something went wrong.")
            if type(i).__name__ == "int":
                while i == 0:
                    try:
                        i = int(input("What's the " + PersonList[count] + "? "))
                    except:
                        print("something went wrong.")
            count += 1
        self.__Books.append(Book(array[0], array[1], array[2], array[3]))
        with open('Catalog.csv', mode='w') as csv_file:
            fieldnames = ['title', 'authorName', 'authorAge', 'ISBN']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for i in self.__Books:
                writer.writerow({'title': i.getTitle(), 'authorName': i.getAuthor.getName(), 'authorAge': i.getAuthor.getName(), 'ISBN': i.getISBN()})

    def addPerson(self, admin = False):
        array = ["", "", "", "", admin]
        PersonList = ['First name', 'last name', 'username', 'password']
        count = 0
        for i in array:
            while i == "":
                try:
                    i = str(input("What's the " + PersonList[count] + "? "))
                except:
                    print("something went wrong.")
            count += 1
        try:
            userId = self.__Users[:-1].getUserId() + 1
        except:
            userId = 1
        self.__Users.append(Person(userId, array[0], array[1], array[2], array[3], array[4]))

        with open('Person.csv', mode='w') as csv_file:
            fieldnames = ['firstName', 'lastName', 'username', 'password']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for i in self.__Users:
                writer.writerow({'userId': i.getUserId(), 'firstName': i.getFirstName(), 'lastName': i.getLastName(), 'username': i.getUsername, 'password': i.getPassword, 'admin': i.isAdmin()})
    #
    # def loginUser(self):
    #     answer = input("Do you have an account?(yes or no)")
    #     if answer == 'yes' :
    #         login = False
    #         csvfile = open("Username password.csv","r")
    #         reader = csv.reader('Username password.csv')
    #         username = input("Player One Username: ")
    #         password = input("Player One Password: ")
    #         for row in reader:
    #             if row[0]== username and row[1] == password:
    #                 login = True
    #             else:
    #                 login = False
    #         if not login:
    #           print("Incorrect. Game Over.")
    #           exit()
    #        else:
    #           print("You are now logged in!")
    #     else:
    #        print('Only Valid Usernames can play. Game Over.')
    #        exit()
    #
    #
