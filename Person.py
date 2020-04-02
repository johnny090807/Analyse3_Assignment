class Person:
    def __init__(self, firstName, lastName, username, password, admin = False):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__username = username
        self.__password = password
        self.__admin = admin

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
