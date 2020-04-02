class Book:
    def __init__(self, title, author, ISBN):
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN

    def getTitle(self):
        return self.__title

    def getAuthor(self):
        return self.__author

    def getISBN(self):
        return self.__ISBN

    def setTitle(self, title):
        self.__title = title

    def setAuthor(self, author):
        self.__author = author

    def setISBN(self, isbn):
        self.__ISBN = isbn
