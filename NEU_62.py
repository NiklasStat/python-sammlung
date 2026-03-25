from collections import Counter
import matplotlib.pyplot as plt
import random


# Daten
num_friends = [2, 3, 4, 3, 4, 5, 3, 4, 3, 6, 3, 5, 4, 6, 4, 9, 3, 5, 4, 11, 14, 12, 12, 11, 14, 21, 21, 24, 15, 14, 18, 10, 8, 22]
friend_counts = Counter(num_friends)
print(friend_counts)

# Subplots erstellen
fig, axes = plt.subplots(1, 3, figsize=(12, 8))  # 1 Zeile, 3 Spalten

# Histogramm 1
xs = range(25)
ys = [friend_counts[x] for x in xs]
axes[0].bar(xs, ys)
axes[0].set_xlim([0, 25])
axes[0].set_ylim([0, 10])
axes[0].set_title("Histogram of Friend Counts")
axes[0].set_xlabel("# of friends")
axes[0].set_ylabel("# of people")

# Histogramm 2 (zweite Kopie als Beispiel)
axes[1].bar(xs, ys, color='orange')
axes[1].set_xlim([0, 25])
axes[1].set_ylim([0, 10])
axes[1].set_title("Histogram of Friend Counts (Copy)")
axes[1].set_xlabel("# of friends")
axes[1].set_ylabel("# of people")

# Leerer Platz
axes[2].axis("off")  # Letzter Platz bleibt leer

# Layout anpassen
plt.tight_layout()  # Vermeidet Überlappung
plt.show()




def coin_flip(Anzahl, p):
    def bernoulli_trial(p):
        # Gibt 1 mit Wahrscheinlichkeit p, sonst 0
        return 1 if random.random() < p else 0

    paare = []
    liste_k = []
    k = []
    for i in range(1, Anzahl + 1):
        paare.append(bernoulli_trial(p))
        k.append(sum(paare) / i)
        liste_k.append(i)
    return k, liste_k


print(coin_flip(10, 0.5))


# Beispielpunkte (x, y)


# Erstelle den Plot

fig, axes = plt.subplots(2, 2, figsize=(12, 8))  # 1 Zeile, 3 Spalten

fig.suptitle("Gesamttitel für alle Subplots", fontsize=16)



y, x = coin_flip(10000, 0.5)[0], coin_flip(10000, 0.5)[1]

axes[0,0].plot(x, y, marker='o', linestyle='-', color='blue', markersize=0.6, linewidth=0.5)

# Achsentitel und Beschriftungen
axes[0,0].set_title("Polygonzug mit verbundenen Punkten")
axes[0,0].set_xlabel("x-Werte")
axes[0,0].set_ylabel("y-Werte")
axes[0,0].grid(True)

# Zeige den Plot
plt.grid(True)  # Optionale Gitterlinien

y, x = coin_flip(10000, 0.4)[0], coin_flip(10000, 0.5)[1]

axes[0,1].plot(x, y, marker='o', linestyle='-', color='grey', markersize=0.6, linewidth=0.5)

# Achsentitel und Beschriftungen
axes[0,1].set_title("Polygonzug mit verbundenen Punkten")
axes[0,1].set_xlabel("x-Werte")
axes[0,1].set_ylabel("y-Werte")
axes[0,1].grid(True)

# Zeige den Plot
plt.grid(True)  # Optionale Gitterlinien

y, x = coin_flip(10000, 0.3)[0], coin_flip(10000, 0.5)[1]

axes[1,0].plot(x, y, marker='o', linestyle='-', color='green', markersize=0.6, linewidth=0.5)

# Achsentitel und Beschriftungen
axes[1,0].set_title("Polygonzug mit verbundenen Punkten")
axes[1,0].set_xlabel("x-Werte")
axes[1,0].set_ylabel("y-Werte")
axes[1,0].grid(True)

# Zeige den Plot
plt.grid(True)  # Optionale Gitterlinien

y, x = coin_flip(10000, 0.2)[0], coin_flip(10000, 0.5)[1]

axes[1,1].plot(x, y, marker='o', linestyle='-', color='red', markersize=0.6, linewidth=0.5)

# Achsentitel und Beschriftungen
axes[1,1].set_title("Polygonzug mit verbundenen Punkten")
axes[1,1].set_xlabel("x-Werte")
axes[1,1].set_ylabel("y-Werte")
axes[1,1].grid(True)




# Layout anpassen
plt.tight_layout()  # Vermeidet Überlappung
plt.show()