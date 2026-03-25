import numpy as np
import matplotlib.pyplot as plt

# Definieren der Funktion f(x)
def f(x):
    return -1 / np.cbrt(x) * np.log(1 / (x + 1))

# Werte für x (ohne 0, um Division durch 0 zu vermeiden)
x = np.linspace(-2, 10, 400)
x = x[x != 0]

# Berechnen der y-Werte
y = f(x)

# Graphen zeichnen
plt.plot(x, y, label=r'$f(x) = \frac{-1}{\sqrt[3]{x}} \ln\left(\frac{1}{x+1}\right)$')
plt.title(r'Graph von $f(x) = \frac{-1}{\sqrt[3]{x}} \ln\left(\frac{1}{x+1}\right)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
