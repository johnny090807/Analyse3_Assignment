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

    def setAuthor(self, author):
        self.__author = author

    def setISBN(self, isbn):
        self.__ISBN = isbn

    def printBook(self):
        print(self.__title + "\n" + self.__author + "\n" + self.__ISBN + "\n")
