import numpy as np
import matplotlib.pyplot as plt

# Definiere die Stückweise Funktion
def piecewise_function(x):
    if x <= 0:
        return (1 / 1.4) * x + 1
    elif 0 < x <= 3:
        return -0.5 * x + 1
    else:
        return -0.5

# Erstelle Werte für x und y
x_values = np.linspace(-10, 10, 400)
y_values = [piecewise_function(x) for x in x_values]

# Zeichne den Graphen
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Stückweise Funktion')

# Markiere die Bereiche
plt.axvline(0, color='red', linestyle='--', label='x = 0')
plt.axvline(3, color='blue', linestyle='--', label='x = 3')

# Plot-Einstellungen
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Stückweise Funktion')
plt.grid(True)
plt.show()


