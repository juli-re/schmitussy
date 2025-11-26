def Passwort():
    print("Das Passwort wird erstellt:")
    Passwort = []
    for i in range(12):
        from random import choice
        Zeichen = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        Passwort.append(choice(Zeichen))
    Passwort_str = "".join(Passwort)
    print("Ihr generiertes Passwort lautet:", Passwort_str)

Passwort()