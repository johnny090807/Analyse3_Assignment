from Catalog import Catalog

catalog = Catalog()
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
        print("***** Filter boeken op titel *****")
        catalog.filter()
        start_keuze = input("Press enter to continue.")
    while start_keuze == "3":
        print("***** Login *****")
        catalog.login()
# Menu als je ingelogd bent als gebruiker
        if catalog.loggedInUser is not None:
            while start_reservering_gebruiker:
                print("***** Reserverings systeem *****")
                print("***** Welkom " + catalog.loggedInUser.getFirstName() + " *****")
                start_keuze_gebruiker = input("1) Bekijk boeken \n2) Filter boeken"
                                              " \n3) Reserveer een boek \n4) Logout")

                while start_keuze_gebruiker == "1":
                    print("***** Bekijk boeken *****")
                    print("lijst met boeken")
                    start_keuze_gebruiker = input("0) Terug")
                while start_keuze_gebruiker == "2":
                    print("***** Filter boeken op titel *****")
                    catalog.filter()
                while start_keuze_gebruiker == "3":
                    print("***** Reserveer een boek *****")
                    titel_boek = input("Zoek boek op titel, auteur, leetijd auteur en ISBN")
                    if titel_boek == "naam":
                        print("naam van boek")
                        reserveren_boek = input("1) Reserveer het boek \n0) Reserveer het boek niet")
                        start_keuze_gebruiker = input("6) Zoek opnieuw \n0) Terug naar menu")
                    elif titel_boek == "onbekend":
                        print("titel bestaat niet")
                        start_keuze_gebruiker = input("6) Zoek opnieuw \n0) Terug naar menu")
                if start_keuze_gebruiker == "4":
                    start_keuze = "0"
                    start_reservering_gebruiker = False
# Menu als je ingelogd bent als admin
        elif catalog.loggedInUser.isAdmin():
                while start_reservering_gebruiker:
                    print("***** Reserverings systeem *****")
                    print("***** Welkom " + catalog.loggedInUser.getFirstName() + " *****")
                    start_keuze_gebruiker = input("1) Bekijk boeken \n2) Filter boeken op titel "
                                                  "\n3) Filter boeken op auteursnaam"
                                                  " \n4) Filter boeken op auteurs leeftijd "
                                                  "\n5) Filter boeken op ISBN"
                                                  " \n6) Voeg een boek toe \n7) Voeg een gebruiker toe \n8) Logout")

                    while start_keuze_gebruiker == "1":
                        if start_keuze_gebruiker == "1":
                            print("***** Bekijk boeken *****")
                            print("lijst met boeken")
                            start_keuze_gebruiker = input("0) Terug")
                    while start_keuze_gebruiker == "2":
                        if start_keuze_gebruiker == "2":
                            print("***** Filter boeken op titel *****")
                            titel_boek = input("Zoek boek op titel")
                            if titel_boek == "naam":
                                print("naam van boek")
                                start_keuze_gebruiker = input("2) Zoek opnieuw \n0) Terug naar menu")
                            elif titel_boek == "onbekend":
                                print("titel bestaat niet")
                                start_keuze_gebruiker = input("2) Zoek opnieuw \n0) Terug naar menu")
                    while start_keuze_gebruiker == "3":
                        if start_keuze_gebruiker == "3":
                            print("***** Filter boeken op auteursnaam *****")
                            titel_boek = input("Zoek boek op auteursnaam")
                            if titel_boek == "naam":
                                print("naam van boek")
                                start_keuze_gebruiker = input("3) Zoek opnieuw \n0) Terug naar menu")
                            elif titel_boek == "onbekend":
                                print("titel bestaat niet")
                                start_keuze_gebruiker = input("3) Zoek opnieuw \n0) Terug naar menu")
                    while start_keuze_gebruiker == "4":
                        if start_keuze_gebruiker == "4":
                            print("***** Filter boeken op auteurs leeftijd *****")
                            titel_boek = input("Zoek boek op auteurs leeftijd")
                            if titel_boek == "naam":
                                print("naam van boek")
                                start_keuze_gebruiker = input("4) Zoek opnieuw \n0) Terug naar menu")
                            elif titel_boek == "onbekend":
                                print("titel bestaat niet")
                                start_keuze_gebruiker = input("4) Zoek opnieuw \n0) Terug naar menu")
                    while start_keuze_gebruiker == "5":
                        if start_keuze_gebruiker == "5":
                            print("***** Filter boeken op ISBN *****")
                            titel_boek = input("Zoek boek op ISBN")
                            if titel_boek == "naam":
                                print("naam van boek")
                                start_keuze_gebruiker = input("5) Zoek opnieuw \n0) Terug naar menu")
                            elif titel_boek == "onbekend":
                                print("titel bestaat niet")
                                start_keuze_gebruiker = input("5) Zoek opnieuw \n0) Terug naar menu")
                    # nieuw boek toevoegen
                    while start_keuze_gebruiker == "6":
                        if start_keuze_gebruiker == "6":
                            print("***** Voeg een boek toe *****")
                            new_boek_titel = input("Vul in titel van nieuw boek:")
                            new_boek_auteur = input("Vul in auteur van nieuw boek:")
                            new_boek_leeftijd = input("Vul in leeftijd van auteur:")
                            new_boek_ISBN = input("Vul in ISBN van nieuw boek:")
                            start_keuze_gebruiker = input("6) Opslaan \n0) Terug naar menu")
# nieuwe gebruiker toevoegen
                    while start_keuze_gebruiker == "7":
                        if start_keuze_gebruiker == "7":
                            print("***** Voeg een nieuwe gerbuiker toe *****")
                            new_gebruiker_naam = input("Vul in titel van nieuw boek:")
                            new_gebruiker_wachwoord = input("Vul in auteur van nieuw boek:")
                            start_keuze_gebruiker = input("7) Opslaan \n0) Terug naar menu")
                    if start_keuze_gebruiker == "8":
                        start_reservering_gebruiker = False
        elif catalog.loggedInUser is None:
            print("Vul iets in.")
if start_keuze == "4":
    start_reservering = False
