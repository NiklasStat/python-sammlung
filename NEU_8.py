import numpy as np
import matplotlib.pyplot as plt

# Werte für x im Intervall (0, 1]
x = np.linspace(0.01, 1, 1000)

# Werte für y, initialisieren mit 0
y = np.zeros_like(x)

# Funktion anwenden: f(x) = 1 für x = 1/n für n ∈ ℕ, sonst 0
for n in range(1, 100):
    xn = 1 / n
    y[np.abs(x - xn) < 1e-3] = 1

# Graphen zeichnen
plt.plot(x, y, 'bo', label=r'$f(x)$')
plt.title(r'Graph von $f(x)$ mit Unstetigkeitsstellen 2. Art')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(-0.1, 1.1)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()
