import matplotlib.pyplot as plt
import numpy as np

# Beispieldaten
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = x**2
y5 = np.sqrt(x)

# Subplots erstellen (2 Zeilen, 3 Spalten)
fig, axes = plt.subplots(2, 3, figsize=(12, 8))  # 2x3 Raster

# 1. Plot
axes[0, 0].plot(x, y1, color='blue')
axes[0, 0].set_title("Sin(x)")

# 2. Plot
axes[0, 1].plot(x, y2, color='red')
axes[0, 1].set_title("Cos(x)")

# 3. Plot
axes[0, 2].plot(x, y3, color='green')
axes[0, 2].set_title("Tan(x)")
axes[0, 2].set_ylim(-10, 10)  # Begrenzung für bessere Darstellung

intervals = [0, 10, 30, 50, 100]
probabilities = [0.1, 0.2, 0.3, 0.4]


# Median-Wert
def median_neu(Intervall, Wahrscheinlichkeiten):
    k = 0
    PR_u = 0
    PR_o = 0
    oben = []

    while PR_o < 0.5:
        PR_u = sum(Wahrscheinlichkeiten[:(k-1)])
        PR_o = sum(Wahrscheinlichkeiten[:k])
        print(PR_o)
        if PR_o > 0.5:
            oben = [k-1, Intervall[k]]
            unten = [k-2, Intervall[k-1]]
            median = Intervall[k-1] + (Intervall[k]-Intervall[k-1])*(0.5-PR_u)/(PR_o-PR_u)
            print(unten, oben, PR_u, PR_o)
            return round(median, 2)
        k += 1

median = median_neu(intervals, probabilities)
print(median_neu(intervals, probabilities))


# 4. Plot
axes[1, 0].plot(x, y4, color='purple')
axes[1, 0].set_title("x^2")

# 5. Plot
axes[1, 1].plot(x, y5, color='orange')
axes[1, 1].set_title("Sqrt(x)")

# Leeren Plot entfernen (optional)
axes[1, 2].axis("off")  # Letzter Platz bleibt leer

# Layout anpassen
plt.tight_layout()  # Vermeidet Überlappung
plt.show()