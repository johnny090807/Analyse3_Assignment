class Catalog:
    def __init__(self, books):
        self.__Books = books

    def returnBooks(self):
        return self.__Books

    def setBooks(self, books):
        self.__Books = books