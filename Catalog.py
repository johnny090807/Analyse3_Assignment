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
        dict = [{
            "thing": 'title',
            "type": ""
        },
            {
            "thing": 'authorName',
            "type": ""
        },
            {
            "thing": 'authorAge',
            "type": ""
        },
            {
            "thing": 'ISBN',
            "type": ""
        }]
        for i in dict:
            while i.get("type") == "":
                try:
                    i["type"] = str(input("What's the " + i.get("thing") + "? "))
                except:
                    print("something went wrong.")
        print(dict[0].get("type"), dict[1].get("type"), dict[2].get("type"), dict[3].get("type"))
        self.__Books.append(Book(dict[0].get("type"), dict[1].get("type"), dict[2].get("type"), dict[3].get("type")))

    def addPerson(self):
        dict = [{
            "thing": 'first name',
            "type": ""
        },
            {
                "thing": 'last name',
                "type": ""
            },
            {
                "thing": 'username',
                "type": ""
            },
            {
                "thing": 'password',
                "type": ""
            }]
        for i in dict:
            while i.get("type") == "":
                try:
                    i["type"] = str(input("What's the " + i.get("thing") + "? "))
                except:
                    print("something went wrong.")
        try:
            userId = self.__Users[:-1].getUserId() + 1
        except:
            userId = 1
        self.__Users.append(Person(userId, dict[0].get("type"), dict[1].get("type"), dict[2].get("type"), dict[3].get("type")))

def login():
    str(input("Username: "))
    str(input("Password: "))

#login
    answer = input("Do you have an account?(yes or no) ")
if answer == 'yes' :
   login = False
   csvfile = open("Username password.csv","r")
   reader = csv.reader('Username password.csv')
   username = input("Player One Username: ")
   password = input("Player One Password: ")
   for row in reader:
        if row[0]== username and row[1] == password:
           login = True
        else:
           login = False
   if login == False:
      print("Incorrect. Game Over.")
      exit()
   else:
      print("You are now logged in!")
else:
   print('Only Valid Usernames can play. Game Over.')
   exit()
