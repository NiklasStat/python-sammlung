import numpy as np
import matplotlib.pyplot as plt

# Werte für x definieren, Ausschluss von Bereichen, in denen der Nenner 0 wird
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = 1 / (np.sin(x) + np.cos(x))

# Erstellen der Maske für nicht definierte Bereiche
undefined = (np.sin(x) + np.cos(x)) == 0
y[undefined] = np.nan  # Setze undefinierte Werte auf NaN, damit sie nicht geplottet werden

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r"$\frac{1}{\sin(x) + \cos(x)}$", color="blue")
plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
plt.axvline(0, color='black', linewidth=0.5, linestyle="--")

# Begrenze den Bereich für y, um die Darstellung übersichtlicher zu machen
plt.ylim(-10, 10)

# Achsenbeschriftung und Titel
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)
plt.title("Plot der Funktion $f(x) = \\frac{1}{\\sin(x) + \\cos(x)}$", fontsize=14)

# X-Achsen-Ticks in π/2-Schritten
ticks = np.arange(-2 * np.pi, 2.5 * np.pi, np.pi / 2)
tick_labels = [f"{t/np.pi:.1g}π" if t != 0 else "0" for t in ticks]
plt.xticks(ticks, tick_labels)

# Legend und Gitter
plt.legend()
plt.grid(True)
plt.show()
