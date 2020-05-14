from Catalog import Catalog

catalog = Catalog()
# Dit is hoe je een loanId kan pakken van een user
#user = catalog.returnUsers()[1].getBookLoans()[0].getLoanId()

start_reservering = True
start_reservering_gebruiker = True
start_keuze = None
while start_reservering or start_keuze == "0":
    # Het menu als je niet bent ingelogd
    print("***** Reserverings systeem *****")
    start_keuze = input("1) Bekijk boeken \n2) Filter boeken \n3) Login \n4) Exit\n")

    while start_keuze == "1":
        print("***** Bekijk boeken *****")
        catalog.printBooks()
        start_keuze = input("Press enter to continue.")
    while start_keuze == "2":
        print("***** Filter boeken *****")
        catalog.filter()
        start_keuze = input("Press enter to continue.")
    while start_keuze == "4":
        print("***** See you later! *****")
        start_reservering = False
        break
    while start_keuze == "3":
        print("***** Login *****")
        catalog.login()
# Menu als je ingelogd bent als gebruiker
        if catalog.loggedInUser.isAdmin() is False:
            while start_reservering_gebruiker:
                print("***** Reserverings systeem *****")
                print("***** Welkom " + catalog.loggedInUser.getFirstName() + " *****")
                start_keuze_gebruiker = input("1) Bekijk boeken \n2) Filter boeken"
                                              " \n3) Reserveer een boek \n4) Logout\n")

                while start_keuze_gebruiker == "1":
                    print("***** Bekijk boeken *****")
                    print("lijst met boeken")
                    start_keuze_gebruiker = input("Press enter to continue")
                while start_keuze_gebruiker == "2":
                    print("***** Filter boeken *****")
                    catalog.filter()
                while start_keuze_gebruiker == "3":
                    print("***** Reserveer een boek *****")
                #     Boek moet hier nog gereserveerd kunnen worden
                if start_keuze_gebruiker == "4":
                    catalog.loggedInUser = None
                    start_keuze = "0"
                    start_reservering_gebruiker = False
        # Menu als je ingelogd bent als admin
        elif catalog.loggedInUser.isAdmin():
                while start_reservering_gebruiker:
                    print("***** Reserverings systeem *****")
                    print("***** Welkom " + catalog.loggedInUser.getFirstName() + " *****")
                    start_keuze_gebruiker = input("1) Bekijk boeken \n2) Filter boeken op titel "
                                                  " \n3) Voeg een boek toe \n4) Voeg een gebruiker toe \n"
                                                  "5) Voeg een gebruiker toe met admin rechten\n6) Logout\n7) "
                                                  "Restore from backup\n8) Save to backup\n")

                    while start_keuze_gebruiker == "1":
                        print("***** Bekijk boeken *****")
                        print("lijst met boeken")
                        start_keuze_gebruiker = input("0) Terug")
                    while start_keuze == "2":
                        print("***** Filter boeken  *****")
                        catalog.filter()
                        start_keuze = input("Press enter to continue.")
                    # nieuw boek toevoegen
                    while start_keuze_gebruiker == "3":
                        print("***** Voeg een boek toe *****")
                        catalog.addBook()
                        start_keuze = input("Press enter to continue.")
# nieuwe gebruiker toevoegen
                    while start_keuze_gebruiker == "4":
                        print("***** Voeg een nieuwe gerbuiker toe *****")
                        catalog.addPerson()
                        start_keuze = "0"
                    while start_keuze_gebruiker == "5":
                        print("***** Voeg een nieuwe gerbuiker toe *****")
                        catalog.addPerson(True)
                        start_keuze = "0"
                    if start_keuze_gebruiker == "6":
                        catalog.loggedInUser = None
                        start_keuze = "0"
                        start_reservering_gebruiker = False
                    if start_keuze_gebruiker == "7":
                        catalog.loggedInUser = None
                        start_keuze = "0"
                        start_reservering_gebruiker = False
                    if start_keuze_gebruiker == "8":
                        catalog.loggedInUser = None
                        start_keuze = "0"
                        start_reservering_gebruiker = False
        elif catalog.loggedInUser is None:
            print("Vul iets in.")
if start_keuze == "4":
    start_reservering = False
