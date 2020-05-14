import csv
from Book import Book
#Loanitem/loanadministration:
#- Een loanid moet aan een persoonid gekoppeld kunnen worden, en er moet 1 boek in de loanitem af gaan
#- Een loanid moet losgekoppeld kunnen worden van een persoonid, en er moet 1 boek bij komen bij loanitem
class LoanItem:
    def __init__(self, title, loanId, aantal, bookId):
        self.__title = title
        self.__loanId = loanId
        self.__aantal = aantal
        self.__book = bookId
        self.fillBook()

    def fillBook(self):
        with open('Catalog.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                try:
                    if row['bookId'] == self.__book:
                        self.__book = Book(row["bookId"], row["title"], row["authorName"], row["authorAge"], row["ISBN"])
                except:
                    pass