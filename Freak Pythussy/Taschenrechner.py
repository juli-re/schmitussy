#25.11.2025

def Taschenrechner():
    print("Willkommen zum Taschenrechner!")
    eins = input ("Bitte erste Zahl eingeben: ")
    zeichen = input("Welche Operation soll ausgeführt werden?\n(+/-/*///%/**): ")
    zwei = input("Bitte zweite Zahl eingeben: ")
    if (zeichen == "+"):
        ergebnis = int(eins) + int(zwei)
        print("Ihre Aufgabe war:", eins, zeichen, zwei, "\nUnd das Ergebnis war:", ergebnis)
    elif (zeichen == "-"):
        ergebnis = int(eins) - int(zwei)
        print("Ihre Aufgabe war:", eins, zeichen, zwei, "\nUnd das Ergebnis war:", ergebnis)
    elif (zeichen == "*"):
        ergebnis = int(eins) * int(zwei)
        print("Ihre Aufgabe war:", eins, zeichen, zwei, "\nUnd das Ergebnis war:", ergebnis)
    elif (zeichen == "/"):
        if(zwei == "0"):
            print("Fehler: Division durch Null ist nicht erlaubt.")
            return
        else:
            ergebnis = int(eins) / int(zwei)
            print("Ihre Aufgabe war:", eins, zeichen, zwei, "\nUnd das Ergebnis war:", ergebnis)
    elif (zeichen == "%"):
        ergebnis = int(eins) % int(zwei)
        print("Ihre Aufgabe war:", eins, zeichen, zwei, "\nUnd das Ergebnis war:", ergebnis)
    elif (zeichen == "**"):
        ergebnis = int(eins) ** int(zwei)
        print("Ihre Aufgabe war:", eins, zeichen, zwei, "\nUnd das Ergebnis war:", ergebnis)


Taschenrechner()