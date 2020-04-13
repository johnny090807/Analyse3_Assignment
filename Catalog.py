import csv
from Book import Book
from Person import Person
class Catalog:
    def __init__(self):
        self.__Books = []
        self.__Users = []
        self.fillCatalog()
        self.fillUsers()

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
        try:
            userId = self.__Users[:-1].getUserId() + 1
        except:
            userId = 1
        self.__Users.append(Person(userId, array[0], array[1], array[2], array[3]))

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
        self.__Users.append(Person(userId, array[0], array[1], array[2], array[3]))
