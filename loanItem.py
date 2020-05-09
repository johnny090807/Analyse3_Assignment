#Loanitem/loanadministration:
#- Een loanid moet aan een persoonid gekoppeld kunnen worden, en er moet 1 boek in de loanitem af gaan
#- Een loanid moet losgekoppeld kunnen worden van een persoonid, en er moet 1 boek bij komen bij loanitem
class LoanItem:
    def __init__(self, naam, loanId, aantal, uitgeleend, book):
        self.__naam = naam
        self.__loanId = loanId
        self.__aantal = aantal
        self.__uitgeleend = uitgeleend
        self.__book = book