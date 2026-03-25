import numpy as np
import matplotlib.pyplot as plt

# Werte für x definieren, mit Ausnahme von x = 0, um Division durch 0 zu vermeiden
x = np.linspace(-2, 2, 400)
x = x[x != 0]

# Funktion definieren
y = (2 - np.sqrt(4 - x)) / x

# Plot erstellen
plt.plot(x, y, label=r'$\frac{2 - \sqrt{4 - x}}{x}$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.grid(True)
plt.show()
