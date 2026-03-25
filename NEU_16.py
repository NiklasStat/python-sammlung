import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-0.1, 0.1, 400)
y = (1/np.tan(x))**(1/np.log(x))

plt.plot(x, y, label=r'$\left( \frac{1}{\tan(x)} \right)^{\frac{1}{\ln(x)}}$')
plt.axhline(1/np.e, color='red', linestyle='--', label=r'$\frac{1}{e}$')
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Graph von $\left( \frac{1}{\tan(x)} \right)^{\frac{1}{\ln(x)}}$')
plt.legend()
plt.grid(True)
plt.show()
