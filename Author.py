class Author:
    def __init__(self, naam, age):
        self.__naam = naam
        self.__age = age

    def getNaam(self):
        return self.__naam

    def getAge(self):
        return self.__age

    def setNaam(self, name):
        self.__naam = name

    def getAge(self, age):
        self.__age = age
