#19.11.2025

Test = [0, 1, 4, 3]
print ("servus")
print (Test)
print (type (Test))
for element in Test:
    print(Test[2])

#20.11.2025

person = {"name": "Schmidt", "vorname": "Yannic", "alter": 25}
print (person)
print ("Nachname: " + person["name"])
person2 = {"name": "Reiser", "vorname": "Julian", "alter": 50}
Index = [person, person2]
for x in Index:
    print (x["vorname"])