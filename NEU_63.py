import numpy as np

# Funktion und Ableitung
def function(x):
    return x**2

def gradient(x):
    return 2*x  # Ableitung von f(x) = x^2

# Gradient Descent Parameter
learning_rate = 0.1  # Schrittweite
epochs = 50  # Anzahl der Iterationen
x_start = 10  # Startpunkt

# Initialisierung
x = x_start
history = []  # Speichert den Verlauf der Werte

# Gradient Descent Schleife
for _ in range(epochs):
    history.append(x)  # Verlauf speichern
    x -= learning_rate * gradient(x)  # Aktualisierung: x = x - lr * grad(x)

print("Minimiertes x:", x)
print("Historie:", history)

# Plot Verlauf
import matplotlib.pyplot as plt

plt.plot(history, marker='o', linestyle='-', color='blue')
plt.title("Verlauf von Gradient Descent")
plt.xlabel("Iteration")
plt.ylabel("x-Wert")
plt.grid(True)
plt.show()









