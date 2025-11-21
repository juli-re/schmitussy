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

#21.11.2025

a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.333..
print(a // b) # 3 (Ganzzahldivision)
print(a % b)  # 1 (Rest)
print(a ** b) # 1000 (Potenz)

print(a > b)   # True
print(a == b)  # False

print(a != b)  # True

test = 20

if test % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.") 

for i in range(5):
    print("Freak des Tages: Julian Reiser ", i, " Test")

count = 0
while count < 5:
    print("Count ist:", count)
    count += 1

def freak_des_tages(name):
    print("Freak des Tages ist:", name)

freak_des_tages(person["vorname"])

def addiere(a, b):
    result = a + b
    if (result < 10):
        print("Retard, lern Kopfrechnen")
    else:
        print(result)
        return result
    return 0

addiere(0,110)