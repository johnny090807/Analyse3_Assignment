#Loanitem/loanadministration:
#- Een loanid moet aan een persoonid gekoppeld kunnen worden, en er moet 1 boek in de loanitem af gaan
#- Een loanid moet losgekoppeld kunnen worden van een persoonid, en er moet 1 boek bij komen bij loanitem
class LoanAdministration:
    def __init__(self, persoonId, loanId):
        self.__persoonId = persoonId
        self.__loanId = loanId

    def getPersoonId(self):
        return self.__persoonId

    def getLoanId(self):
        return self.__loanId