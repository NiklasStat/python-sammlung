import numpy as np
import matplotlib.pyplot as plt

# Definition des Intervalls und der Funktionen
x = np.linspace(0, 2 * np.pi, 1000)
cos_5x = np.cos(5 * x)
cos_2x = np.cos(2 * x)
cos_neg2x = np.cos(-2 * x)
cos_neg5x = np.cos(-5 * x)

# Erstellen der Plots
plt.figure(figsize=(10, 6))
plt.plot(x, cos_5x, label='cos(5x)')
plt.plot(x, cos_2x, label='cos(2x)')
plt.plot(x, cos_neg2x, label='cos(-2x)')
plt.plot(x, cos_neg5x, label='cos(-5x)')

# Anpassen der Plot-Eigenschaften
plt.title('Plots von cos(5x), cos(2x), cos(-2x) und cos(-5x)')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Anpassung der x-Achse in Schritten von π/2
plt.xticks(np.arange(0, 2 * np.pi + np.pi / 2, np.pi / 2),
           [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])

# Anzeigen des Plots
plt.show()
