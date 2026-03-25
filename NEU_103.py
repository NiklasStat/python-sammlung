import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ReLU-Funktion
def relu(x):
    return np.maximum(0, x)

# X-Bereich
x = np.linspace(-10, 10, 400)

# Startwerte
a0 = 1
b0 = 0

# Plot vorbereiten
fig, ax = plt.subplots(figsize=(8, 5))
plt.subplots_adjust(left=0.1, bottom=0.25)

y = relu(a0 * x + b0)
(line,) = ax.plot(x, y, lw=2)

ax.set_xlabel("x")
ax.set_ylabel("ReLU(a·x + b)")
ax.set_title("Interaktive ReLU-Funktion mit a- und b-Regler")
ax.grid(True)

# Slider-Achsen
ax_a = plt.axes([0.1, 0.15, 0.8, 0.03])
ax_b = plt.axes([0.1, 0.1, 0.8, 0.03])

# Slider erstellen
slider_a = Slider(ax_a, "a", -5.0, 5.0, valinit=a0)
slider_b = Slider(ax_b, "b", -5.0, 5.0, valinit=b0)

# Update-Funktion
def update(val):
    a = slider_a.val
    b = slider_b.val
    line.set_ydata(relu(a * x + b))
    fig.canvas.draw_idle()

slider_a.on_changed(update)
slider_b.on_changed(update)

plt.show()