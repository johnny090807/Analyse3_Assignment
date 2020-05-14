from loanAdministration import LoanAdministration
import csv
class Person:
    def __init__(self, userId, firstName, lastName, username, password, admin=False):
        self.__userId = userId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__username = username
        self.__password = password
        self.__admin = admin
        self.__bookLoans = []
        self.fillBookLoans()

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def isAdmin(self):
        return self.__admin

    def getUserId(self):
        return self.__userId

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def changeAdmin(self, admin):
        self.__admin = admin

    def getBookLoans(self):
        return self.__bookLoans

    def addBookLoan(self, bookId):
        self.__bookLoans.append(bookId)

    def fillBookLoans(self):
        with open('LoanAdministration.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['userId'] == self.__userId:
                    self.__bookLoans.append(LoanAdministration(row['userId'], row['loanId']))
