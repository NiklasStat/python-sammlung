import matplotlib.pyplot as plt
import numpy as np

# Definieren Sie die Funktion
def f(x):
    return np.abs(3*x - 2) / (x + 2)

# Erstellen Sie einen Bereich für x-Werte
x = np.linspace(-10, 10, 400)
y = f(x)

# Bedingung, wann die Ungleichung erfüllt ist
y_condition = y >= 2

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$\frac{|3x - 2|}{x + 2}$')
plt.fill_between(x, -10, 10, where=y_condition, color='lightgray', alpha=0.5, label=r'$\frac{|3x - 2|}{x + 2} \geq 2$')
plt.axhline(2, color='red', linestyle='--', label=r'$y=2$')
plt.ylim(-5, 15)  # Begrenzen wir den y-Bereich zur besseren Sichtbarkeit
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Plot von $\frac{|3x - 2|}{x + 2} \geq 2$')
plt.legend()
plt.grid(True)
plt.show()
