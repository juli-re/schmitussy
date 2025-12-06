import numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print(arr[0, 1])   # 20
print(arr[:, 1])   # ganze zweite Spalte
print(arr[0, :])   # ganze erste Zeile
print(arr[:, 0:2]) # erste zwei Spalten

a = np.array([1, 2, 3, 4])

print(np.mean(a))   # Durchschnitt
print(np.sum(a))    # Summe
print(np.max(a))    # Maximum

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(A * B)   # elementweise
print(A @ B)   # Matrix-Multiplikation

np.random.seed(0)        # reproduzierbar
np.random.rand(3)        # 3 Zufallszahlen
np.random.randint(0, 10, size=(2, 3))  # 2x3 Array mit Zufallszahlen von 0 bis 9

test = np.arange(10)
test2 = np.arange(0,11,2) 
print(test)
print(test2)
print(np.ones((3,3)))