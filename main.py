from Book import Book
import csv

start_reservering = True
start_reservering_gebruiker = True
start_keuze = None
while start_reservering or start_keuze == "0":
    # Het menu als je niet bent ingelogd
    print("***** Reserverings systeem *****")
    start_keuze = input("1) Bekijk boeken \n2) Filter boeken op titel \n3) Filter boeken op auteursnaam"
                  " \n4) Filter boeken op auteurs leeftijd \n5) Filter boeken op ISBN \n6) Login \n7) Exit")

    while start_keuze == "1":
        if start_keuze == "1":
            print("***** Bekijk boeken *****")
            print("lijst met boeken")
            start_keuze = input("0) Terug")
    while start_keuze == "2":
        if start_keuze == "2":
            print("***** Filter boeken op titel *****")
            titel_boek = input("Zoek boek op titel")
            if titel_boek == "naam":
                print("naam van boek")
                start_keuze = input("2) Zoek opnieuw \n0) Terug naar menu")
            elif titel_boek == "onbekend":
                print("titel bestaat niet")
                start_keuze = input("2) Zoek opnieuw \n0) Terug naar menu")
    while start_keuze == "3":
        if start_keuze == "3":
            print("***** Filter boeken op auteursnaam *****")
            titel_boek = input("Zoek boek op auteursnaam")
            if titel_boek == "naam":
                print("naam van boek")
                start_keuze = input("3) Zoek opnieuw \n0) Terug naar menu")
            elif titel_boek == "onbekend":
                print("titel bestaat niet")
                start_keuze = input("3) Zoek opnieuw \n0) Terug naar menu")
    while start_keuze == "4":
        if start_keuze == "4":
            print("***** Filter boeken op auteurs leeftijd *****")
            titel_boek = input("Zoek boek op auteurs leeftijd")
            if titel_boek == "naam":
                print("naam van boek")
                start_keuze = input("4) Zoek opnieuw \n0) Terug naar menu")
            elif titel_boek == "onbekend":
                print("titel bestaat niet")
                start_keuze = input("4) Zoek opnieuw \n0) Terug naar menu")
    while start_keuze == "5":
        if start_keuze == "5":
            print("***** Filter boeken op ISBN *****")
            titel_boek = input("Zoek boek op ISBN")
            if titel_boek == "naam":
                print("naam van boek")
                start_keuze = input("5) Zoek opnieuw \n0) Terug naar menu")
            elif titel_boek == "onbekend":
                print("titel bestaat niet")
                start_keuze = input("5) Zoek opnieuw \n0) Terug naar menu")
    while start_keuze == "6":
        if start_keuze == "6":
            print("***** Login *****")
            start_keuze = input("9) Login \n0) Terug naar menu")
            if start_keuze == "9":
                login_naam = input("Naam:")
                login_wachtwoord = input("Wachtwoord:")
            elif start_keuze == "0":
                start_keuze = "0"
    # Menu als je ingelogd bent als gebruiker
                if login_naam == "naam" and login_wachtwoord == "wachtwoord":
                    while start_reservering_gebruiker:
                        print("***** Reserverings systeem *****")
                        print("***** Welkom " + login_naam + "*****")
                        start_keuze_gebruiker = input("1) Bekijk boeken \n2) Filter boeken op titel \n3) Filter boeken op auteursnaam"
                                            " \n4) Filter boeken op auteurs leeftijd \n5) Filter boeken op ISBN"
                                            " \n6) Reserveer een boek \n7) Logout")

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
                        while start_keuze_gebruiker == "6":
                            if start_keuze_gebruiker == "6":
                                print("***** Reserveer een boek *****")
                                titel_boek = input("Zoek boek op titel, auteur, leetijd auteur en ISBN")
                                if titel_boek == "naam":
                                    print("naam van boek")
                                    reserveren_boek = input("1) Reserveer het boek \n0) Reserveer het boek niet")
                                    start_keuze_gebruiker = input("6) Zoek opnieuw \n0) Terug naar menu")
                                elif titel_boek == "onbekend":
                                    print("titel bestaat niet")
                                    start_keuze_gebruiker = input("6) Zoek opnieuw \n0) Terug naar menu")
                        if start_keuze_gebruiker == "7":
                            start_reservering_gebruiker = False
    # Menu als je ingelogd bent als admin
            if login_naam == "admin" and login_wachtwoord == "wachtwoord":
                    print("titel bestaat niet")
                    start_keuze = input("6) Zoek opnieuw \n0) Terug naar menu")
    if start_keuze == "7":
        start_reservering = False
