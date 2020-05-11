import csv
from Person import Person
from Catalog import Catalog
from Book import Book
catalog = Catalog()
#Loanitem/loanadministration:
#- Een loanid moet aan een persoonid gekoppeld kunnen worden, en er moet 1 boek in de loanitem af gaan
#- Een loanid moet losgekoppeld kunnen worden van een persoonid, en er moet 1 boek bij komen bij loanitem
class LoanAdministration:
    def __init__(self, persoonId, loanId):
        self.__persoonId = persoonId
        self.__loanId = loanId

    books = catalog.returnBooks()

    def getPersoonId(self):
        return self.__persoonId

    def getLoanId(self):
        return self.__loanId
    

    
    def reserveer_boek(self, loggedinUser, persoonId, loanId):
        print("***** Reserveer een boek *****")
        titel_boek = input("Zoek boek op titel of ISBN:")
        for i in books:
            if titel_boek == i.getTitle or titel_boek == i.getISBN:
                print(i.printBook)
                reserveren_boek = input("1) Reserveer het boek \n0) Reserveer het boek niet")
                if reserveren_boek == "1":
                    #Add the book to Person localy
                    loggedinUser.addBookToLoaned(i.getLoanId)
                    #Add the book to Person in csv 
                    fields=[persoonId,loanId]
                    with open(r'loanAdministration.csv', 'a') as addLoan:
                        writer = csv.writer(addLoan)
                        writer.writerow(fields)
                    print("Het boek is toegevoegd aan de geleende boeken")
                else:
                   start_keuze_gebruiker = input("6) Zoek opnieuw \n0) Terug naar menu") 
            else:
                print("titel bestaat niet")
                start_keuze_gebruiker = input("6) Zoek opnieuw \n0) Terug naar menu")
