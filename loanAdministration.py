class LoanAdministration:
    def __init__(self, persoonId, loanId):
        self.__persoonId = persoonId
        self.__loanId = loanId

    def getPersoonId(self):
        return self.__persoonId

    def getLoanId(self):
        return self.__loanId
