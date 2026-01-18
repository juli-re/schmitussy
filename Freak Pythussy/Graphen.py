import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(0, 10, 0.1)

#plt.plot(x, np.sin(x), label="sin(x)")
#plt.plot(x, np.cos(x), label="cos(x)")

#plt.title("Einfacher Plot")
#plt.xlabel("X-Achse")
#plt.ylabel("Y-Achse")

#plt.legend()
#plt.show()

#x = np.random.rand(50)
#y = np.random.rand(50)

#plt.scatter(x, y)
#plt.show()

#labels = ["A", "B", "C"]
#values = [5, 7, 3]

#plt.bar(labels, values)
#plt.show()

#data = np.random.randn(1000)

#plt.hist(data, bins=30)
#plt.show()

#plt.plot(x, np.sin(x), color="red", linestyle="--", label="sin(x)")
#plt.legend()
#plt.show()

x = np.linspace(-5, 5, 200)

#plt.figure(figsize=(10, 8))

#plt.subplot(2, 2, 1)
#plt.plot(x, np.sin(x))
#plt.title("sin(x)")

#plt.subplot(2, 2, 2)
#plt.plot(x, np.cos(x))
#plt.title("cos(x)")

#plt.subplot(2, 2, 3)
#plt.plot(x, np.sin(2*x))
#plt.title("sin(2x)")

#plt.subplot(2, 2, 4)
#plt.plot(x, np.cos(2*x))
#plt.title("cos(2x)")
#plt.savefig("plot.png")  # speichert den Plot
plt.show()

plt.plot(x, 3*(x**2), color="black", linestyle="-", label="x^2")
plt.plot(x, x**3, color="blue", linestyle="--", label="x^3")
plt.plot(x, x**4, color="red", linestyle=":", label="x^4")

# Vertikale Linie
plt.axvline(x=0, color='black', linestyle='-')

# Text-Beschriftung
#plt.text(0.1, 0.93, "x = 0", rotation=90, color='black',
#         ha='left', va='center', fontsize=12, transform=plt.gca().get_xaxis_transform())
plt.grid()
plt.legend()
plt.show()