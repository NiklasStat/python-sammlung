import numpy as np
import matplotlib.pyplot as plt

# Werte für x
x = np.linspace(-10, 10, 400)

# Werte für y
y = np.sinc(x / np.pi)  # np.sinc(x) ist definiert als sin(πx) / (πx) in numpy

# Graphen zeichnen
plt.plot(x, y, label=r'$\frac{\sin(x)}{x}$')
plt.title(r'Graph von $\frac{\sin(x)}{x}$')
plt.xlabel('x')
plt.ylabel(r'$\frac{\sin(x)}{x}$')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()
