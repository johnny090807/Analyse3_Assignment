from Author import Author
class Book:
    def __init__(self, title, authorName, authorAge, ISBN):
        self.__title = title
        self.__author = Author(authorName, authorAge)
        self.__ISBN = ISBN

    def getTitle(self):
        return self.__title

    def getAuthor(self):
        return self.__author

    def getISBN(self):
        return self.__ISBN

    def setTitle(self, title):
        self.__title = title

    def getAuthor(self, author):
        self.__author = author

    def getISBN(self, isbn):
        self.__ISBN = isbn
