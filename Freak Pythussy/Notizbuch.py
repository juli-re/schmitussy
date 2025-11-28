def NotizbuchSchreiben (Notiz):
    empty = False
    with open("Notizbuch.txt", "r") as file:
        content = file.read()
        if(content == ""):
            empty = True
        print("Bisher steht das in der Datei: ", content)
    with open("Notizbuch.txt", "w") as file:
        if(empty):
            file.write(Notiz)
        else:
            einfügen = content + "\n" + Notiz
            file.write(einfügen)
    with open("Notizbuch.txt", "r") as file:
        content = file.read()
        print("Jetzt steht das in der Datei: ", content)

modus = input("Willkommen im Notizbuch! Was soll gemacht werden? (Lesen/Schreiben/Löschen) ").lower()
if(modus == "lesen"):
    with open("Notizbuch.txt", "r") as file:
        content = file.read()
        print("Das steht in der Datei: ", content)
elif(modus == "schreiben"):
    NotizbuchSchreiben(input("Was soll geschrieben werden? "))
elif(modus == "löschen"):
    with open("Notizbuch.txt", "w") as file:
        file.write("")
    print("Die Datei wurde geleert.")
else:
    print("Ungültiger Modus ausgewählt.")