from Book import Book

class loanItem:
   def __init__(self, bookId, aantal = 3):
      self.__aantal = int(aantal)
      self.__bookId = bookId

   def getAantal(self):
      return self.__aantal
   
   def reduceAantal(self):
      self.__aantal -= 1

   def getBookId(self):
      return self.__bookId