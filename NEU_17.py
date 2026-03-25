import matplotlib.pyplot as plt
import numpy as np

# Definieren Sie die Funktion
def f(x):
    return (2*x + 3) / np.abs(x + 4)

# Erstellen Sie einen Bereich für x-Werte
x = np.linspace(-10, 10, 400)
y = f(x)

# Bedingung, wann die Ungleichung erfüllt ist
y_condition = y <= 1

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$\frac{2x+3}{|x+4|}$')
plt.fill_between(x, -10, 10, where=y_condition, color='lightgray', alpha=0.5, label=r'$\frac{2x+3}{|x+4|} \leq 1$')
plt.axhline(1, color='red', linestyle='--', label=r'$y=1$')
plt.axvline(-4, color='green', linestyle='--', label=r'$x=-4$')
plt.ylim(-10, 10)  # Begrenzen wir den y-Bereich zur besseren Sichtbarkeit
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Plot von $\frac{2x+3}{|x+4|} \leq 1$')
plt.legend()
plt.grid(True)
plt.show()
