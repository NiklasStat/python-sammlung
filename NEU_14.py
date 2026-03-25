import numpy as np
import matplotlib.pyplot as plt

# Definitionsbereich für x
x = np.linspace(-10, 10, 400)
y = (-x + 1) / (-2 * x - 1)

# Bedingung der Ungleichung
condition = np.abs(y) < 2

# Plotten der Graphen
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$\left| \frac{-x + 1}{-2x - 1} \right| < 2$')

# Gültiger Bereich der Ungleichung hervorheben
plt.fill_between(x, y, where=condition, color='lightblue', alpha=0.5)

# Plot-Einstellungen
plt.axhline(2, color='red', linestyle='--', label='y = 2')
plt.axhline(-2, color='red', linestyle='--', label='y = -2')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.ylim(-10, 10)
plt.xlim(-10, 10)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
