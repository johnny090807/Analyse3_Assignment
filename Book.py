from Author import Author
class Book:
    def __init__(self, bookId, title, authorName, authorAge, ISBN):
        self.__bookId = bookId
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

    def getBookId(self):
        return self.__bookId

    def __str__(self):
        return self.__title + "\n" + self.__author.getName() + "\n" + self.__author.getAge() + "\n" + self.__ISBN + "\n" 
