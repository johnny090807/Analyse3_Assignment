#Catalog:
#- Inlogfunctie maken
#- Persoon met rechten toekunnen voegen
#- Persoon zonder rechten toevoegen
class Catalog:
    def __init__(self, books):
        self.__Books = books

    def returnBooks(self):
        return self.__Books

    def setBooks(self, books):
        self.__Books = books