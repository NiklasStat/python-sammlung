# Python Code Sammlung
Generiert am: 2026-03-25 16:23:54.642836

## NEU60.py

### Code
```python
from collections import Counter
import matplotlib.pyplot as plt
import math
from statistics import variance
import random
import numpy as np



num_friends = [2, 3, 4, 3, 4, 5, 3, 4, 3, 6, 3, 5, 4, 6, 4, 9, 3, 5, 4, 11, 14, 12, 12, 11, 14, 21, 21, 24, 15, 14, 18, 10, 8, 22]
friend_counts = Counter(num_friends)
print(friend_counts)

fig, axes = plt.subplots(2, 3, figsize=(12, 8))  # 2x3 Raster



xs = range(25)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 25, 0, 10])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

laenge, maxi, mini, kleinste, groesste = len(num_friends), max(num_friends), min(num_friends), sorted(num_friends)[0], sorted(num_friends)[-1]
print(laenge, maxi, mini, kleinste, groesste)

def mean(x):
    return sum(x)/len(x)

print(mean(num_friends))

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n//2
    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

print(median(num_friends))

def mode(x):
    counts = Counter(x)
    print(counts)
    max_count = max(counts.values())
    print(max_count)
    print("_____________")
    print(counts.keys())
    print(counts.values())
    print(counts.items())
    print("____________")
    return [x_i for x_i, count in counts.items()
    if count == max_count]

print(mode(num_friends))

def standard_deviation(x):
    return math.sqrt(variance(x))
print(standard_deviation(num_friends))

def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
plt.plot(xs,[normal_pdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
plt.legend()
plt.title("Various Normal pdfs")
plt.show()

def normal_cdf(x, mu=0,sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
plt.plot(xs,[normal_cdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
plt.legend(loc=4) # bottom right
plt.title("Various Normal cdfs")
plt.show()

print("________")
# find approximate inverse using binary search
# if not standard, compute standard and rescale
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z, low_p = -10.0, 0 # normal_cdf(-10) is (very close to) 0
    hi_z, hi_p = 10.0, 1 # normal_cdf(10) is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2 # consider the midpoint
        mid_p = normal_cdf(mid_z) # and the cdf's value there
        if mid_p < p:
    # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
    # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z

print(inverse_normal_cdf(0.6, mu=0, sigma=1, tolerance=0.00001))

print("_________--------")
print(random.random())
print(random.random())
print(random.random())

def bernoulli_trial(p):
    return 1 if random.random() < p else 0
def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

print("NNNNNNNNNNNNNNNNNNNN")
print(binomial(10, 0.3))


def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]
 # use a bar chart to show the actual binomial samples
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
    [v / num_points for v in histogram.values()],
     0.8,
    color='0.75')
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))
 # use a line chart to show the normal approximation
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
    for i in xs]
    plt.plot(xs,ys)
    plt.title("Binomial Distribution vs. Normal Approximation")
    plt.show()

make_hist(0.4, 10, 100)





# Klassenintervalle und Wahrscheinlichkeiten
intervals = [0, 10, 30, 50, 100]
probabilities = [0.1, 0.2, 0.3, 0.4]

# Berechnung der Höhen (Höhe = Fläche / Breite des Intervalls)
widths = [intervals[i+1] - intervals[i] for i in range(len(intervals)-1)]
heights = [prob / width for prob, width in zip(probabilities, widths)]

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


# Histogramm zeichnen
plt.bar(intervals[:-1], heights, width=widths, align='edge', edgecolor='black', alpha=0.7)

# Wahrscheinlichkeiten in die Balken schreiben
for i in range(len(heights)):
    x_position = intervals[i] + widths[i] / 2  # Mittelpunkt des Balkens
    plt.text(x_position, heights[i] / 2, f"{probabilities[i]:.1f}", ha='center', va='center', color='black', fontsize=10)

# Klassenintervalle unter die x-Achse schreiben
plt.xticks(intervals, labels=[f"{intervals[i]}" for i in range(len(intervals))])

# Median als gestrichelte Linie einzeichnen
plt.axvline(x=median, color='red', linestyle='--', linewidth=2, label=f'Median = {median}')
plt.legend()

# Achsentitel und Beschriftungen
plt.xlabel('Intervalle')
plt.ylabel('Höhe (Dichte)')
plt.title('Histogramm mit Median als gestrichelte Linie')

# Zeige das Diagramm
plt.show()









```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU60.py", line 2, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

```

## NEU_1.py

### Code
```python
k = 2
N = 0
while True:
    Zahlen = [x for x in range(2, k)
              if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]
    if len(Zahlen) < 11:
        k = k + 1
        N = len(Zahlen)
    else: break

print("_____")
print(N)
print(Zahlen)
print(k)

k = 2
N = 0
while True:
    Zahlen = [x for x in range(2, k)
              if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]
    k = k + 1
    if len(Zahlen) == 50:
        N = len(Zahlen)
        break

print("_____")
print(N)
print(Zahlen)
print(Zahlen[-1])
print(f"Es gibt insgesamt {N} Primzahlen, und die 50. lautet {Zahlen[-1]}.")


wort = "Autobahnbrücke"
print(wort.lower())
buchstaben_liste = [buchstabe for buchstabe in wort.lower()]
print(set(buchstaben_liste))
test = {i: wort.lower().count(i) for i in wort.lower()} # ist set deshalb automatisch für i jeder buchstabe nur einmal
print(test)

text = ("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
        "sed diam nonumy eirmod tempor invidunt ut labore et dolore"
        " magna aliquyam erat, sed diam voluptua. At vero eos et "
        "accusam et justo duo dolores et ea rebum. Stet clita kasd "
        "gubergren, no sea takimata sanctus est Lorem ipsum dolor "
        "sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing "
        "elitr, sed diam nonumy eirmod tempor invidunt ut labore "
        "et dolore magna aliquyam erat, sed diam voluptua. "
        "At vero eos et accusam et justo duo dolores et ea rebum. "
        "Stet clita kasd gubergren, no sea takimata sanctus est"
        " Lorem ipsum dolor sit amet.")

print(text)

buchstaben_liste_2 = [buchstabe for buchstabe in text.lower() if buchstabe.isalpha()]
test_2 = {i: buchstaben_liste_2.count(i) for i in set(buchstaben_liste_2)} # ist set deshalb automatisch für i jeder buchstabe nur einmal
print(test_2)


import matplotlib.pyplot as plt

# Der Text, den du analysieren möchtest
text = "Autobahnbrücke"

# Buchstaben aus dem Text filtern und zählen
buchstaben_liste = [buchstabe for buchstabe in text.lower() if buchstabe.isalpha()]
buchstaben_haeufigkeit = {i: buchstaben_liste.count(i) for i in set(buchstaben_liste)}

# Daten für das Diagramm vorbereiten
buchstaben = sorted(test_2.keys())
haeufigkeiten = list(test_2.values())

# Diagramm erstellen
plt.bar(buchstaben, haeufigkeiten)
plt.xlabel('Buchstaben')
plt.ylabel('Häufigkeit')
plt.title('Häufigkeit der Buchstaben in "lorem ip..."')
plt.show()

```

### Ausgabe
```
_____
10
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
32
_____
50
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
229
Es gibt insgesamt 50 Primzahlen, und die 50. lautet 229.
autobahnbrücke
{'ü', 'n', 'h', 'u', 'o', 't', 'a', 'e', 'c', 'b', 'r', 'k'}
{'a': 2, 'u': 1, 't': 1, 'o': 1, 'b': 2, 'h': 1, 'n': 1, 'r': 1, 'ü': 1, 'c': 1, 'k': 1, 'e': 1}
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
{'v': 6, 'q': 2, 'n': 20, 'y': 4, 'p': 10, 'j': 2, 'a': 46, 'c': 12, 'l': 22, 'k': 4, 'm': 32, 'u': 30, 'r': 32, 'i': 30, 'd': 26, 'g': 8, 'e': 56, 's': 38, 'o': 42, 't': 50, 'b': 6}

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_1.py", line 59, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

```

## NEU_10.py

### Code
```python
import numpy as np
import matplotlib.pyplot as plt

# Definieren der Funktion f(x)
def f(x):
    return -1 / np.cbrt(x) * np.log(1 / (x + 1))

# Werte für x (ohne 0, um Division durch 0 zu vermeiden)
x = np.linspace(-1, 1, 400)
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

# Zeichne einen roten Kreis um (0, 0)
circle = plt.Circle((0, 0), 0.05, color='red', fill=False)
plt.gca().add_artist(circle)

plt.show()

```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_10.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

```

## NEU_101.py

### Code
```python
import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.linear_model import BayesianRidge

# 1. Beispiel-Daten mit fehlenden Werten
df = pd.DataFrame({
    "Alter": [25, 30, np.nan, 45, 50],
    "Einkommen": [3000, np.nan, 3500, 5000, 5200],
    "Arbeitsstunden": [40, 38, 42, np.nan, 45]
})

print("Rohdaten:")
print(df)

# 2. MICE-Imputer definieren
imputer = IterativeImputer(
    estimator=BayesianRidge(),
    max_iter=10,
    random_state=42
)

# 3. Daten imputieren
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print("\nNach MICE-Imputation:")
print(df_imputed)


```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_101.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

```

## NEU_102.py

### Code
```python
import tensorflow as tf
import numpy as np

# Beispiel-Daten (fiktiv):
# Features: [xG_home, xG_away, shots_home, shots_away, possession_home]
X = np.array([
    [1.8, 0.9, 15, 8, 55],
    [0.7, 1.5, 7, 14, 42],
    [1.2, 1.2, 10, 10, 50],
    [2.1, 0.5, 18, 6, 60],
    [0.5, 1.8, 5, 16, 38],
    [1.4, 1.0, 12, 9, 52]
], dtype=np.float32)

# Labels: 0 = Niederlage, 1 = Unentschieden, 2 = Sieg
y = np.array([2, 0, 1, 2, 0, 2])

# One-hot-Encoding
y_onehot = tf.keras.utils.to_categorical(y, num_classes=3)

# Modell definieren
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(5,)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Training
history = model.fit(X, y_onehot, epochs=50, verbose=0)

# Beispielvorhersage
sample = np.array([[1.6, 0.8, 14, 7, 57]], dtype=np.float32)
prediction = model.predict(sample)

classes = ["Loss", "Draw", "Win"]
print("Prediction probabilities:", prediction)
print("Predicted outcome:", classes[np.argmax(prediction)])

```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_102.py", line 1, in <module>
    import tensorflow as tf
ModuleNotFoundError: No module named 'tensorflow'

```

## NEU_103.py

### Code
```python
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
```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_103.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

```

## NEU_104.py

### Code
```python
import math

# Aktivierungsfunktionen
def relu(z):
    return max(0, z)

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Vorwärtsfunktion
def forward(x1, x2):
    # Gewichte und Biases
    w11, w21 = 0.031, -0.2
    w12, w22 = 0.043, -0.02
    b1, b2 = 0.01, -0.01
    wh1, wh2 = 0.05, 0.031
    by = -0.02

    # Hidden Layer
    z1 = x1 * w11 + x2 * w21 + b1
    z2 = x1 * w12 + x2 * w22 + b2
    h1 = relu(z1)
    h2 = relu(z2)

    # Output Layer
    zy = h1 * wh1 + h2 * wh2 + by
    y_hat = sigmoid(zy)

    return y_hat

# Kreuzentropie
def cross_entropy(y, y_hat):
    # numerische Stabilität
    eps = 1e-12
    y_hat = min(max(y_hat, eps), 1 - eps)
    return -(y * math.log(y_hat) + (1 - y) * math.log(1 - y_hat))


# Beispielwerte
x1 = 99.1
x2 = 90
y = 1

y_hat = forward(x1, x2)
loss = cross_entropy(y, y_hat)

print("y_Dach =", y_hat)
print("Kreuzentropie =", loss)

import matplotlib.pyplot as plt
import networkx as nx

# Gewichte und Biases
w11, w21 = 0.031, -0.2
w12, w22 = 0.043, -0.02
b1, b2 = 0.01, -0.01
wh1, wh2 = 0.05, 0.031
by = -0.02

G = nx.DiGraph()

# Knoten
G.add_node("x1")
G.add_node("x2")
G.add_node("b1")
G.add_node("b2")
G.add_node("h1\nReLU")
G.add_node("h2\nReLU")
G.add_node("by")
G.add_node("ŷ\nSigmoid")

# Kanten Input → Hidden
G.add_edge("x1", "h1\nReLU", weight=w11)
G.add_edge("x2", "h1\nReLU", weight=w21)
G.add_edge("x1", "h2\nReLU", weight=w12)
G.add_edge("x2", "h2\nReLU", weight=w22)

# Bias → Hidden
G.add_edge("b1", "h1\nReLU", weight=b1)
G.add_edge("b2", "h2\nReLU", weight=b2)

# Hidden → Output
G.add_edge("h1\nReLU", "ŷ\nSigmoid", weight=wh1)
G.add_edge("h2\nReLU", "ŷ\nSigmoid", weight=wh2)

# Bias → Output
G.add_edge("by", "ŷ\nSigmoid", weight=by)

# Positionen
pos = {
    "x1": (-2, 1.2),
    "x2": (-2, -1.2),

    "b1": (-1, 3),
    "b2": (-1, -3),

    "h1\nReLU": (0, 1.2),
    "h2\nReLU": (0, -1.2),

    "by": (1, 3),
    "ŷ\nSigmoid": (2, 0)
}

plt.figure(figsize=(13, 8))

# Gerade Kanten zeichnen
nx.draw_networkx_edges(G, pos, arrows=True)

# Knoten zeichnen
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color="#D0E4FF")
nx.draw_networkx_labels(G, pos, font_size=10)

# Gewichtslabels manuell versetzen
for (u, v, d) in G.edges(data=True):
    x1, y1 = pos[u]
    x2, y2 = pos[v]

    # Position des Labels (Mitte der Linie)
    lx = (x1 + x2) / 2
    ly = (y1 + y2) / 2

    # Seitlicher Offset abhängig von der Richtung
    offset = 0.15 if u == "x1" and v == "h2\nReLU" else \
             -0.15 if u == "x2" and v == "h1\nReLU" else 0

    plt.text(
        lx + offset, ly,
        f"{d['weight']}",
        color="red",
        fontsize=10,
        bbox=dict(facecolor="white", edgecolor="none", pad=1)
    )

plt.title("Neuronales Netzwerk – gerade Linien, überlappungsfreie Gewichtslabels")
plt.axis("off")
plt.show()

#------------------------------

def relu(z):
    return max(0, z)

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def tanh(z):
    return math.tanh(z)

def forward(x1, x2, activation="relu"):
    # Gewichte und Biases
    w11, w21 = 0.031, -0.2
    w12, w22 = 0.043, -0.02
    b1, b2 = 0.01, -0.01
    wh1, wh2 = 0.05, 0.031
    by = -0.02

    # Aktivierungsfunktion wählen
    if activation == "relu":
        act = relu
    elif activation == "tanh":
        act = tanh
    elif activation == "sigmoid":
        act = sigmoid
    else:
        raise ValueError("Unbekannte Aktivierungsfunktion")

    # Hidden Layer
    z1 = x1 * w11 + x2 * w21 + b1
    z2 = x1 * w12 + x2 * w22 + b2
    h1 = act(z1)
    h2 = act(z2)

    # Output Layer
    zy = h1 * wh1 + h2 * wh2 + by
    y_hat = sigmoid(zy)

    return y_hat

# Beispiel
x1 = 99.1
x2 = 90

print("ReLU:", forward(x1, x2, "relu"))
print("tanh:", forward(x1, x2, "tanh"))
print("sigmoid:", forward(x1, x2, "sigmoid"))
```

### Ausgabe
```
y_Dach = 0.513993919380205
Kreuzentropie = 0.6655438435965481

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_104.py", line 50, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

```

## NEU_105.py

### Code
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Anzahl der Punkte
n = 1000

# Zufällige Punkte im gewünschten Bereich
x1 = np.random.uniform(-5, 5, n)
x2 = np.random.uniform(0, 10, n)

# Herz skalieren und verschieben:
# Standardherz liegt ungefähr in y ∈ [-1.3, 1.3]
# Wir skalieren um Faktor 3 und verschieben um +4
# Ergebnis: Herz liegt in x2 ∈ [0, 8]
X = x1 / 3
Y = (x2 - 4) / 3

# Herzgleichung
heart = (X**2 + Y**2 - 1)**3 - X**2 * Y**3

# y = 1 wenn im Herz, sonst 0
y = (heart <= 0).astype(int)

# DataFrame
df = pd.DataFrame({"x1": x1, "x2": x2, "y": y})

print(df.head())

# Plot
plt.figure(figsize=(8, 10))

# Hintergrundpunkte (y=0)
plt.scatter(df[df.y == 0].x1, df[df.y == 0].x2,
            color="black", s=10, alpha=0.5, label="y = 0")

# Herzpunkte (y=1)
plt.scatter(df[df.y == 1].x1, df[df.y == 1].x2,
            color="red", s=10, alpha=0.8, label="y = 1")

plt.title("Herzförmiger Datensatz (n = 1000)")
plt.xlabel("x1")
plt.ylabel("x2")
plt.ylim(0, 10)
plt.legend()
plt.grid(True)
plt.show()

import torch
import torch.nn as nn

class HeartNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(2, 16),
            nn.Tanh(),
            nn.Linear(16, 8),
            nn.Tanh(),
            nn.Linear(8, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x)

net = HeartNet()
loss_fn = nn.BCELoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.001)




# 1000 Punkte erzeugen
n = 1000
x1 = np.random.uniform(-5, 5, n)
x2 = np.random.uniform(0, 10, n)

# Herz skalieren
X = x1 / 3
Y = (x2 - 4) / 3

heart = (X**2 + Y**2 - 1)**3 - X**2 * Y**3
y = (heart <= 0).astype(int)

#----------------



X_data = torch.tensor(np.column_stack((x1, x2)), dtype=torch.float32)
y_data = torch.tensor(y.reshape(-1, 1), dtype=torch.float32)

# Netz lernt Herzform

epochs = 2000

for epoch in range(epochs):
    optimizer.zero_grad()

    y_pred = net(X_data)
    loss = loss_fn(y_pred, y_data)

    loss.backward()
    optimizer.step()

    if epoch % 200 == 0:
        print(f"Epoch {epoch}, Loss = {loss.item():.4f}")

# Vorhersagen

with torch.no_grad():
    preds = net(X_data)
    preds = (preds > 0.5).int()


# Ergebnisse visualisieren



plt.scatter(x1[preds[:,0]==0], x2[preds[:,0]==0], color="black", s=10)
plt.scatter(x1[preds[:,0]==1], x2[preds[:,0]==1], color="red", s=10)
plt.show()




# 10 Testpunkte erzeugen
x1_test = np.linspace(-5, 5, 10)
x2_test = np.linspace(0, 10, 10)
test_points = np.column_stack((x1_test, x2_test))

# In Tensor umwandeln
test_tensor = torch.tensor(test_points, dtype=torch.float32)

# Vorhersage
with torch.no_grad():
    probs = net(test_tensor).numpy().flatten()

print("Wahrscheinlichkeiten:")
for (x1, x2), p in zip(test_points, probs):
    print(f"({x1:.1f}, {x2:.1f}) -> {float(p):.4f}")



# Herz-Datensatz zeichnen (schwarz + rot)
plt.figure(figsize=(8, 10))
plt.scatter(df[df.y == 0].x1, df[df.y == 0].x2, color="black", s=10, alpha=0.5, label="y = 0")
plt.scatter(df[df.y == 1].x1, df[df.y == 1].x2, color="red",   s=10, alpha=0.8, label="y = 1")

# Gelbe Testpunkte
plt.scatter(x1_test, x2_test, color="yellow", s=120, edgecolors="black", label="Testpunkte")

# Wahrscheinlichkeiten an die Punkte schreiben
for (x1, x2, p) in zip(x1_test, x2_test, probs):
    plt.text(x1 + 0.1, x2 + 0.1, f"{p:.2f}", color="blue", fontsize=10)

plt.legend()
plt.xlabel("x1")
plt.ylabel("x2")
plt.ylim(0, 10)
plt.grid(True)
plt.show()




#----------------------------------------

def visualize_layer(model, layer_index, num_neurons, title_prefix):
    xs = np.linspace(-1.5, 1.5, 300)
    ys = np.linspace(-1.5, 1.5, 300)
    grid = np.array([[x, y] for x in xs for y in ys], dtype=np.float32)
    grid_t = torch.tensor(grid)

    # Forward bis Layer 1
    with torch.no_grad():
        out1 = model.model[0](grid_t)   # Linear 2->16
        out1 = model.model[1](out1)     # Tanh

        if layer_index == 1:
            out2 = model.model[2](out1)  # Linear 16->8
            out2 = model.model[3](out2)  # Tanh

    # Plot-Grid vorbereiten
    cols = 4
    rows = (num_neurons + cols - 1) // cols
    plt.figure(figsize=(12, 3 * rows))

    for i in range(num_neurons):
        plt.subplot(rows, cols, i + 1)

        if layer_index == 0:
            activ = out1[:, i]
        else:
            activ = out2[:, i]

        activ = activ.reshape(len(xs), len(ys))

        plt.imshow(
            activ.numpy(),
            extent=(-1.5, 1.5, -1.5, 1.5),
            origin='lower',
            cmap='inferno'
        )
        plt.title(f"{title_prefix} Neuron {i}")
        plt.axis("off")

    plt.tight_layout()
    plt.show()


# ---- Aufruf für ALLE Neuronen ----

# Layer 1: 16 Neuronen
visualize_layer(net, layer_index=0, num_neurons=16, title_prefix="Layer 1")

# Layer 2: 8 Neuronen
visualize_layer(net, layer_index=1, num_neurons=8, title_prefix="Layer 2")
```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_105.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

```

## NEU_106.py

### Code
```python
import torch
import numpy as np
import matplotlib.pyplot as plt

def visualize_layer(model, layer_index, num_neurons, title_prefix):
    xs = np.linspace(-1.5, 1.5, 300)
    ys = np.linspace(-1.5, 1.5, 300)
    grid = np.array([[x, y] for x in xs for y in ys], dtype=np.float32)
    grid_t = torch.tensor(grid)

    # Forward bis Layer 1
    with torch.no_grad():
        out1 = model.model[0](grid_t)   # Linear 2->16
        out1 = model.model[1](out1)     # Tanh

        if layer_index == 1:
            out2 = model.model[2](out1)  # Linear 16->8
            out2 = model.model[3](out2)  # Tanh

    # Plot-Grid vorbereiten
    cols = 4
    rows = (num_neurons + cols - 1) // cols
    plt.figure(figsize=(12, 3 * rows))

    for i in range(num_neurons):
        plt.subplot(rows, cols, i + 1)

        if layer_index == 0:
            activ = out1[:, i]
        else:
            activ = out2[:, i]

        activ = activ.reshape(len(xs), len(ys))

        plt.imshow(
            activ.numpy(),
            extent=(-1.5, 1.5, -1.5, 1.5),
            origin='lower',
            cmap='inferno'
        )
        plt.title(f"{title_prefix} Neuron {i}")
        plt.axis("off")

    plt.tight_layout()
    plt.show()


# ---- Aufruf für ALLE Neuronen ----

# Layer 1: 16 Neuronen
visualize_layer(net, layer_index=0, num_neurons=16, title_prefix="Layer 1")

# Layer 2: 8 Neuronen
visualize_layer(net, layer_index=1, num_neurons=8, title_prefix="Layer 2")
```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_106.py", line 1, in <module>
    import torch
ModuleNotFoundError: No module named 'torch'

```

## NEU_11.py

### Code
```python



while True:
   # eingabe = input("Zahl: ")
    eingabe = 44

    try:
        ergebnis = 100 / float(eingabe)


    except ZeroDivisionError:
        print("Durch 0 geteilt")
    except ValueError:
        print("Du hast keine gültige Zahl eingegeben")
    except:
        print("Irgendein Fehler")

    else:
        print(ergebnis)
        break



while True:
    eingabe = "ff"
    try:
        ergebnis = 1/int(eingabe)
    except:
        print("Fehler, Feierabend!")
        break  # oder continue
    else:
        print(ergebnis)
        break
    finally:
        print("Ich räume hier auf")
    print("Programm geht weiter")
```

### Ausgabe
```
2.272727272727273
Fehler, Feierabend!
Ich räume hier auf

```

## NEU_12.py

### Code
```python
""" Das ist ein Modul zum ausprobieren.
"""
def fkt(vektor):
    ''' Diese Funktion nimmt das erste Zeichen. '''
    k = vektor[0]
    return k

if __name__ == '__main__':
    print("Ich wurde direkt aufgerufen.")
    #zu_pruefen = input("Vektor?")
    zu_pruefen = [5, 22]
    print(fkt(zu_pruefen))
else:
    print(f"Ich wurde als Modul {__name__} eingebunden")

print(fkt([6,7,8]))
print("___")


faktor = 10
letztes_ergebnis = None
def wert_mal_faktor(wert):
    global letztes_ergebnis
    letztes_ergebnis = wert * faktor
    return letztes_ergebnis

print(wert_mal_faktor(2))
print(letztes_ergebnis)
```

### Ausgabe
```
Ich wurde direkt aufgerufen.
5
6
___
20
20

```

## NEU_13.py

### Code
```python
import NEU_12 # import NEU_12 as N12
help(NEU_12)
print(NEU_12.fkt([6,7,8]))

print(NEU_12.wert_mal_faktor(7))
print(NEU_12.faktor)
NEU_12.faktor = 20
print(NEU_12.wert_mal_faktor(7))
print(NEU_12.letztes_ergebnis)
print("---------")
from random import uniform as mit_komma, randint
zufallszahl = mit_komma(1, 10)
print(randint(1, 10))

import pandas as pd
import numpy as np

# Beispiel-Daten
data = {
    'Größe': [175, 160, 180, 165, 170],
    'Gewicht': [70, 55, 80, 60, 75]
}

df = pd.DataFrame(data)

# Berechnungen
size_var = np.var(df['Größe'], ddof=1)
size_median = np.median(df['Größe'])
size_mean = np.mean(df['Größe'])
size_mode = df['Größe'].mode().iloc[0] if not df['Größe'].mode().empty else None
size_range = np.ptp(df['Größe'])

weight_var = np.var(df['Gewicht'], ddof=1)
weight_median = np.median(df['Gewicht'])
weight_mean = np.mean(df['Gewicht'])
weight_mode = df['Gewicht'].mode().iloc[0] if not df['Gewicht'].mode().empty else None
weight_range = np.ptp(df['Gewicht'])

# Ergebnisse in eine Tabelle einfügen
result_df = pd.DataFrame({
    '': ['Varianz', 'Median', 'Arithmetisches Mittel', 'Modus', 'Spannweite'],
    'Größe': [size_var, size_median, size_mean, size_mode, size_range],
    'Gewicht': [weight_var, weight_median, weight_mean, weight_mode, weight_range]
})

print(result_df)


# Beispiel-Daten
data = {
    'Größe': [175, 160, 180, 165, 170],
    'Gewicht': [70, 55, 80, 60, 75]
}

df = pd.DataFrame(data)

# Initialisiere Ergebnis-DataFrame
result_df = pd.DataFrame({
    '': ['Varianz', 'Median', 'Arithmetisches Mittel', 'Modus', 'Spannweite']
})

# Schleife durch alle numerischen Spalten
for column in df.select_dtypes(include=[np.number]).columns:
    var = np.var(df[column], ddof=1)
    median = np.median(df[column])
    mean = np.mean(df[column])
    mode = df[column].mode().iloc[0] if not df[column].mode().empty else None
    range_ = np.ptp(df[column])

    result_df[column] = [var, median, mean, mode, range_]

print(result_df)

# Beispiel-Daten
data = {
    'Größe': [175, 160, 180, 165, 170],
    'Geschlecht': ['männlich', 'weiblich', 'männlich', 'weiblich', 'männlich'],
    'Gewicht': [70, 55, 80, 60, 75]
}

df = pd.DataFrame(data)

# Initialisiere Ergebnis-DataFrame
result_df = pd.DataFrame({
    '': ['Varianz', 'Median', 'Arithmetisches Mittel', 'Modus', 'Spannweite']
})

# Schleife durch alle numerischen Spalten
for column in df.select_dtypes(include=[np.number]).columns:
    var = np.var(df[column], ddof=1)
    median = np.median(df[column])
    mean = np.mean(df[column])
    mode = df[column].mode().iloc[0] if not df[column].mode().empty else None
    range_ = np.ptp(df[column])

    result_df[column] = [var, median, mean, mode, range_]

# Speichern der Tabelle als CSV-Datei
result_df.to_csv('statistische_kennwerte.csv', index=False)

print("Daten erfolgreich gespeichert in 'statistische_kennwerte.csv'")

import os

print("Arbeitsverzeichnis:", os.getcwd())

```

### Ausgabe
```
Ich wurde als Modul NEU_12 eingebunden
6
___
20
20
Help on module NEU_12:

NAME
    NEU_12 - Das ist ein Modul zum ausprobieren.

FUNCTIONS
    fkt(vektor)
        Diese Funktion nimmt das erste Zeichen.

    wert_mal_faktor(wert)

DATA
    faktor = 10
    letztes_ergebnis = 20

FILE
    c:\users\nikla\pycharmprojects\pythonproject\neu_12.py


6
70
10
140
140
---------
7

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_13.py", line 15, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'

```

## NEU_14.py

### Code
```python
import numpy as np
import matplotlib.pyplot as plt

# Definitionsbereich für x
x = np.linspace(-10, 10, 400)
y = (-x + 1) / (-2 * x - 1)

# Bedingung der Ungleichung
condition = np.abs(y) < 2

# Plotten der Graphen
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$\left| \frac{-x + 1}{-2x - 1} \right| < 2$')

# Gültiger Bereich der Ungleichung hervorheben
plt.fill_between(x, y, where=condition, color='lightblue', alpha=0.5)

# Plot-Einstellungen
plt.axhline(2, color='red', linestyle='--', label='y = 2')
plt.axhline(-2, color='red', linestyle='--', label='y = -2')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.ylim(-10, 10)
plt.xlim(-10, 10)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_14.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

```

## NEU_15.py

### Code
```python
import numpy as np
import matplotlib.pyplot as plt

# Definiere die Stückweise Funktion
def piecewise_function(x):
    if x <= 0:
        return (1 / 1.4) * x + 1
    elif 0 < x <= 3:
        return -0.5 * x + 1
    else:
        return -0.5

# Erstelle Werte für x und y
x_values = np.linspace(-10, 10, 400)
y_values = [piecewise_function(x) for x in x_values]

# Zeichne den Graphen
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Stückweise Funktion')

# Markiere die Bereiche
plt.axvline(0, color='red', linestyle='--', label='x = 0')
plt.axvline(3, color='blue', linestyle='--', label='x = 3')

# Plot-Einstellungen
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Stückweise Funktion')
plt.grid(True)
plt.show()



```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_15.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

```

## NEU_16.py

### Code
```python
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

```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_16.py", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

```

## NEU_17.py

### Code
```python
import matplotlib.pyplot as plt
import numpy as np

# Definieren Sie die Funktion
def f(x):
    return (2*x + 3) / np.abs(x + 4)

# Erstellen Sie einen Bereich für x-Werte
x = np.linspace(-10, 10, 400)
y = f(x)

# Bedingung, wann die Ungleichung erfüllt ist
y_condition = y <= 1

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$\frac{2x+3}{|x+4|}$')
plt.fill_between(x, -10, 10, where=y_condition, color='lightgray', alpha=0.5, label=r'$\frac{2x+3}{|x+4|} \leq 1$')
plt.axhline(1, color='red', linestyle='--', label=r'$y=1$')
plt.axvline(-4, color='green', linestyle='--', label=r'$x=-4$')
plt.ylim(-10, 10)  # Begrenzen wir den y-Bereich zur besseren Sichtbarkeit
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Plot von $\frac{2x+3}{|x+4|} \leq 1$')
plt.legend()
plt.grid(True)
plt.show()

```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_17.py", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

```

## NEU_18.py

### Code
```python
import matplotlib.pyplot as plt
import numpy as np

# Definieren Sie die Funktion
def f(x):
    return np.abs(3*x - 2) / (x + 2)

# Erstellen Sie einen Bereich für x-Werte
x = np.linspace(-10, 10, 400)
y = f(x)

# Bedingung, wann die Ungleichung erfüllt ist
y_condition = y >= 2

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$\frac{|3x - 2|}{x + 2}$')
plt.fill_between(x, -10, 10, where=y_condition, color='lightgray', alpha=0.5, label=r'$\frac{|3x - 2|}{x + 2} \geq 2$')
plt.axhline(2, color='red', linestyle='--', label=r'$y=2$')
plt.ylim(-5, 15)  # Begrenzen wir den y-Bereich zur besseren Sichtbarkeit
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Plot von $\frac{|3x - 2|}{x + 2} \geq 2$')
plt.legend()
plt.grid(True)
plt.show()

```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_18.py", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

```

## NEU_19.py

### Code
```python
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

```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_19.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

```

## NEU_2.py

### Code
```python




def fkt_leer(wert):
    drei_mal_drei_leer = [[" ", wert, " "] for i in range(3)]
    return drei_mal_drei_leer


print(fkt_leer(33))

def Summe(wert):
    S = sum(int(fkt_leer(wert)[i][1]) for i in range(3))
    return S

print(Summe(77))

# füge 9 objekte hinzu.
Liste = []
while True:
    einkaufen = input("Was willst du kaufen?")
    if len(Liste) > 8:
        break
    else:
        Liste.append(einkaufen)

print(Liste)
```

### Ausgabe
```

[Fehler]
Fehler beim Ausführen: Command '['python', 'C:\\Users\\nikla\\PycharmProjects\\pythonProject\\NEU_2.py']' timed out after 10 seconds
```

## NEU_21.py

### Code
```python
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

```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_21.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

```

## NEU_22.py

### Code
```python
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

```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_22.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

```

## NEU_23.py

### Code
```python
import random

# Initialisiere die Bilder und ELO-Bewertungen
images = [f"BILD{i}" for i in range(1, 11)]
elo_ratings = {image: 1500 for image in images}

# Funktion, um die Siegwahrscheinlichkeit zu berechnen
def expected_score(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

# Funktion, um ELO-Werte zu aktualisieren
def update_elo(rating_a, rating_b, result, k=32):
    expected_a = expected_score(rating_a, rating_b)
    expected_b = 1 - expected_a
    new_rating_a = rating_a + k * (result - expected_a)
    new_rating_b = rating_b + k * ((1 - result) - expected_b)
    return new_rating_a, new_rating_b

# Hauptlogik: Vergleiche sicherstellen
def ensure_minimum_comparisons(min_comparisons=3):
    global elo_ratings

    # Verfolgen, wie oft jedes Bild in einem Vergleich vorkam
    comparison_counts = {image: 0 for image in images}
    pair_counts = {image: 0 for image in images}
    total_comparisons = 0

    while any(count < min_comparisons for count in comparison_counts.values()):
        # Zufällige Auswahl von zwei verschiedenen Bildern
        image_a, image_b = random.sample(images, 2)

        # Aktualisiere Paarzählungen für die beiden Bilder
        pair_counts[image_a] += 1
        pair_counts[image_b] += 1

        # Benutzerinteraktion
        print(f"Welches Bild gefällt dir besser? (1 für {image_a}, 2 für {image_b})")
        choice = input()

        if choice == "1":
            elo_ratings[image_a], elo_ratings[image_b] = update_elo(
                elo_ratings[image_a], elo_ratings[image_b], 1
            )
            comparison_counts[image_a] += 1
        elif choice == "2":
            elo_ratings[image_a], elo_ratings[image_b] = update_elo(
                elo_ratings[image_a], elo_ratings[image_b], 0
            )
            comparison_counts[image_b] += 1
        else:
            print("Ungültige Eingabe. Bitte wähle 1 oder 2.")
            continue  # Ungültige Eingaben überspringen

        total_comparisons += 1

    # Rangliste erstellen
    sorted_images = sorted(elo_ratings.items(), key=lambda x: x[1], reverse=True)
    print("\nRangliste der Bilder:")
    for rank, (image, rating) in enumerate(sorted_images, 1):
        print(f"{rank}. {image} (ELO: {rating:.1f})")

    # Vergleichsanzahl pro Bild anzeigen
    print("\nVergleichshäufigkeit pro Bild:")
    for image, count in pair_counts.items():
        print(f"{image}: {count} Mal im Paarvergleich verwendet")

    # Zeige die Gesamtzahl der Vergleiche an
    print(f"\nInsgesamt durchgeführte Vergleiche: {total_comparisons}")

# Starte die Vergleiche
ensure_minimum_comparisons(min_comparisons=3)

```

### Ausgabe
```

[Fehler]
Fehler beim Ausführen: Command '['python', 'C:\\Users\\nikla\\PycharmProjects\\pythonProject\\NEU_23.py']' timed out after 10 seconds
```

## NEU_24.py

### Code
```python
import tkinter as tk
from tkinter import messagebox
import itertools
import random

# Initialisiere die Bilder und ELO-Bewertungen
images = [f"BILD{i}" for i in range(1, 11)]
elo_ratings = {image: 1500 for image in images}


# Funktion, um die Siegwahrscheinlichkeit zu berechnen
def expected_score(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))


# Funktion, um ELO-Werte zu aktualisieren
def update_elo(rating_a, rating_b, result, k=32):
    expected_a = expected_score(rating_a, rating_b)
    expected_b = 1 - expected_a
    new_rating_a = rating_a + k * (result - expected_a)
    new_rating_b = rating_b + k * ((1 - result) - expected_b)
    return new_rating_a, new_rating_b


# Hauptlogik: Paarvergleich und GUI-Update
def compare(choice):
    global current_pair_index, comparisons

    image_a, image_b = all_pairs[current_pair_index]

    # Aktualisiere ELO-Werte basierend auf der Benutzerauswahl
    if choice == "left":
        elo_ratings[image_a], elo_ratings[image_b] = update_elo(
            elo_ratings[image_a], elo_ratings[image_b], 1
        )
    elif choice == "right":
        elo_ratings[image_a], elo_ratings[image_b] = update_elo(
            elo_ratings[image_a], elo_ratings[image_b], 0
        )

    comparisons += 1
    current_pair_index += 1

    # Überprüfen, ob alle Paarungen abgeschlossen sind
    if current_pair_index >= len(all_pairs):
        show_results()
    else:
        # Nächste Paarung anzeigen
        image_a, image_b = all_pairs[current_pair_index]
        left_button.config(text=image_a)
        right_button.config(text=image_b)


# Ergebnisse anzeigen
def show_results():
    # Ergebnisse sortieren
    sorted_images = sorted(elo_ratings.items(), key=lambda x: x[1], reverse=True)
    result_message = "\n".join([f"{rank}. {image} (ELO: {rating:.1f})"
                                for rank, (image, rating) in enumerate(sorted_images, 1)])

    messagebox.showinfo("Rangliste", result_message)
    messagebox.showinfo("Vergleiche", f"Insgesamt durchgeführte Vergleiche: {comparisons}")
    root.destroy()


# GUI-Setup
root = tk.Tk()
root.title("Bildvergleich")

# Erstelle alle möglichen Paarungen
all_pairs = list(itertools.combinations(images, 2))
random.shuffle(all_pairs)  # Optional: Zufällige Reihenfolge der Vergleiche

comparisons = 0
current_pair_index = 0

# Erste Paarung festlegen
image_a, image_b = all_pairs[current_pair_index]

# Buttons für die Bildauswahl
left_button = tk.Button(root, text=image_a, font=("Arial", 14), command=lambda: compare("left"))
left_button.pack(side="left", expand=True, fill="both", padx=20, pady=20)

right_button = tk.Button(root, text=image_b, font=("Arial", 14), command=lambda: compare("right"))
right_button.pack(side="right", expand=True, fill="both", padx=20, pady=20)

# Event-Schleife starten
root.mainloop()

```

### Ausgabe
_Keine Ausgabe_

## NEU_25.py

### Code
```python
import random


# Funktion zur Optimierung der Pivot-Wahl (Median of Three)
def choose_pivot(arr):
    if len(arr) < 3:
        return arr[0]
    else:
        # Wähle drei zufällige Elemente und finde deren Median
        samples = random.sample(arr, 3)
        samples.sort()
        return samples[1]


# QuickSort-Algorithmus mit optimierter Pivot-Wahl
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Pivot intelligent wählen (Median-of-Three oder zufällig)
        pivot = choose_pivot(arr)
        arr.remove(pivot)  # Entferne das Pivot aus der Liste

        # Zwei Listen für "kleiner" und "größer"
        less_than_pivot = []
        greater_than_pivot = []

        for item in arr:
            # Vergleiche das aktuelle Element mit dem Pivot
            print(f"Vergleich: {item} mit {pivot}. (1 für kleiner, 2 für größer)")
            choice = input()
            if choice == "1":
                less_than_pivot.append(item)
            elif choice == "2":
                greater_than_pivot.append(item)
            else:
                print("Ungültige Eingabe. Bitte wähle 1 oder 2.")

        # Rekursive Aufrufe und Zusammenfügen der Listen
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


# Hauptfunktion
def start_comparison():
    print("Wie viele Elemente möchtest du sortieren?")
    n = int(input())

    # Generiere eine Liste von Zahlen oder Items
    items = [f"ITEM{i}" for i in range(1, n + 1)]
    random.shuffle(items)  # Zufällige Reihenfolge für einen realistischen Test

    print("\nStarte QuickSort mit den folgenden Elementen:")
    print(", ".join(items))

    # QuickSort ausführen
    sorted_items = quicksort(items)

    # Ergebnis anzeigen
    print("\nSortierte Reihenfolge:")
    for rank, item in enumerate(sorted_items, 1):
        print(f"{rank}. {item}")


# Programm starten
start_comparison()

```

### Ausgabe
```

[Fehler]
Fehler beim Ausführen: Command '['python', 'C:\\Users\\nikla\\PycharmProjects\\pythonProject\\NEU_25.py']' timed out after 10 seconds
```

## NEU_26.py

### Code
```python
import itertools

# Initialisiere die Bilder
images = [f"BILD{i}" for i in range(1, 11)]

# Alle möglichen Paare generieren
all_pairs = list(itertools.combinations(images, 2))  # Jede Kombination aus zwei Bildern

# Hauptlogik
def start_equal_comparisons():
    # Zähler für die Vergleiche
    comparison_counts = {image: 0 for image in images}
    total_comparisons = 0

    for image_a, image_b in all_pairs:
        # Benutzerinteraktion
        print(f"Welches Bild gefällt dir besser? (1 für {image_a}, 2 für {image_b})")
        choice = input()

        if choice == "1":
            comparison_counts[image_a] += 1
        elif choice == "2":
            comparison_counts[image_b] += 1
        else:
            print("Ungültige Eingabe. Bitte wähle 1 oder 2.")
            continue  # Ungültige Eingaben überspringen

        total_comparisons += 1

    # Rangliste erstellen basierend auf der Anzahl der Favoriten
    sorted_images = sorted(comparison_counts.items(), key=lambda x: x[1], reverse=True)

    print("\nRangliste der Bilder:")
    for rank, (image, count) in enumerate(sorted_images, 1):
        print(f"{rank}. {image} (Favoriten: {count})")

    # Zeige die Gesamtanzahl der Vergleiche an
    print(f"\nInsgesamt durchgeführte Vergleiche: {total_comparisons}")

# Starte die Funktion
start_equal_comparisons()

```

### Ausgabe
```

[Fehler]
Fehler beim Ausführen: Command '['python', 'C:\\Users\\nikla\\PycharmProjects\\pythonProject\\NEU_26.py']' timed out after 10 seconds
```

## NEU_27.py

### Code
```python
import itertools

# Liste der Bilder
bilder = [f"BILD{i}" for i in range(1, 11)]

# Alle möglichen Paare generieren, 2 für 2 Bilder, aber mehr auc möglich.
paare = list(itertools.combinations(bilder, 2))

# Ausgabe der Paare
for paar in paare:
    print(paar)


def vergleiche():

    counter = {bild: 0 for bild in bilder}
    total_comparisons = 0

    for bild_a, bild_b in paare:
        while True:
            #choice = input(f"wähle 1 für {bild_a} und 2 für {bild_b}: ")
            choice = "1"
            if choice == "1":
                counter[bild_a] += 1
                break
            elif choice == "2":
                counter[bild_b] += 1
                break
            else:
                print("Ungültige Eingabe. Bitte wähle 1 oder 2.")

        total_comparisons += 1
    return counter

print(vergleiche())

```

### Ausgabe
```
('BILD1', 'BILD2')
('BILD1', 'BILD3')
('BILD1', 'BILD4')
('BILD1', 'BILD5')
('BILD1', 'BILD6')
('BILD1', 'BILD7')
('BILD1', 'BILD8')
('BILD1', 'BILD9')
('BILD1', 'BILD10')
('BILD2', 'BILD3')
('BILD2', 'BILD4')
('BILD2', 'BILD5')
('BILD2', 'BILD6')
('BILD2', 'BILD7')
('BILD2', 'BILD8')
('BILD2', 'BILD9')
('BILD2', 'BILD10')
('BILD3', 'BILD4')
('BILD3', 'BILD5')
('BILD3', 'BILD6')
('BILD3', 'BILD7')
('BILD3', 'BILD8')
('BILD3', 'BILD9')
('BILD3', 'BILD10')
('BILD4', 'BILD5')
('BILD4', 'BILD6')
('BILD4', 'BILD7')
('BILD4', 'BILD8')
('BILD4', 'BILD9')
('BILD4', 'BILD10')
('BILD5', 'BILD6')
('BILD5', 'BILD7')
('BILD5', 'BILD8')
('BILD5', 'BILD9')
('BILD5', 'BILD10')
('BILD6', 'BILD7')
('BILD6', 'BILD8')
('BILD6', 'BILD9')
('BILD6', 'BILD10')
('BILD7', 'BILD8')
('BILD7', 'BILD9')
('BILD7', 'BILD10')
('BILD8', 'BILD9')
('BILD8', 'BILD10')
('BILD9', 'BILD10')
{'BILD1': 9, 'BILD2': 8, 'BILD3': 7, 'BILD4': 6, 'BILD5': 5, 'BILD6': 4, 'BILD7': 3, 'BILD8': 2, 'BILD9': 1, 'BILD10': 0}

```

## NEU_28_tkinter.py

### Code
```python
from tkinter import *


root = Tk() # erzeuge Fenster

e = Entry(root, width = 40) # Textzeile zur Eingabe
e.pack()
e.insert(0, "Enter Name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text =  "Enter name",
                  command = myClick)
myButton.pack()


root.mainloop()
```

### Ausgabe
_Keine Ausgabe_

## NEU_29_tkinter2.py

### Code
```python
from tkinter import *

root = Tk() # erzeuge Fenster

# Creating a Label Widget
myLabel1 = Label(root, text = "Hello World!")
myLabel2 = Label(root, text = "I am cool")
myLabel3 = Label(root, text = "Nächste Reihe").grid(row = 2, column = 2)


# Shoving it onto the screen = schieben
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 4) # relativ, 1 = 4 = 5


root.mainloop()

root = Tk() # erzeuge Fenster

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text = "Click me!", padx = 50, pady = 50)

myButton.pack()


root.mainloop()

root = Tk() # erzeuge Fenster

def myClick():
    myLabel = Label(root, text = "I clicked")
    myLabel.pack()

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text = "Click me!",
                  command = myClick, fg = "blue", bg = "#000000")
myButton.pack()


root.mainloop()

root = Tk() # erzeuge Fenster

e = Entry(root, width = 40, bg = "blue", fg = "white",
          borderwidth = 5) # Textzeile zur Eingabe
e.pack()


def myClick():
    myLabel = Label(root, text = "I clicked")
    myLabel.pack()

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text = "Click me!",
                  command = myClick)
myButton.pack()


root.mainloop()

root = Tk() # erzeuge Fenster

e = Entry(root, width = 40) # Textzeile zur Eingabe
e.pack()


def myClick():
    myLabel = Label(root, text = e.get())
    myLabel.pack()

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text = "Enter name",
                  command = myClick)
myButton.pack()


root.mainloop()

root = Tk() # erzeuge Fenster

e = Entry(root, width = 40) # Textzeile zur Eingabe
e.pack()


def myClick():
    myLabel = Label(root, text = "Hello " + e.get())
    myLabel.pack()

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text =  "Enter name",
                  command = myClick)
myButton.pack()


root.mainloop()


root = Tk() # erzeuge Fenster

e = Entry(root, width = 40) # Textzeile zur Eingabe
e.pack()


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text =  "Enter name",
                  command = myClick)
myButton.pack()


root.mainloop()

root = Tk() # erzeuge Fenster

e = Entry(root, width = 40) # Textzeile zur Eingabe
e.pack()
e.insert(0, "Enter Name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text =  "Enter name",
                  command = myClick)
myButton.pack()


root.mainloop()
```

### Ausgabe
```

[Fehler]
Fehler beim Ausführen: Command '['python', 'C:\\Users\\nikla\\PycharmProjects\\pythonProject\\NEU_29_tkinter2.py']' timed out after 10 seconds
```

## NEU_3.py

### Code
```python
daten = """
Name,Alter,Stadt
Anna,28,Berlin
Max,35,Hamburg
Sophie,22,München
Lukas,30,Köln
"""

# Daten in Zeilen aufteilen
zeilen = daten.strip().split('\n')

# Überschriften extrahieren
header = zeilen[0].split(',')

# Daten in eine Liste von Dictionaries umwandeln
personen = [
    {header[i]: eintrag for i, eintrag in enumerate(zeile.split(','))}
    for zeile in zeilen[1:]
]

# Ausgabe der eingelesenen Daten
for person in personen:
    print(person)

import pandas as pd

# Daten in einem Dictionary speichern
daten = {
    "Name": ["Anna", "Max", "Sophie", "Lukas"],
    "Alter": [28, 35, 22, 30],
    "Stadt": ["Berlin", "Hamburg", "München", "Köln"]
}

print(daten)
# DataFrame erstellen
df = pd.DataFrame(daten)
print(df)
wert_1 = df.iloc[3, 1]
wert_2 = df.iloc[3]
neue_zeile = pd.DataFrame([{'Name': 'Nik', 'Alter': '39', 'Stadt': 'Köln'}])

df = pd.concat([df, neue_zeile], ignore_index=True)
print(df)

neue_zeilen_2 = pd.DataFrame([
    {"Name": "AA", "Alter": 33, "Stadt": "Nürnberg"},
    {"Name": "BB", "Alter": 55, "Stadt": "München"}
])

df = pd.concat([df, neue_zeilen_2], ignore_index=True)
print(df)

df.loc[len(df)] = ["AA", 33, "Nürnberg"]
df.loc[len(df)] = ["BB", None, "München"]
print(df)


# Assuming 'df' is already defined and 'Alter' column exists

import pandas as pd
import numpy as np

# Assuming 'df' is already defined and 'Alter' column exists

# Convert the 'Alter' column to numeric, forcing non-numeric values to NaN
df['Alter'] = pd.to_numeric(df['Alter'], errors='coerce')

# Calculate the mean of the 'Alter' column, ignoring NaN values
mean_alter = df['Alter'].mean()

# Replace None and NaN values with the mean of the 'Alter' column
for i in range(len(df)):
    for j in range(df.shape[1]):
        if pd.isna(df.iloc[i, j]):
            df.iloc[i, j] = mean_alter
            print(df.iloc[i, j])

import statistics
import numpy as np

def boxpl(x):
    mean_value = statistics.mean(x)
    variance_value = statistics.variance(x)
    return mean_value, variance_value

# Generate 100 random numbers from the standard normal distribution
random_numbers = np.random.standard_normal(100)

# Call the function and print the result
mean, variance = boxpl(random_numbers)
print(f"Mean: {mean:.2f}, Variance: {variance:.2f}")

print(df)

df["Geschlecht"] = np.tile(["w", "m"], len(df) // 2 + 1)[:len(df)]

print(df)
print(5//2, 4//2, 3//2)
zahlen_liste = list(range(1, 101))
print(zahlen_liste)
zahlen_liste_2 = [x for x in range(1, 11)]
print(zahlen_liste_2)
df["Nummerierung"] = np.tile(zahlen_liste_2, 1)[:len(df)]
print(df)

df["Nummerierung"] = [i if i % 2 == 0 else 0 for i in df["Nummerierung"]]
print(df)

mean_by_gender = df.groupby(["Geschlecht", "Stadt"])["Alter"].mean()

print(mean_by_gender)
```

### Ausgabe
```
{'Name': 'Anna', 'Alter': '28', 'Stadt': 'Berlin'}
{'Name': 'Max', 'Alter': '35', 'Stadt': 'Hamburg'}
{'Name': 'Sophie', 'Alter': '22', 'Stadt': 'München'}
{'Name': 'Lukas', 'Alter': '30', 'Stadt': 'Köln'}

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_3.py", line 25, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'

```

## NEU_30.py

### Code
```python
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

# Hauptfenster erstellen
root = Tk()
root.title("Normalverteilung Plotter")

# Eingabefelder für Erwartungswert und Varianz
mean_label = Label(root, text="Erwartungswert (Mean):")
mean_label.pack()
mean_entry = Entry(root, width=20)
mean_entry.pack()

variance_label = Label(root, text="Varianz:")
variance_label.pack()
variance_entry = Entry(root, width=20)
variance_entry.pack()

# Funktion zum Plotten der Normalverteilung
def plot_normal_distribution():
    try:
        mean = float(mean_entry.get())
        variance = float(variance_entry.get())
        if variance <= 0:
            raise ValueError("Die Varianz muss positiv sein.")

        # Normalverteilung berechnen
        std_dev = np.sqrt(variance)
        x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 500)
        y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

        # Plot erstellen
        plt.figure(figsize=(8, 5))
        plt.plot(x, y, label=f"Mean = {mean}, Variance = {variance}")
        plt.title("Normalverteilung")
        plt.xlabel("x")
        plt.ylabel("Wahrscheinlichkeit")
        plt.ylim(0, 0.4)  # Begrenzung der y-Achse auf maximal 0.4
        plt.legend()
        plt.grid()
        plt.show()
    except ValueError as e:
        error_label = Label(root, text=f"Fehler: {e}", fg="red")
        error_label.pack()

# Button zum Plotten erstellen
plot_button = Button(root, text="Normalverteilung zeichnen", command=plot_normal_distribution)
plot_button.pack()

# Hauptschleife starten
root.mainloop()



from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Hauptfenster erstellen
root = Tk()
root.title("Normalverteilung Plotter")

# Eingabefelder für Erwartungswert und Varianz
mean_label = Label(root, text="Erwartungswert (Mean):")
mean_label.pack()
mean_entry = Entry(root, width=20)
mean_entry.pack()

variance_label = Label(root, text="Varianz:")
variance_label.pack()
variance_entry = Entry(root, width=20)
variance_entry.pack()

# Rahmen für den Plot
plot_frame = Frame(root)
plot_frame.pack()

# Funktion zum Plotten der Normalverteilung
def plot_normal_distribution():
    try:
        mean = float(mean_entry.get())
        variance = float(variance_entry.get())
        if variance <= 0:
            raise ValueError("Die Varianz muss positiv sein.")

        # Normalverteilung berechnen
        std_dev = np.sqrt(variance)
        x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 500)
        y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

        # Plot erstellen
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x, y, label=f"Mean = {mean}, Variance = {variance}")
        ax.set_title("Normalverteilung")
        ax.set_xlabel("x")
        ax.set_ylabel("Wahrscheinlichkeit")
        ax.set_ylim(0, 0.4)
        ax.legend()
        ax.grid()

        # Vorherigen Plot entfernen (falls vorhanden)
        for widget in plot_frame.winfo_children():
            widget.destroy()

        # Plot in Tkinter einbetten
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()
        canvas.draw()
    except ValueError as e:
        error_label = Label(root, text=f"Fehler: {e}", fg="red")
        error_label.pack()

# Button zum Plotten erstellen
plot_button = Button(root, text="Normalverteilung zeichnen", command=plot_normal_distribution)
plot_button.pack()

# Hauptschleife starten
root.mainloop()



```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_30.py", line 2, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

```

## NEU_31.py

### Code
```python
from tkinter import *


root = Tk() # erzeuge Fenster

e = Entry(root, width = 40) # Textzeile zur Eingabe
e.pack()
e.insert(0, "Enter Name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text =  "Enter name",
                  command = myClick)
myButton.pack()


root.mainloop()
```

### Ausgabe
_Keine Ausgabe_

## NEU_32.py

### Code
```python
from tkinter import *

root = Tk()

e = Entry(root, width = 50)
e.pack()
e.insert(0, "Enter Name now: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

myButton = Button(root, text = "Enter Name", command = myClick)
myButton.pack()

root.mainloop()


```

### Ausgabe
_Keine Ausgabe_

## NEU_33.py

### Code
```python
from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def button_click(number):
   current = e.get()
   e.delete(0, END)
   e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
       e.insert(0, f_num + int(second_number))
    if math == "subtraction":
       e.insert(0, f_num - int(second_number))
    if math == "multiplication":
       e.insert(0, f_num * int(second_number))
    if math == "division":
       e.insert(0, f_num / int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))

button_add = Button(root, text = "+", padx = 39, pady = 20, command = button_add)
button_equal = Button(root, text = "=", padx = 91, pady = 20, command = button_equal)
button_clear = Button(root, text = "Clear", padx = 79, pady = 20, command = button_clear)

button_subtract = Button(root, text = "-", padx = 41, pady = 20, command = button_subtract)
button_multiply = Button(root, text = "*", padx = 40, pady = 20, command = button_multiply)
button_divide = Button(root, text = "/", padx = 41, pady = 20, command = button_divide)


button_0.grid(row = 4, column = 0)

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_clear.grid(row = 4, column = 1, columnspan = 2)
button_add.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 1, columnspan = 2)

button_subtract.grid(row = 6, column = 0)
button_multiply.grid(row = 6, column = 1)
button_divide.grid(row = 6, column = 2)


root.mainloop()
```

### Ausgabe
_Keine Ausgabe_

## NEU_34.py

### Code
```python
from tkinter import *

root = Tk()
root.title("Grid-Beispiel")

# Eingabefeld oben
entry = Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Beispiel-Funktion
def button_click(number):
    entry.insert(END, str(number))

# Buttons 1–9 in einem 3x3-Raster
buttons = []
row = 1
col = 0
for i in range(1, 10):
    btn = Button(root, text=str(i), padx=20, pady=20, command=lambda num=i: button_click(num))
    btn.grid(row=row, column=col)
    col += 1
    if col > 2:
        col = 0
        row += 1
    buttons.append(btn)

# Button 0 mittig unten
btn_zero = Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))
btn_zero.grid(row=4, column=1)

# Weitere Buttons (z. B. Clear, =)
btn_clear = Button(root, text="Clear", padx=20, pady=20, command=lambda: entry.delete(0, END))
btn_clear.grid(row=4, column=0)

btn_equal = Button(root, text="=", padx=20, pady=20)
btn_equal.grid(row=4, column=2)

root.mainloop()

```

### Ausgabe
_Keine Ausgabe_

## NEU_35.py

### Code
```python
import matplotlib.pyplot as plt
import numpy as np

def plot_nv():
    while True:
        try:
            # Eingaben für Erwartungswert und Varianz abfragen
            #e_wert = float(input("Erwartungswert: "))
            #varianz = float(input("Varianz: "))
            e_wert = 100
            varianz = 25
            # Überprüfen, ob die Varianz positiv ist
            if varianz <= 0:
                raise ValueError("Die Varianz muss positiv sein.")

            # Daten erstellen
            x = np.linspace(e_wert - 5 * np.sqrt(varianz), e_wert + 5 * np.sqrt(varianz), 500)
            y = (1 / np.sqrt(2 * np.pi * varianz)) * np.exp(-((x - e_wert) ** 2) / (2 * varianz))

            # Plot erstellen
            plt.plot(x, y,
                     label=f'Normalverteilung ($\\mu$={e_wert},'
                           f' $\\sigma^2$={varianz})',
                     color='blue', linewidth=2)

            # Achsenbeschriftungen hinzufügen
            plt.xlabel('x-Wert')
            plt.ylabel('Dichte der NV')

            # Titel hinzufügen
            plt.title('Dichtefunktion der Normalverteilung')

            # Legende hinzufügen
            # Legende hinzufügen und in die rechte obere Ecke platzieren
            plt.legend(loc='upper right')

            # Gitter anzeigen (optional)
            plt.grid(True)

            # Plot anzeigen
            plt.show()

            # Beende die Schleife, wenn der Plot erfolgreich angezeigt wurde
            break

        except ValueError as ve:
            print(f"Fehler: {ve} Bitte erneut versuchen.")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}. Bitte erneut versuchen.")

# Funktionsaufruf
plot_nv()
```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_35.py", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

```

## NEU_36.py

### Code
```python
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Coding.")
root.iconbitmap(r"C:\Users\nikla\Downloads\bnb_crypto_icon_264371.ico")

my_img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\nikla\Downloads\Hornbach.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\nikla\Downloads\Cartoon_1.jfif"))
my_img3 = ImageTk.PhotoImage(Image.open(r"C:\Users\nikla\Downloads\Cartoon_2.jfif"))
my_img4 = ImageTk.PhotoImage(Image.open(r"C:\Users\nikla\Downloads\Cartoon_3.jfif"))
my_img5 = ImageTk.PhotoImage(Image.open(r"C:\Users\nikla\Downloads\Cartoon_4.jpg"))

# Liste erstellen
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number - 1])
    button_forward = Button(root, text = ">>",
                            command = lambda: forward(image_number + 1))
    button_back = Button(root, text = "<<",
                         command = lambda: back(image_number -1))
    if image_number == 5:
        button_forward = Button(root, text = ">>",
                            state = DISABLED)

    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>",
                            command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<",
                         command=lambda: back(image_number - 1))
    if image_number == 1:
        button_back = Button(root, text="<<",
                                state=DISABLED)

    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)



button_back = Button(root, text = "<<", state = DISABLED)
button_exit = Button(root, text = "EXIT PROGRAMM", command = root.quit)
button_forward = Button(root, text = ">>", command = lambda: forward(2))

button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2)




root.mainloop()


```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_36.py", line 2, in <module>
    from PIL import ImageTk, Image
ModuleNotFoundError: No module named 'PIL'

```

## NEU_37.py

### Code
```python
a = 5


def func():
    c = 10
    d = c + a

    globals()['a'] = d
    print(a)


func()




my_img1, my_img2, my_img3, my_img4, my_img5 = 20, 30, 40, 50, 60

image_list = [globals()[f"my_img{i}"] for i in range(1, 6)]
print(image_list)
print("----")
values = [21, 31, 41, 51, 61]
variables = {}

for i, value in enumerate(values, start=1):
    variables[f"my_img{i}"] = value

print(variables)
print(variables["my_img2"])

import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("240x100")
root.title('Login')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


root.mainloop()

```

### Ausgabe
```
15
[20, 30, 40, 50, 60]
----
{'my_img1': 21, 'my_img2': 31, 'my_img3': 41, 'my_img4': 51, 'my_img5': 61}
31

```

## NEU_38.py

### Code
```python
from tkinter import Tk, Canvas, Button

# Hauptfenster erstellen
root = Tk()
root.title("6x6 Grid mit Buttons")

# Größe des Fensters und des Spielfelds
window_width = 600
window_height = 600
rows, columns = 6, 6  # 6x6 Raster
cell_size = window_width // columns

# Canvas für das Spielfeld
canvas = Canvas(root, width=window_width, height=window_height, bg="white")
canvas.grid(row=0, column=1, rowspan=6)  # Grid wird zentral platziert, über mehrere Zeilen

# Links neben dem Grid: Buttons erstellen
for i in range(4):
    Button(root, text=f"Button L{i+1}", width=12, height=2).grid(row=i+1, column=0, padx=10, pady=20)

# Rechts neben dem Grid: Buttons erstellen
for i in range(4):
    Button(root, text=f"Button R{i+1}", width=12, height=2).grid(row=i+1, column=2, padx=10, pady=20)

# Raster zeichnen
for row in range(rows):
    for col in range(columns):
        x1 = col * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

# Hauptfenster starten
root.mainloop()
```

### Ausgabe
_Keine Ausgabe_

## NEU_39.py

### Code
```python
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Coding.")
root.iconbitmap(r"C:\Users\nikla\Downloads\bnb_crypto_icon_264371.ico")

my_img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\nikla\Downloads\Hornbach.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\nikla\Downloads\Cartoon_1.jfif"))
my_img3 = ImageTk.PhotoImage(Image.open(r"C:\Users\nikla\Downloads\Cartoon_2.jfif"))
my_img4 = ImageTk.PhotoImage(Image.open(r"C:\Users\nikla\Downloads\Cartoon_3.jfif"))
my_img5 = ImageTk.PhotoImage(Image.open(r"C:\Users\nikla\Downloads\Cartoon_4.jpg"))

# Liste erstellen
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text = "Image 1 of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E)


my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number - 1])
    button_forward = Button(root, text = ">>",
                            command = lambda: forward(image_number + 1))
    button_back = Button(root, text = "<<",
                         command = lambda: back(image_number -1))
    if image_number == 5:
        button_forward = Button(root, text = ">>",
                            state = DISABLED)

    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>",
                            command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<",
                         command=lambda: back(image_number - 1))
    if image_number == 1:
        button_back = Button(root, text="<<",
                                state=DISABLED)

    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

button_back = Button(root, text = "<<", state = DISABLED)
button_exit = Button(root, text = "EXIT PROGRAMM", command = root.quit)
button_forward = Button(root, text = ">>", command = lambda: forward(2))

button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2, pady = 10)
status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)



root.mainloop()


```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_39.py", line 2, in <module>
    from PIL import ImageTk, Image
ModuleNotFoundError: No module named 'PIL'

```

## NEU_4.py

### Code
```python
def AddiSubbi(x, y):
    return x + y, x - y

print(AddiSubbi(3, 4))

def Multi(x, y):
    return x * y

print(Multi(3, 4))
print(AddiSubbi(3, 5))

# Aufteilen des Tupels in zwei Variablen
add_result, sub_result = AddiSubbi(2, 3)

# Aufruf der Multi-Funktion mit den einzelnen Werten
print(Multi(add_result, sub_result))  # -5

k = 0
liste = []
zahlen = [x for x in range(1, 11)]
print(zahlen, liste)

for i in zahlen:
    k = k + i
    liste.append(k)

print(liste)


liste_2 = []
k = 1

def leere_i(i):
    L = [[" " for _ in range(i)] for _ in range(i)]
    return L

print(leere_i(5))




def Binomial(L):
    matrix = leere_i(L)
    for i in range(1, L+1):
        matrix[i-1][i-1] = i
    return matrix

print(Binomial(5))

def Binomial(L):
    result = []
    for i in range(L):
        row = [1] * (i+1)
        for j in range(1, i):
            row[j] = result[i-1][j-1] + result[i-1][j]
        result.append(row)
    return result

print(Binomial(5))


for row in Binomial(7):
    print(" ".join(map(str, row)))

liste = [1]
k = 10
h = 1
for i in range(2, k+2):
    h = h * 2
    liste.append(h)
    print(liste)

namen = ["Armin", "Bert", "Conrad", "Damian", "Emil"]

for i, j in enumerate(namen):
    print(i+1, j)
```

### Ausgabe
```
(7, -1)
12
(8, -2)
-5
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] []
[1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
[[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
[[1, ' ', ' ', ' ', ' '], [' ', 2, ' ', ' ', ' '], [' ', ' ', 3, ' ', ' '], [' ', ' ', ' ', 4, ' '], [' ', ' ', ' ', ' ', 5]]
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
[1, 2]
[1, 2, 4]
[1, 2, 4, 8]
[1, 2, 4, 8, 16]
[1, 2, 4, 8, 16, 32]
[1, 2, 4, 8, 16, 32, 64]
[1, 2, 4, 8, 16, 32, 64, 128]
[1, 2, 4, 8, 16, 32, 64, 128, 256]
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
1 Armin
2 Bert
3 Conrad
4 Damian
5 Emil

```

## NEU_40.py

### Code
```python
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learn Coding.")
root.iconbitmap(r"C:\Users\nikla\Downloads\bnb_crypto_icon_264371.ico")



frame = LabelFrame(root, text = "This is my Frame...", padx = 50, pady = 50)
frame.pack(padx = 10, pady = 10) # Abstand zu Fensterrand

b = Button(frame, text = "Do not Click Here!")
b2 = Button(frame, text = "ohhhh")

b.grid(row = 0, column = 0)
b2.grid(row = 1, column = 1)

#r = IntVar()
#r.set("2")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushrooms", "Mushrooms"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text = text, variable = pizza, value = mode).pack(anchor = W)


def clicked(value):
    myLabel = Label(root, text = value)
    myLabel.pack()

#Radiobutton(root, text = "Option 1", variable = r, value = 1, command = lambda: clicked(r.get())).pack()
#Radiobutton(root, text = "Option 2", variable = r, value = 2, command = lambda: clicked(r.get())).pack()

myLabel = Label(root, text = pizza.get())
myLabel.pack()

myButton = Button(root, text = "Click", command = lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()


```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_40.py", line 2, in <module>
    from PIL import ImageTk, Image
ModuleNotFoundError: No module named 'PIL'

```

## NEU_41.py

### Code
```python
from tkinter import Tk, Frame, Canvas, Button

# Hauptfenster erstellen
root = Tk()
root.title("Spielfeld mit Buttons")

# Fenstergröße
window_width = 600
window_height = 600

# Frame für das Spielfeld
frame = Frame(root, bg="white")
frame.grid(row=1, column=1, padx=20, pady=20)  # Spielfeld zentral platzieren

# Canvas innerhalb des Frames
canvas = Canvas(frame, width=window_width, height=window_height, bg="white")
canvas.pack()

# Spielfeld-Parameter
rows, columns = 6, 6  # 6x6 Grid
cell_size = 100  # Größe eines Feldes
circle_radius = 30  # Radius der Kreise

# Kreise zeichnen (6x6 Spielfeld)
for row in range(rows):
    for col in range(columns):
        # Berechnung der Kreis-Koordinaten
        x1 = col * cell_size + (cell_size // 2) - circle_radius
        y1 = row * cell_size + (cell_size // 2) - circle_radius
        x2 = x1 + 2 * circle_radius
        y2 = y1 + 2 * circle_radius

        # Kreis zeichnen
        canvas.create_oval(x1, y1, x2, y2, fill="lightblue", outline="black")

# Buttons in den Ecken platzieren
# Oben links
Button(root, text="Button UL1", width=12, height=2).grid(row=0, column=0, padx=5, pady=5, sticky = "n")
Button(root, text="Button UL2", width=12, height=2).grid(row=1, column=0, padx=5, pady=5, sticky = "n")

# Oben rechts
Button(root, text="Button UR1", width=12, height=2).grid(row=0, column=2, padx=5, pady=5, sticky = "n")
Button(root, text="Button UR2", width=12, height=2).grid(row=1, column=2, padx=5, pady=5, sticky = "n")

# Unten links
Button(root, text="Button BL1", width=12, height=2).grid(row=2, column=0, padx=5, pady=5, sticky="s")
Button(root, text="Button BL2", width=12, height=2).grid(row=3, column=0, padx=5, pady=5, sticky="s")

# Unten rechts
Button(root, text="Button BR1", width=12, height=2).grid(row=2, column=2, padx=5, pady=5, sticky="s")
Button(root, text="Button BR2", width=12, height=2).grid(row=3, column=2, padx=5, pady=5, sticky="s")

# Hauptfenster starten
root.mainloop()
```

### Ausgabe
_Keine Ausgabe_

## NEU_42.py

### Code
```python
from tkinter import *
from PIL import ImageTk, Image

# Hauptfenster erstellen
root = Tk()
root.title("Spielfeld mit Ergebnis-Liste speichern")

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushrooms", "Mushrooms"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")  # Voreinstellung

# Liste zum Speichern der Ergebnisse
Liste_pizza = []

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value = topping).pack(anchor=W)

def clicked(value):
    global Liste_pizza
    Liste_pizza.append(value)  # Auswahl in Liste speichern
    myLabel = Label(root, text=f"Gespeichert: {value}")
    myLabel.pack()

def alle(wert):
    global Liste_pizza
    haeufigkeiten = {}
    for item in Liste_pizza:
        if item in haeufigkeiten:
            haeufigkeiten[item] += 1
        else:
            haeufigkeiten[item] = 1

    myLabel2 = Label(root, text = f"ALLE: {' '.join(Liste_pizza)}")
    myLabel2.pack()
    Label(root, text = "Bestellung:").pack(pady = 10)
    for key, value in haeufigkeiten.items():
        myLabel3 = Label(root, text = f"{value} mal {key}")
        myLabel3.pack(anchor = W)

#myLabel = Label(root, text=f"Voreinstellung: {pizza.get()}")
#myLabel.pack()

myButton = Button(root, text="Click", command=lambda: clicked(pizza.get()))
myButton.pack()
myButton2 = Button(root, text = "Liste", command = lambda: alle(pizza.get()))
myButton2.pack()

root.mainloop()

# Ergebnisse anzeigen
print("Auswahl-Liste:", Liste_pizza)
```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_42.py", line 2, in <module>
    from PIL import ImageTk, Image
ModuleNotFoundError: No module named 'PIL'

```

## NEU_43.py

### Code
```python
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
# Hauptfenster erstellen

root = Tk()
root.title("Spielfeld mit Ergebnis-Liste speichern")


def popup():
 #   messagebox.showinfo("This is Popup.", "Hallo world")
 #   messagebox.showerror("This is Popup.", "Hallo world")
 #   messagebox.askquestion("This is Popup.", "Hallo world")
#    messagebox.askokcancel("This is Popup.", "Hallo world")
    #response = messagebox.askokcancel("This is Popup.", "Hallo world")
    # response = messagebox.askquestion("This is Popup.", "Hallo world")
     response = messagebox.showerror("This is Popup.", "Hallo world")

     Label(root, text = response).pack()
    # if response == 1:
   #     Label(root, text = "You clicked yes").pack()
  #   else:
   #     Label(root, text = "Clicked no").pack()

Button(root, text = "Popup", command = popup).pack()


root.mainloop()


```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_43.py", line 2, in <module>
    from PIL import ImageTk, Image
ModuleNotFoundError: No module named 'PIL'

```

## NEU_44.py

### Code
```python
from tkinter import *
from tkinter import PhotoImage

from PIL import ImageTk, Image

# Hauptfenster erstellen

root = Tk()
root.title("Spielfeld mit Ergebnis-Liste speichern")

def open():
    top = Toplevel()
    top.title("Learn to code")
    img = ImageTk.PhotoImage(Image.open(r"C:\Users\nikla\Downloads\Hornbach.jpg"))
    label = Label(top, image=img)
    label.image = img  # Referenz speichern!
    label.pack()
    Button(top, text="Close Window", command=top.destroy).pack()


btn = Button(root, text = "Open Second Window", command = open).pack()


root.mainloop()

```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_44.py", line 4, in <module>
    from PIL import ImageTk, Image
ModuleNotFoundError: No module named 'PIL'

```

## NEU_45.py

### Code
```python
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

# Hauptfenster erstellen
root = Tk()
root.title("Spielfeld mit Ergebnis-Liste speichern")

def open_file():
    # Dateidialog öffnen
    root.filename = filedialog.askopenfilename(
        initialdir="C:\\Users\\nikla\\Downloads\\",
        title="Select a file",
        filetypes=(("png files", "*.png"), ("all files", "*.*"))
    )

    # Label aktualisieren, nachdem der Benutzer eine Datei ausgewählt hat
    if root.filename:
        my_label.config(text=f"Ausgewählte Datei: {root.filename}")

        # Bild laden und anzeigen
        img = Image.open(root.filename)
        my_image = ImageTk.PhotoImage(img)

        # Bild-Label aktualisieren oder neues Label erstellen
        my_image_label.config(image=my_image)
        my_image_label.image = my_image  # Referenz speichern, damit das Bild nicht gelöscht wird
    else:
        my_label.config(text="Keine Datei ausgewählt.")

# Label für Dateiname erstellen (initial leer)
my_label = Label(root, text="Noch keine Datei ausgewählt.")
my_label.pack(pady=20)

# Button zum Öffnen des Dialogs hinzufügen
my_button = Button(root, text="Datei auswählen", command=open_file)
my_button.pack(pady=20)

# Platzhalter für Bild
my_image_label = Label(root)
my_image_label.pack(pady=20)

root.mainloop()
```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_45.py", line 2, in <module>
    from PIL import ImageTk, Image
ModuleNotFoundError: No module named 'PIL'

```

## NEU_46.py

### Code
```python
from tkinter import *
from PIL import ImageTk, Image


# Hauptfenster erstellen
root = Tk()
root.title("Spielfeld mit Ergebnis-Liste speichern")
root.geometry("400x400")

vertical = Scale(root, from_ = 0, to = 200)
vertical.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

horizontal = Scale(root, from_ = 0, to = 400, orient = HORIZONTAL)
horizontal.pack()

my_label = Label(root, text = horizontal.get()).pack()


my_btn = Button(root, text = "Click", command = slide).pack()

root.mainloop()
```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_46.py", line 2, in <module>
    from PIL import ImageTk, Image
ModuleNotFoundError: No module named 'PIL'

```

## NEU_47.py

### Code
```python
from tkinter import *

root = Tk()
root.title("Canvas")
root.geometry("500x500")

my_canvas = Canvas(root, width = 300, height = 200, bg = "white")
my_canvas.pack(pady = 20)

#x1 y1 x2 y2
my_canvas.create_rectangle(50, 150, 250, 50, fill = "pink")
my_canvas.create_oval(50, 150, 250, 50, fill = "cyan")
my_canvas.create_line(0, 100, 300, 100, fill = "red")
my_canvas.create_line(150, 0, 150, 200, fill = "red")

def show():
    myLabel = Label(root, text = var.get()).pack()

def show_2():
    myLabel = Label(root, text = clicked.get()).pack()

var = StringVar()

c = Checkbutton(root, text = "Check box", variable = var, onvalue = "Pizza", offvalue = "Off")
c.deselect()
c.pack()


options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

clicked = StringVar()
clicked.set(options[0])

myButton = Button(root, text = "Show Selection", command = show).pack()

drop = OptionMenu(root, clicked, *options)
drop.pack()


myButton_2 = Button(root, text = "Show Selection", command = show_2).pack()
root.mainloop()
```

### Ausgabe
_Keine Ausgabe_

## NEU_48.py

### Code
```python
from tkinter import Tk, Canvas

liste = [2, 4, 6]
liste_2 = [3, *liste]
print(liste_2)

def create_board():
    # Hauptfenster erstellen
    root = Tk()
    root.title("Mensch ärgere dich nicht - Spielfeld")
    canvas_size = 600
    cell_size = 50
    offset = 100

    # Canvas erstellen
    canvas = Canvas(root, width=canvas_size, height=canvas_size, bg="white")
    canvas.pack()

    # Farben für die Spieler
    colors = {
        "red": "red",
        "blue": "blue",
        "green": "green",
        "yellow": "yellow",
    }

    # Startfelder erstellen (Ecken)
    def draw_start_area(x, y, color):
        for i in range(2):
            for j in range(2):
                canvas.create_oval(
                    x + i * cell_size + 5,
                    y + j * cell_size + 5,
                    x + (i + 1) * cell_size - 5,
                    y + (j + 1) * cell_size - 5,
                    fill=color,
                    outline="black"
                )

    # Spielfeldfelder zeichnen (Raster)
    def draw_board():
        for row in range(7):
            for col in range(7):
                x1 = offset + col * cell_size
                y1 = offset + row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size

                if (row in [0, 6] or col in [0, 6]) and not (row in [0, 6] and col in [0, 6]):
                    canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

    # Zielfelder zeichnen (Zentrale Linie)
    def draw_home_area():
        for i in range(4):
            canvas.create_rectangle(
                offset + 3 * cell_size,
                offset + (i + 1) * cell_size,
                offset + 4 * cell_size,
                offset + (i + 2) * cell_size,
                fill="gray",
                outline="black",
            )
            canvas.create_rectangle(
                offset + (i + 1) * cell_size,
                offset + 3 * cell_size,
                offset + (i + 2) * cell_size,
                offset + 4 * cell_size,
                fill="gray",
                outline="black",
            )

    # Spielfeld erstellen
    draw_board()

    # Startbereiche in den Ecken
    draw_start_area(0, 0, colors["red"])
    draw_start_area(canvas_size - 2 * cell_size, 0, colors["blue"])
    draw_start_area(0, canvas_size - 2 * cell_size, colors["green"])
    draw_start_area(canvas_size - 2 * cell_size, canvas_size - 2 * cell_size, colors["yellow"])

    # Zielfelder zeichnen
    draw_home_area()

    # Hauptfenster starten
    root.mainloop()


# Spielfeld erstellen
create_board()
```

### Ausgabe
```
[3, 2, 4, 6]

```

## NEU_49.py

### Code
```python
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

from docutils.nodes import address

root = Tk()
root.title("Canvas")
root.geometry("400x600")


conn = sqlite3.connect("address_book.db")


c = conn.cursor()
# EINMAL einlesen reicht
'''
c.execute("""CREATE TABLE addresses (
           first_name text,
           last_name text,
           address text,
           city text,
           state text,
           zipcode integer
           )""")
'''

def edit():
    editor = Tk()
    editor.title("Update A Record")
    editor.geometry("400x300")

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = delete_box.get()

    if not record_id.isdigit():
        error_label = Label(editor, text="Ungültige ID! Bitte eine Zahl eingeben.", fg="red")
        error_label.grid(row=0, column=0)
        return

    # c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    c.execute("SELECT * from addresses WHERE oid = ?",  (record_id,))
    records = c.fetchall()
    print(records)

    if not records:
        error_label = Label(editor, text="Keine Daten für diese ID gefunden.", fg="red")
        error_label.grid(row=0, column=0)
        return

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)

    address_name_editor = Entry(editor, width=30)
    address_name_editor.grid(row=2, column=1, padx=20)

    city_name_editor = Entry(editor, width=30)
    city_name_editor.grid(row=3, column=1, padx=20)

    state_name_editor = Entry(editor, width=30)
    state_name_editor.grid(row=4, column=1, padx=20)

    zipcode_name_editor = Entry(editor, width=30)
    zipcode_name_editor.grid(row=5, column=1, padx=20)


    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))

    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)

    address_name_label_editor = Label(editor, text="Address")
    address_name_label_editor.grid(row=2, column=0)

    city_name_label_editor = Label(editor, text="City")
    city_name_label_editor.grid(row=3, column=0)

    state_name_label_editor = Label(editor, text="State")
    state_name_label_editor.grid(row=4, column=0)

    zipcode_name_label_editor = Label(editor, text="Zipcode")
    zipcode_name_label_editor.grid(row=5, column=0)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_name_editor.insert(0, record[2])
        city_name_editor.insert(0, record[3])
        state_name_editor.insert(0, record[4])
        zipcode_name_editor.insert(0, record[5])

    def save_record():
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()
        c.execute("""UPDATE addresses SET
            first_name = ?,
            last_name = ?,
            address = ?,
            city = ?,
            state = ?,
            zipcode = ?
            WHERE oid = ?""", (
            f_name_editor.get(),
            l_name_editor.get(),
            address_name_editor.get(),
            city_name_editor.get(),
            state_name_editor.get(),
            zipcode_name_editor.get(),
            record_id
        ))
        conn.commit()
        conn.close()
        editor.destroy()  # Editor-Fenster schließen

    save_btn_editor = Button(editor, text="Save Record", command=save_record)
    save_btn_editor.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=144)

    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    c.execute("DELETE from addresses WHERE oid = ?",  (delete_box.get(),))
    conn.commit()
    conn.close()



def submit():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address_name, :city_name, :state_name, :zipcode_name) ",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address_name': address_name.get(),
                  'city_name': city_name.get(),
                  'state_name': state_name.get(),
                  'zipcode_name': zipcode_name.get(),
              })


    conn.commit()

    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address_name.delete(0, END)
    city_name.delete(0, END)
    state_name.delete(0, END)
    zipcode_name.delete(0, END)

def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    #print(records)

    print_records = ""
    for record in records:
        # Breitere Werte angepasst: erste Spalte 10 Zeichen, zweite Spalte 15 Zeichen, dritte Spalte 5 Zeichen
        print_records += f"{record[0]:<10} {record[1]:<15} {record[6]:>5}\n"

    query_label = Label(root, text=print_records, font=("Courier", 10), justify=LEFT, anchor="w")
    query_label.grid(row=11, column=0, columnspan=2, pady=50)

    conn.commit()
    conn.close()

f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20, pady = (10, 0))

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1, padx = 20)

address_name = Entry(root, width = 30)
address_name.grid(row = 2, column = 1, padx = 20)

city_name = Entry(root, width = 30)
city_name.grid(row = 3, column = 1, padx = 20)

state_name = Entry(root, width = 30)
state_name.grid(row = 4, column = 1, padx = 20)

zipcode_name = Entry(root, width = 30)
zipcode_name.grid(row = 5, column = 1, padx = 20)

delete_box = Entry(root, width = 30)
delete_box.grid(row = 9, column = 1, pady = 5)



f_name_label = Label(root, text = "First Name")
f_name_label.grid(row = 0, column = 0, pady = (10, 0))

l_name_label = Label(root, text = "Last Name")
l_name_label.grid(row = 1, column = 0)

address_name_label = Label(root, text = "Address")
address_name_label.grid(row = 2, column = 0)

city_name_label = Label(root, text = "City")
city_name_label.grid(row = 3, column = 0)

state_name_label = Label(root, text = "State")
state_name_label.grid(row = 4, column = 0)

zipcode_name_label = Label(root, text = "Zipcode")
zipcode_name_label.grid(row = 5, column = 0)

delete_box_label = Label(root, text = "Select ID")
delete_box_label.grid(row = 9, column = 0, pady = 5)



submit_btn = Button(root, text = "Add Record To Database", command = submit)
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, ipadx = 110)

query_btn = Button(root, text = "Show records", command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 138)

delete_btn = Button(root, text = "Delete Record", command = delete)
delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

edit_btn = Button(root, text = "Edit Record", command = edit)
edit_btn.grid(row = 12, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 144)








conn.commit()

conn.close()

root.mainloop()
```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_49.py", line 2, in <module>
    from PIL import ImageTk, Image
ModuleNotFoundError: No module named 'PIL'

```

## NEU_5.py

### Code
```python
import csv
import io
import pandas as pd

data = """
Name, Adresse, Größe
Hans, Straße 33, 55
Peter,      Weg 10, 100
"""

# Daten aus dem String einlesen
file = io.StringIO(data)
reader = csv.reader(file)

# Leerzeichen entfernen und Daten in eine Liste von Listen konvertieren
cleaned_data = [[cell.strip() for cell in row] for row in reader]

# Bereinigte Daten ausgeben
for row in cleaned_data:
    print(row)



# Daten aus dem String in einen Pandas DataFrame einlesen und Leerzeichen entfernen
file = io.StringIO(data)
df = pd.read_csv(file, skipinitialspace=True)

# Bereinigte Daten als Tabelle anzeigen
print(df)

df["Gewicht"] = [44, 55]
print(df)

new_row = pd.DataFrame([["Jan", "Gasse 11", 88, 99]], columns=["Name", "Adresse", "Größe", "Gewicht"])
df = pd.concat([df, new_row], ignore_index = True)
print(df)

df.loc[len(df)] = ["Kurt", "Platz 1", 45, 77]
print(df)
print(df.dtypes)

daten = ["A", "B", "C", "E"]
daten.insert(3, "D")
print(daten)

print(daten.index("C"))

# Gegebene Liste
liste = ["A", "B", "C", "A"]

# Indizes aller "A" finden
indices = [index for index, value in enumerate(liste) if value == "A"]

# Indizes ausgeben
print(indices)

tupel = "EINS", "ZWEI"
print(tupel)

dict = {"Peter": 3}
print(dict)

print(dict.get("Peter"))

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Wertebereich definieren
x = np.linspace(-4, 4, 1000)

# Dichtefunktion der Standardnormalverteilung berechnen
y = norm.pdf(x)

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$\frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}$', color='blue')
plt.title('Standardnormalverteilung')
plt.xlabel('x')
plt.ylabel('Dichte')
plt.legend()
plt.grid(True)
plt.show()









```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_5.py", line 3, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'

```

## NEU_50.py

### Code
```python
from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root = Tk()
root.title('CODE')
root.geometry('600x100')

def zipLookup():
    #zip.get()
    #zipLabel = Label(root, text = zip.get())
    #zipLabel.grid(row = 1, column = 0, columnspan = 2)

    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=6B49D5D2-FED1-41F6-9C76-9AABA93CBEAB")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(bg=weather_color)

        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Halvetica", 15),
                        bg=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        api = "Error..."
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=6B49D5D2-FED1-41F6-9C76-9AABA93CBEAB




zip = Entry(root)
zip.grid(row = 0, column = 0, sticky=W+E+N+S)

zipButton = Button(root, text="Lookup Zipcode", command = zipLookup)
zipButton.grid(row = 0, column = 1)


root.mainloop()



```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_50.py", line 2, in <module>
    from PIL import ImageTk, Image
ModuleNotFoundError: No module named 'PIL'

```

## NEU_51.py

### Code
```python
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Code")
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()

my_button = Button(root, text = "Graph it.", command = graph)
my_button.pack()

root.mainloop()


```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_51.py", line 2, in <module>
    from PIL import ImageTk, Image
ModuleNotFoundError: No module named 'PIL'

```

## NEU_52.py

### Code
```python
from jovian.pythondsa import evaluate_test_case, binary_search
from jovian.pythondsa import evaluate_test_cases

# an welcher stelle ist eine bestimmte zahl in liste?

liste = [13, 11, 10, 7, 4, 3, 1, 0]
def locate_card(cards, query):
    k = 0
    for i in cards:
        if i != query:
            k += 1
        else:
            break
    return k

print(locate_card(liste, 7))

test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

print(locate_card(**test['input']) == test['output'])

tests = []
tests.append(test)
tests.append({
'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

tests.append({
'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

tests.append({
'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

tests.append({
'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

tests.append({
'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

tests.append({
'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

tests.append({
'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

tests.append({
'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

print(tests)
print("--------------")
def locate_card_2(cards, query):
    if query not in cards:
        return -1
    if len(cards) == 0:
        return -1
    pos = 0
    print('cards:', cards)
    print('query:', query)

    while True:
        print('position:', pos)

        if cards[pos] == query:
            return pos

        pos += 1

        if pos == len(cards):
            return -1

print("+++++")
result = locate_card_2(test['input']['cards'], test['input']['query'])

print("MMMMM")
print(result == test['output'])

print("*****")
evaluate_test_case(locate_card_2, test)

print("HHHHH")
for test in tests:
    print(locate_card(**test['input']) == test['output'])

print("----")
print(evaluate_test_cases(locate_card_2, tests))
print(44444)
def locate_card_3(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

print(tests[5])

print("---------")
print(locate_card_3([], 7))

print(evaluate_test_cases(locate_card_3, tests))
print("NNNNNNNEEEEEE")
# zb 9 7 5 4 3 2 1
def locate_card_4(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        print("lo:", lo, "hi:", hi, "mid:", mid,
              "mid_number:", mid_number)
        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            hi = mid - 1
        elif cards[mid] > query:
            lo = mid + 1

    return - 1

print(evaluate_test_cases(locate_card_4, tests))




print('-----------g-----------')
print(evaluate_test_case(locate_card_4, tests[8]))


def test_location(cards, query, mid):
    mid_number = cards[mid]
   # print("mid:", mid, ". mid_number:", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
       # print("lo:", lo, "hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid -1
        elif result == 'right':
            lo = mid + 1
    return -1


print(evaluate_test_case(locate_card, tests[8]))


# linear extrem test case

def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

large_test = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998

}

result, passed, runtime = evaluate_test_case(locate_card_linear, large_test, display=False)
print(f"RESULT {result}, PASSED {passed}, RUNTIME {runtime}")

print("_________________")
result, passed, runtime = evaluate_test_case(locate_card, large_test, display=False)
print(f"RESULT {result}, PASSED {passed}, RUNTIME {runtime}")


def test_location(cards, query, mid):
    mid_number = cards[mid]
   # print("mid:", mid, ". mid_number:", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'


print("iiiiiiiiiiiiiiiiiii")
def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) //2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def locate_card(cards, query):

    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'


    return binary_search(0, len(cards) - 1, condition)

print(evaluate_test_cases(locate_card, tests))
print(333)
def first_position(nums, target):

    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums) - 1, condition)

def last_position(nums, target):

    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid + 1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums) - 1, condition)

def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)


```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_52.py", line 1, in <module>
    from jovian.pythondsa import evaluate_test_case, binary_search
  File "C:\Users\nikla\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\jovian\__init__.py", line 9, in <module>
    from jovian.utils.initialize import _initialize_jovian
  File "C:\Users\nikla\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\jovian\utils\initialize.py", line 2, in <module>
    from jovian.utils.latest import check_update
  File "C:\Users\nikla\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\jovian\utils\latest.py", line 4, in <module>
    from pkg_resources import parse_version
ModuleNotFoundError: No module named 'pkg_resources'

```

## NEU_53.py

### Code
```python
# Ein Dictionary erstellen
student = {
    "name": "Anna",
    "age": 23,
    "subjects": ["Mathematics", "Physics", "Chemistry"]
}

# Zugriff auf Werte mithilfe der Keys
print(student["name"])  # Ausgabe: Anna
print(student["age"])   # Ausgabe: 23
print(student["subjects"])  # Ausgabe: ['Mathematics', 'Physics', 'Chemistry']

# Ein bestimmtes Fach aus der Liste der Fächer abrufen
print(student["subjects"][1])  # Ausgabe: Physics

# Hinzufügen eines neuen Key-Value-Paares
student["graduation_year"] = 2025
print(student)

# Überprüfen, ob ein Key existiert
if "name" in student:
    print("Name ist vorhanden.")
else:
    print("Name fehlt.")

# Ein Dictionary erstellen
person = {
    "name": "Niklas",
    "age": 25,
    "city": "Köln"
}

# Wert abrufen mit .get()
name = person.get("name")  # Gibt "Niklas" zurück
print(name)

# Key existiert nicht, Standardwert zurückgeben
country = person.get("country", "Deutschland")  # Gibt "Deutschland" zurück
print(country)

# Key existiert nicht, ohne Standardwert
job = person.get("job")  # Gibt None zurück
print(job)

print("-------------------------------------")

print('F' + 'G')

print("Fisch")
line = '*'
max_length = 10
while len(line) <= max_length:
    print(line)
    line += '*'
while len(line) > 0:
    print(line)
    line = line[:-1]

print("Fisch reverse")

max_length = 6
k, l = 0, 6
while k <= max_length:
    print(" " * l, "*" * k)
    k += 1
    l -= 1
max_length = 6
k, l = 0, 6
while k <= max_length:
    print(" " * (7-l), "*" * (5-k))
    k += 1
    l -= 1

# print(515 434 353 272 191 0110)
print("Raute")
k = 5
l = 1
while l <= 11:
    print(" " * k, "*" * l, " " * k)
    k -= 1
    l += 2

k = 1
l = 9
while l > 0:
    print(" " * k, "*" * l, " " * k)
    l -= 2
    k += 1

for i in range(5):
    if i == 2:
        continue
    print(i)


def error():
    ''' teste errordivision'''
    try:
        result = 5/0
        print("success")
    except ZeroDivisionError:
        print("Failed divided zero")
        result = 5
        return result

print(error())


k = 0
l = 5
for i in range(5):
    print("" * k,"*" * l )
    k += 1
    l -= 1

k = 1
l = 4
for i in range(5):
    print(" " * l,"-" * k, " " * l )
    k += 2
    l -= 1

k = 7
l = 1
for i in range(4):
    print(" " * l,"-" * k, " " * l )
    k -= 2
    l += 1


k = [print(i) for i in range(5)]
print("___")
k = [print(i) for i in range(5) if i % 2 == 0 and i != 2]

liste_rot = [5, 6, 9, 0, 2, 3, 4]

def rot_fkt(liste, anzahl_rot):
    liste_neu = [0] * len(liste)
    k = 0
    for i in liste:
        if k < 3:
            liste_neu[k + anzahl_rot] = i
        else:
            liste_neu[k + anzahl_rot -7] = i
        k += 1
    return liste_neu

print(rot_fkt(liste_rot, 4))

def rot_fkt(liste, anzahl_rot):
    liste_neu = [0] * len(liste)  # Neue Liste mit Nullen
    for k in range(len(liste)):
        # benutze %, also Rest:
        # 4%7 4, 5%7 5, 6%7 6, 7%7 0, 8%7 1, 9%7 2, 10%7 3
        neue_pos = (k + anzahl_rot) % len(liste)
        liste_neu[neue_pos] = liste[k]
    return liste_neu

print(rot_fkt(liste_rot, 4))

ergebnis = [a-b for a, b in zip([1,2,4], [2,3,3])]
print(ergebnis)

lis = [5,7,9,11,2,3,4]
lis_n = (lis[-1], *lis)
print(lis_n)

lis_n = [*lis[-1:], *lis[:-1]]
print(lis[-1:])
print(lis[:-1])
print(lis_n)  # → [4, 5, 7, 9, 11, 2, 3]

lis = [5, 7, 9, 11, 2, 3, 4]
lisn = [1, 2, 3, 4, 5, 6, 7]

differenz = [a - b for a, b in zip(lis, lisn)]
print(differenz)
print(444)
liste = [4, 5, 6, 7, -3, -3, -3]
index = next(i for i, val in enumerate(liste) if val < 0)
print(index)


import numpy as np
result = np.array(lis) - np.array(lisn)
print(result)
```

### Ausgabe
```
Anna
23
['Mathematics', 'Physics', 'Chemistry']
Physics
{'name': 'Anna', 'age': 23, 'subjects': ['Mathematics', 'Physics', 'Chemistry'], 'graduation_year': 2025}
Name ist vorhanden.
Niklas
Deutschland
None
-------------------------------------
FG
Fisch
*
**
***
****
*****
******
*******
********
*********
**********
***********
**********
*********
********
*******
******
*****
****
***
**
*
Fisch reverse
       
      *
     **
    ***
   ****
  *****
 ******
  *****
   ****
    ***
     **
      *
       
        
Raute
      *      
     ***     
    *****    
   *******   
  *********  
 *********** 
  *********  
   *******   
    *****    
     ***     
      *      
0
1
3
4
Failed divided zero
5
 *****
 ****
 ***
 **
 *
     -     
    ---    
   -----   
  -------  
 --------- 
  -------  
   -----   
    ---    
     -     
0
1
2
3
4
___
0
4
[0, 2, 3, 4, 5, 6, 9]
[0, 2, 3, 4, 5, 6, 9]
[-1, -1, 1]
(4, 5, 7, 9, 11, 2, 3, 4)
[4]
[5, 7, 9, 11, 2, 3]
[4, 5, 7, 9, 11, 2, 3]
[4, 5, 6, 7, -3, -3, -3]
444
4

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_53.py", line 184, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

```

## NEU_54.py

### Code
```python
# binary search

from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases


liste_rot = [5, 6, 9, 0, 2, 3, 4]

def rot_fkt(liste, anzahl_rot):
    if min(liste) == liste[0]:
        return 0
    else:
        k = [0] * len(liste)
        for i in range(len(liste)):
            k[i] = liste[i-anzahl_rot]
        return k

print(rot_fkt(liste_rot, 4))




liste_rot = [5, 6, 9, 0, 2, 3, 4]

def rot_fkt(liste):
   n = 0
   if liste[0] == 0:
    return n
   else:
        while min(liste) != liste[0]:
            k = [0] * len(liste)
            for i in range(len(liste)):
                k[i] = liste[i-1]
            liste = k
            n += 1
        return n

print(rot_fkt(liste_rot))

liste_blau = [0, 2, 3, 4, 5, 6, 9]


# RECHTSRUM rotieren
print('-------------- RECHTSRUM ----------------')


def count_rotations_rechts(nums):
   rotations = 0
   while min(nums) != nums[0]:
        k = [0] * len(nums)
        for i in range(len(nums)):
            k[i] = nums[i-1]
        nums = k
        rotations += 1
   return rotations

print(count_rotations_rechts(liste_blau), count_rotations_rechts(liste_rot))

# LINKSRUM rotieren
print('-------------- LINKSRUM ----------------')

def count_rotations(nums):
   rotations = 0
   while min(nums) != nums[0]:
        k = [0] * len(nums)
        for i in range(len(nums)-1):
            k[i] = nums[i+1]
        k[len(nums)-1] = nums[0]
        nums = k
        rotations += 1
   return rotations

print(count_rotations(liste_blau), count_rotations(liste_rot))

test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

print(evaluate_test_case(count_rotations, test))

# zwei Listen zu einer zusammengepackt
liste_test = [3,4,5,6]
liste_dazu = [7,8,9]

liste_zsm = [*liste_test, *liste_dazu]

test0 = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}


test1 = {
    'input': {
        'nums': [4, 5, 6, 7, 8, 1, 2, 3]
    },
    'output': 5
}

test2 = {
    'input': {
        'nums': [3, 5, 6, 7, 9, 11, 14, 19, 25, 29]
    },
    'output': 0
}

test3 = {
    'input': {
        'nums': [40, 3, 5, 6, 7, 9, 11, 14, 19, 25, 29]
    },
    'output': 1
}

test4 = {
    'input': {
        'nums': [5, 6, 7, 9, 11, 14, 19, 25, 29, 3]
    },
    'output': 9
}

test5= {
    'input': {
        'nums': [3, 5, 6, 7, 9, 11, 14, 19, 25, 29]
    },
    'output': 0
}

test6= {
    'input': {
        'nums': []
    },
    'output': 0
}

test7= {
    'input': {
        'nums': [3]
    },
    'output': 0
}
tests = [f"test{i}" for i in range(7)]
print("---")
print(tests)
print("'''''''''''''")


tests_k = [test0, test1, test2, test3, test4, test5, test6, test7]
tests = [test0, test1, test3, test5]

print(evaluate_test_cases(count_rotations, tests))

print(test4["input"]["nums"])
print("+++")
def differenz(nums):
    verschobene_liste = [nums[-1]] + nums[:-1]
    ergebnis = [a - b for a, b in zip(verschobene_liste, nums)]
    position = [i for i, val in enumerate(ergebnis) if val > 0]
    rotations = position[0]
    return rotations


list_tesst = [2,3,4,5,1]
print(differenz(list_tesst))

print('11111111111')
print(evaluate_test_cases(count_rotations, tests))
print("2222222222222222")
print(evaluate_test_cases(differenz, tests))

def count_rotations_linear(nums):
    position = 0

    while position < len(nums):
        if position > 0 and nums[position] < nums[position-1]:
            return position

        position += 1

    return 0

print("33333333333333")
print(evaluate_test_cases(count_rotations_linear, tests))

print("44444444444")
list_links = [5,1,2,3,4]
list_rechts = [2,3,4,5,1]
list_tst = [3,4,5,1,2]
list_o = [1,2,3,4,5]
list_list = [4,5,1,2,3]
def count_rotations_linear2 (nums):
    lo, hi = 0, len(nums)-1
    while lo < hi:
        mitte = (lo + hi) // 2
       # print(lo, mitte, hi)
        if nums[mitte] < nums[mitte-1]:
            return mitte
        elif(nums[lo] < nums[mitte]) and (nums[mitte] < nums[hi]):
            return 0
        elif  nums[mitte] < nums[hi]:
            hi = mitte - 1
        else:
            lo = mitte + 1

    return lo

print(count_rotations_linear2(list_links))
print(count_rotations_linear2(list_rechts))
print(count_rotations_linear2(list_tst))
print(count_rotations_linear2(list_o))
print(count_rotations_linear2(list_list))

print("TTTTTEEEEEESSSSSSTTTTTT")
print(evaluate_test_cases(count_rotations_linear2, tests_k))










```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_54.py", line 3, in <module>
    from jovian.pythondsa import evaluate_test_case
  File "C:\Users\nikla\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\jovian\__init__.py", line 9, in <module>
    from jovian.utils.initialize import _initialize_jovian
  File "C:\Users\nikla\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\jovian\utils\initialize.py", line 2, in <module>
    from jovian.utils.latest import check_update
  File "C:\Users\nikla\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\jovian\utils\latest.py", line 4, in <module>
    from pkg_resources import parse_version
ModuleNotFoundError: No module named 'pkg_resources'

```

## NEU_55.py

### Code
```python
from os import times
import time
import numpy as np

a = [1,2,3]
b = [10, 20, 30]

def Summ(a, b):
    result = 0
    for x, y in zip(a, b):
        result += x * y
    return result
print(Summ(a, b))

kanto = [73, 67, 43]
johto = [91, 88, 64]
hoenn = [87, 134, 58]
sinnoh = [102, 43, 37]
unova = [69, 96, 70]

w1, w2, w3 = 0.3, 0.2, 0.5
weights = [w1, w2, w3]

kanto_temp = 73
kanto_rainfall = 67
kanto_humidity = 43

kanto_yield_apples = kanto_temp*w1 + kanto_rainfall*w2 + kanto_humidity*w3
print(kanto_yield_apples)

def crop_yield(region, weights):
    result = 0
    for x, y in zip(region, weights):
        result += x * y
    return result

print(crop_yield(johto, weights))

kanto_np = np.array([73, 67, 43])
print(kanto_np)
weights_np = np.array([w1, w2, w3])

print(np.dot(kanto, weights))
print((kanto_np * weights_np).sum())

arr1 = list(range(1000000))
arr2 = list(range(1000000, 2000000))

arr1_np = np.array(arr1)
arr2_np = np.array(arr2)

print("-------------")


start_time = time.time()
# Dein Code hier
result = 0
for x1, x2 in zip(arr1, arr2):
    result += x1 * x2
print(result)
end_time = time.time()
print("Dauer:", end_time - start_time, "Sekunden")
print(33333344444444555555555)
print(f"Laufzeit: {end_time - start_time:.5f} Sekunden")

start_time2 = time.time()
print(np.dot(arr1_np, arr2_np))
end_time2 = time.time()
print(f"Laufzeit: {end_time2 - start_time2:.5f} Sekunden")

x = [1,2,3]
x.extend([4,5,6])
y = x + [7,8,9]
print(y)

dic = {"Name": "Nik", "Alter": 40, "Groeße": 180}
print(dic.keys(), dic.values())
print(dic["Name"])

zaehlen = [0 for i in range(4)]
zaehlen2 = [0 for _ in range(4)]
print(zaehlen, zaehlen2)

paare = [(x, y) for x in range(2,4) for y in range(11, 13)]
print(paare)

k = [2, 4, 6, 8]
dict = {}
for i in k:
    dict[i] = True

print(dict)

print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
class Set:

    def __init__(self, values = None):
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        return "Set: " + str(self.dict.keys())

    def add(self, value):
        self.dict[value] = True

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

s = Set([1,2,3])
s.add(4)
print(s.contains(4)) # True
s.remove(3)
print(s.contains(3)) # False
print(s.__repr__())
print(s)


def gutu(x, y):
    return 2 * x * y

print(list(map(gutu, [3, 4], [4, 5])))

result = map(gutu, [3, 4], [5, 6])
print(next(result))  # Gibt den ersten Wert aus: 30
print(next(result))  # Gibt den zweiten Wert aus: 48

durch_3 = [x for x in range(1, 101) if x % 3 == 0]
def durch6(x):
    return x % 6 == 0
list_6 = filter(durch6, durch_3)
print(list(list_6))

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print(letters, numbers)






```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_55.py", line 3, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

```

## NEU_56.py

### Code
```python
class User:

    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('User created')

    def introduce_yourself(self, guest_name):
        print(f"Hi {guest_name}, I am {self.name}, contact me at {self.email}")

    # __repr__() gibt eine technische Darstellung des Objekts zurück – nützlich für Debugging.

    def __repr__(self):
        return f"User(username = '{self.username}', name = '{self.name}', email = '{self.email}')"

# __str__() wird verwendet, wenn du print(user) aufrufst.
# hier gibt __str()__ das ergebnis von __repr()__ zurück

    def __str__(self):
        return self.__repr__()


# Erstellt ein neues Objekt user2
# Ausgabe: User created
user2 = User("john", "John Doe", "john@doe.com")
# Ausgabe: Hi David, I am John Doe, contact me at john@doe.com
user2.introduce_yourself("David")
print(1111111111)
user3 = User("jane", "Jane Doe", "jane@doe.com")
user3.introduce_yourself("David")
print(22222222)
user4 = User('jane', 'Jane Doe', 'jane@doe.com')
# print(user4) ruft __str__() auf → das wiederum ruft __repr__() auf → Ausgabe:
print(user4)
print(1111111)
class UserDatabase:
    # Konstruktor: initialisiert die Datenban mit einer leeren Liste namens users
    def __init__(self):
        self.users = []
    # Benutzer einfügen sortiert nach username
    # fügt neuen Benmutzer alphabetisch sortiert nach username ein in Liste
    # wenn zb user.username = "bernd", dann zwischen "armin" und "colin"

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    # Durchsucht die Liste nach einem Benutzer mit dem passenden username
    # Gibt das User -Objekt zurück, wenn gefunden
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    # Benutzer aktualisieren
    # Sucht Benutzer mit user.username und aktualisiert dessen name und email

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    # Alle Benutzer zurückgeben
    # Gibt die gesamte Benutzerliste zurück
    def list_all(self):
        return self.users

# Beispielobjekte, erstelle vier User -Objekte
armin = User('armin', 'Armin Aal', 'armin@web.de')
bernd = User('bernd', 'Bernd Brot', 'bernd@google.com')
colin = User('colin', 'Colin Col', 'colin@web.de')
david = User('david', 'david degen', 'david@google.com')

# Speichert sie in einer Liste - aber nicht in Datenbank UserDatabase.
# Muss noch mit insert() eingefügt werden.
users = [armin, bernd, colin, david]
# gibt Daten von bernd aus
print(bernd.username, bernd.email, bernd.name)
# vergleicht zwei Strings alphabetisch:
# "Abend" kommt vor "Bernd" -> Ergebnis: True
print("Abend" < "Bernd")



print('----------------------')
names = ['bernd', 'arndt', 'david', 'colin']
def sorted_list(users):
    liste = []
    # für jeden Namen wird eine Einfügeposition person_stelle gesucht.
    for person in users:
        person_stelle = 0
        # vergleicht person mit den bereits eingefügten Namen
        while person_stelle < len(liste):
            # solange person alphabetisch größer ist, wird person_stelle erhöht
            if person > liste[person_stelle]:
              person_stelle += 1
            # sobald ein größerer oder gleicher Name gefunden wird, wird Schleife abgebrochen
            else:
                break
        # führt eine gezielte Einfügung eines Elements (person) an einer bestimmten Position (person_stelle) in die Liste liste durch.
        liste.insert(person_stelle, person)

    return liste

print(sorted_list(names))


names = ['bernd', 'arndt', 'david', 'colin']
sorted_names = sorted(names)
print(sorted_names)

verdopple = lambda x: x * 2
print(verdopple(5))  # Ergebnis: 10
addiere = lambda a, b: a + b
print(addiere(3, 7))  # Ergebnis: 10
zahlen = [1, 2, 3, 4]
verdoppelt = list(map(lambda x: x * 2, zahlen))
print(verdoppelt)  # Ergebnis: [2, 4, 6, 8] lambda wird auf jedes element in liste zahlen angewendet
zahlen = [1, 2, 3, 4, 5, 6]
ungerade = list(filter(lambda x: x % 2 != 0, zahlen))
print(ungerade)  # Ergebnis: [1, 3, 5]


```

### Ausgabe
```
User created
Hi David, I am John Doe, contact me at john@doe.com
1111111111
User created
Hi David, I am Jane Doe, contact me at jane@doe.com
22222222
User created
User(username = 'jane', name = 'Jane Doe', email = 'jane@doe.com')
1111111
User created
User created
User created
User created
bernd bernd@google.com Bernd Brot
True
----------------------
['arndt', 'bernd', 'colin', 'david']
['arndt', 'bernd', 'colin', 'david']
10
10
[2, 4, 6, 8]
[1, 3, 5]

```

## NEU_57.py

### Code
```python
from collections import Counter
from matplotlib import pyplot as plt
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
# add a title
plt.title("Nominal GDP")
# add a label to the y-axis
plt.ylabel("Billions of $")
plt.show()


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
# bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]
# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")
# label x-axis with movie names at bar centers
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()


grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)
plt.bar([x - 4 for x in histogram.keys()], # shift each bar to the left by 4
     histogram.values(), # give each bar its correct height
 8) # give each bar a width of 8
plt.axis([-5, 105, 0, 5]) # x-axis from -5 to 105,
 # y-axis from 0 to 5
plt.xticks([10 * i for i in range(11)]) # x-axis labels at 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]
# we can make multiple calls to plt.plot
# to show multiple series on the same chart
plt.plot(xs, variance, 'g-', label='variance') # green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2') # red dot-dashed line
plt.plot(xs, total_error, 'b:', label='total error') # blue dotted line
# because we've assigned labels to each series
# we can get a legend for free
# loc=9 means "top center"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plt.scatter(friends, minutes)
# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
 plt.annotate(label,
 xy=(friend_count, minute_count), # put the label with its point
 xytext=(5, -5), # but slightly offset
 textcoords='offset points')
plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()

# seaborn ggplot  libraries for more


```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_57.py", line 2, in <module>
    from matplotlib import pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

```

## NEU_58.py

### Code
```python
height_weight_age = [70, # inches,
 170, # pounds,
40 ] # years

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]

a = [20, 30, 40]
b = [30, 40, 50]

print(vector_add(a, b))

A = [[1, 2, 3], # A has 2 rows and 3 columns
 [4, 5, 6]]
B = [[1, 2], # B has 3 rows and 2 columns
 [3, 4],
 [5, 6]]

def shape(A):
 num_rows = len(A)
 num_cols = len(A[0]) if A else 0 # number of elements in first row
 return num_rows, num_cols

print(shape(A))

print("_________")

def make_matrix(num_rows, num_cols, entry_fn):
 """returns a num_rows x num_cols matrix
 whose (i,j)th entry is entry_fn(i, j)"""
 return [[entry_fn(i, j) # given i, create a list
 for j in range(num_cols)] # [entry_fn(i, 0), ... ]
 for i in range(num_rows)] # create one list for each i


def is_diagonal(i, j):
 """1's on the 'diagonal', 0's everywhere else"""
 return 2 if i == j else 0
print(is_diagonal(5,5))

identity_matrix = make_matrix(5, 5, is_diagonal)
print(identity_matrix)


```

### Ausgabe
```
[50, 70, 90]
(2, 3)
_________
2
[[2, 0, 0, 0, 0], [0, 2, 0, 0, 0], [0, 0, 2, 0, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 2]]

```

## NEU_59.py

### Code
```python
# Interview Master 100
# Summe aus 2 Zahlen einer Liste muss genau 9 sein-
# gib beide indices an. es müssen verschiedene zahlen sein.
from collections import Counter


num = [2,3,4,3,4,3,6,5,3,4,5,3,5]
friend_counts = Counter(num)
print(friend_counts)
xs = range(101)
ys = [friend_counts[x] for x in xs]
print(list(xs))
print(ys)
print(len(num))

print("___________")
def addi(nums):
    pos = 0
    kos = pos + 1
    for zahl in nums:
        while kos < len(nums):
            if zahl + nums[kos] == 9:
                return [pos, kos]
            else:
                kos += 1
        pos += 1
        kos = pos + 1

    return -99



a = [2, 11, 15, 7]
b = [3, 2, 4, 1, 0, 7, 3]
c = [1, 2, 3, 2, 6, 22]

print(addi(a))
print(addi(b))
print(addi(c))

print('_______________')
def addi2(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            num_indices[num] = i
            print(num_indices)
            return [num_indices[complement], i]

        num_indices[num] = i
        print(num_indices)
    return []

print(addi2(a, 9))

hh = {"aa": "bb", "cc": "dd"}
print("aa" in hh)
print("bb" in hh)
stack = []
print(stack if not stack else 0)

print("___________")
def klammern_string(klammern) -> bool:
    dic = {')': '(', ']': '[', '}': '{'}
    offen = []
    for k in klammern:
        if k in dic:
            if not offen or offen[-1] != dic[k]:
                return [False, 77]
            offen.pop()
        else:
            offen.append(k)
    return len(offen) == 0

print(klammern_string("[()]"))
print(klammern_string("[()"))
print(klammern_string("][()"))
print(klammern_string("[(])"))

print('_______________')
def kl(string):
    dict = {')': '(', ']': '[', '}': '{'}
    bisher = []
    for i in string:
        if i in dict:
            if bisher == [] or bisher[-1] != dict[i]:
                return [False, 77]
            bisher.pop()
        else:
            bisher.append(i)

    return len(bisher) == 0

print(kl("[()]"))
print(kl("[()"))
print(kl("][()"))
print(kl("[(])"))

Liste1 = [1, 4, 5]
Liste2 = [2, 3, 6]

print('______+++______')
def listlist(list1, list2):
    Liste_neu = []
    i, k = 0, 0
    while i < len(list1) and k < len(list2):
        if list2[k] < list1[i]:
            Liste_neu.append(list2[k])
            k += 1
        else:
            Liste_neu.append(list1[i])
            i += 1



    return Liste_neu

print(listlist(Liste1, Liste2))






def sumtest(data):
    for a in range(len(data) - 1):
        b = a + 1
        while b < len(data):
            if data[a] + data[b] == 10:
                return a, b
            b += 1
    return -1, -1

v = [1,2,3,4,5,6]
print(sumtest(v))



d = [2, 4, 5, 6, 8]
def test(x):
    if x == 4:
        return 99
    else:
        return x

print(list(map(test, d)))


# if ... else ... goes before the for loop
d = [2, 4, 5, 6, 8]
fff = [99 if i == 4 else i for i in d]
print(fff)

import matplotlib.pyplot as plt
import pandas as pd

# 1. Daten definieren (basierend auf Ihrer Eingabe)
# Die Werte müssen als Dezimalzahlen (float) für die Grafik konvertiert werden
daten = {
    'Jahr': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Neuzulassungen': [3.20, 3.35, 3.44, 3.44, 3.61, 2.90, 2.62, 2.65, 2.83, 2.80]
}

df = pd.DataFrame(daten)

# 2. Grafik erstellen (Liniendiagramm für Zeitreihen)
plt.figure(figsize=(10, 6)) # Größe des Diagramms festlegen

# Liniendiagramm zeichnen
plt.plot(df['Jahr'], df['Neuzulassungen'], marker='o', linestyle='-', color='#0077b6')

# Höchstwert (2019) und Tiefstwert (2021) markieren und beschriften
plt.annotate(
    'Höchstwert (3.61 Mio.)',
    xy=(2019, 3.61),
    xytext=(2018.5, 3.7),
    arrowprops=dict(facecolor='red', shrink=0.05, width=1, headwidth=6),
    fontsize=9,
    color='red'
)
plt.annotate(
    'Tiefstwert (2.62 Mio.)',
    xy=(2021, 2.62),
    xytext=(2020.5, 2.45),
    arrowprops=dict(facecolor='green', shrink=0.05, width=1, headwidth=6),
    fontsize=9,
    color='green'
)

# 3. Grafik beschriften
plt.title('PKW-Neuzulassungen in Deutschland (2015–2024)', fontsize=14, fontweight='bold')
plt.xlabel('Jahr', fontsize=12)
plt.ylabel('Neuzulassungen (in Millionen)', fontsize=12)

# X-Achsen-Ticks als ganze Zahlen festlegen
plt.xticks(df['Jahr'], rotation=45, ha='right')

# Gitternetzlinien hinzufügen
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Layout anpassen und Grafik speichern/anzeigen
plt.tight_layout()
plt.savefig('neuzulassungen_grafik.png') # Grafik als PNG-Datei speichern

print("✅ Der Python-Code wurde ausgeführt. Die Grafik wurde als 'neuzulassungen_grafik.png' gespeichert.")
print("Um die Grafik anzuzeigen, benötigen Sie die lokalen Bibliotheken 'matplotlib' und 'pandas'.")
```

### Ausgabe
```
Counter({3: 5, 4: 3, 5: 3, 2: 1, 6: 1})
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
[0, 0, 1, 5, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
13
___________
[0, 3]
[1, 5]
[2, 4]
_______________
{2: 0}
{2: 0, 11: 1}
{2: 0, 11: 1, 15: 2}
{2: 0, 11: 1, 15: 2, 7: 3}
[0, 3]
True
False
[]
___________
True
False
[False, 77]
[False, 77]
_______________
True
False
[False, 77]
[False, 77]
______+++______
[1, 2, 3, 4, 5]
(3, 5)
[2, 99, 5, 6, 8]
[2, 99, 5, 6, 8]

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_59.py", line 155, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

```

## NEU_6.py

### Code
```python
dateiname = "Autotext-lesexn.JPG"
print(dateiname[1:])
print(dateiname[-3:])
print(dateiname.lower()[:-2])
print(dateiname[1:3])

name = "Autotext-lesen.JPG"
only_letters = ''.join([char for char in name if char.isalpha()])
print(only_letters)

name = "Autotext-lesen.JPG"
words = name.replace("-", " ").replace(".", " ").split()
print(words)

neu = " ".join(words)
print(neu)

text = "SCHRÖDINGER"
suche = "IN"
print(text.find(suche))

text = "SCHRÖDINGER"
suche = "INDE"
print(text.find(suche))  # -1, wenn nicht drinnen

neu = "exempeltext mit mehreren ex"
substring = "ex"
start = 0

while start < len(neu):
    pos = neu.find(substring, start) # beginnt such ab position start
    if pos == -1:
        break
    print("Gefunden an Position:", pos)
    start = pos + 1


neu = "exempeltext miiiiiiiiiiit mehreren ex"
substring = "ex"
start = 0

print("_______")


while start < len(neu):
    pos = neu.find(substring, start)
    if pos == -1:
        break
    print(pos)
    start = pos + 1


















```

### Ausgabe
```
utotext-lesexn.JPG
JPG
autotext-lesexn.j
ut
AutotextlesenJPG
['Autotext', 'lesen', 'JPG']
Autotext lesen JPG
6
-1
Gefunden an Position: 0
Gefunden an Position: 8
Gefunden an Position: 25
_______
0
8
35

```

## NEU_61.py

### Code
```python
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
```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_61.py", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

```

## NEU_62.py

### Code
```python
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
```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_62.py", line 2, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'

```

## NEU_63.py

### Code
```python
import numpy as np

# Funktion und Ableitung
def function(x):
    return x**2

def gradient(x):
    return 2*x  # Ableitung von f(x) = x^2

# Gradient Descent Parameter
learning_rate = 0.1  # Schrittweite
epochs = 50  # Anzahl der Iterationen
x_start = 10  # Startpunkt

# Initialisierung
x = x_start
history = []  # Speichert den Verlauf der Werte

# Gradient Descent Schleife
for _ in range(epochs):
    history.append(x)  # Verlauf speichern
    x -= learning_rate * gradient(x)  # Aktualisierung: x = x - lr * grad(x)

print("Minimiertes x:", x)
print("Historie:", history)

# Plot Verlauf
import matplotlib.pyplot as plt

plt.plot(history, marker='o', linestyle='-', color='blue')
plt.title("Verlauf von Gradient Descent")
plt.xlabel("Iteration")
plt.ylabel("x-Wert")
plt.grid(True)
plt.show()










```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_63.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

```

## NEU_64.py

### Code
```python
from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tag = soup.find('h5') # stops at first h5 element!
    courses_html_tags = soup.find_all('h5')
    for course in courses_html_tags:
        print(course.text)
    print('_________')
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print('_________---------------')
        print(f"{course_name} costs {course_price}")


import matplotlib.pyplot as plt
import numpy as np

# Beispiel-Daten für die Tabellen generieren
def create_random_data():
    return np.random.randint(1, 100, size=(5, 5))  # 5x5 Tabelle mit Zufallswerten

# Dashboard (3x2 Grid) erstellen
fig = plt.figure(figsize=(12, 8))  # Größe des Dashboards
grid = fig.add_gridspec(3, 2, wspace=0.4, hspace=0.6)  # 3x2 Grid mit Abständen

# 6 Tabellen aufteilen
for i in range(3):  # Zeilen
    for j in range(2):  # Spalten
        ax = fig.add_subplot(grid[i, j])  # Subplot für Tabelle
        ax.axis('tight')  # Grenzen anpassen
        ax.axis('off')  # Achsen deaktivieren
        data = create_random_data()  # Daten generieren
        table = ax.table(cellText=data, colLabels=[f"Spalte {k+1}" for k in range(5)],
                         loc='center', cellLoc='center', colColours=['#cccccc']*5)
        table.auto_set_font_size(False)  # Schriftgröße festlegen
        table.set_fontsize(8)  # Schriftgröße
        ax.set_title(f"Tabelle {i*2 + j + 1}")  # Titel jeder Tabelle

# Dashboard anzeigen
plt.show()



```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_64.py", line 1, in <module>
    from bs4 import BeautifulSoup
ModuleNotFoundError: No module named 'bs4'

```

## NEU_65.py

### Code
```python
import requests  # Die requests-Bibliothek wird importiert, um HTTP-Anfragen an eine Webseite zu senden.
from bs4 import \
    BeautifulSoup  # BeautifulSoup wird importiert, um die HTML-Inhalte der Webseite zu analysieren und zu durchsuchen.

# Die URL der Bundesliga-Tabelle auf der Sportschau-Webseite.
url = "https://www.sportschau.de/live-und-ergebnisse/fussball/deutschland-bundesliga/tabelle"

# Sende eine HTTP-GET-Anfrage, um die Inhalte der Webseite abzurufen.
response = requests.get(url)

# Überprüfe, ob die Anfrage erfolgreich war (Statuscode 200 bedeutet Erfolg).
if response.status_code == 200:
    # Analysiere die HTML-Inhalte der Webseite mit BeautifulSoup.
    soup = BeautifulSoup(response.content, "html.parser")

    # Suche nach dem ersten Tabellen-Element auf der Seite.
    # Dies ist nur ein Beispiel und sollte an die spezifische Struktur der Webseite angepasst werden.
    team_table = soup.find("table")  # Hier wird angenommen, dass die Tabelle als <table>-Element dargestellt wird.

    # Finde alle Tabellenzeilen (<tr>), um durch die Teams zu iterieren.
    rows = team_table.find_all("tr")

    # Iteriere durch jede Zeile in der Tabelle.
    for row in rows:
        # Überprüfe, ob der Name "Bayer Leverkusen" in der Zeile vorkommt.
        if "Bayer Leverkusen" in row.text:
            # Finde alle Tabellenspalten (<td>) in der aktuellen Zeile.
            columns = row.find_all("td")

            # Nimm an, dass die Punkte in der letzten Spalte der Tabelle stehen.
            points = columns[-1].text.strip()  # Extrahiere den Text und entferne zusätzliche Leerzeichen.

            # Gib die Punkte von Bayer Leverkusen aus.
            print(f"Bayer Leverkusen's points: {points}")
else:
    # Falls die Anfrage fehlschlägt, gib den HTTP-Statuscode aus.
    print("Failed to retrieve the webpage. Status code:", response.status_code)
```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_65.py", line 2, in <module>
    from bs4 import \
    ^^^^^^^^^^^^^^^^^
        BeautifulSoup  # BeautifulSoup wird importiert, um die HTML-Inhalte der Webseite zu analysieren und zu durchsuchen.
        ^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'bs4'

```

## NEU_66.py

### Code
```python
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python&cboWorkExp1=-1&txtLocation=').text


soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_ ="ui-tabs-active ui-state-active")

print(jobs)

#jobs_2 = soup.find_all('li', id = "expLiAnchor")
#print(jobs_2)

jobs = soup.find_all(class_ ="ui-tabs-active ui-state-active")
print(jobs)

#print(soup.prettify())  # Gibt den gesamten HTML-Code schön formatiert aus
# Um sicherzustellen, dass du den richtigen HTML-Code durchsuchst, kannst du die Inhalte ausgeben:

hh = soup.find_all('h2')
for element in hh:
    print(element.text)
    print(element.text.strip())





# Beispiel 1: Entfernen von Leerzeichen
text = "   Hallo Welt!   "
bereinigt = text.strip()
print(f"Original: '{text}'")
print(f"Bereinigt: '{bereinigt}'")

# Beispiel 2: Entfernen von bestimmten Zeichen
text2 = "###Python ist toll###"
bereinigt2 = text2.strip("#")
print(f"Original: '{text2}'")
print(f"Bereinigt: '{bereinigt2}'")
```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_66.py", line 1, in <module>
    from bs4 import BeautifulSoup
ModuleNotFoundError: No module named 'bs4'

```

## NEU_67.py

### Code
```python
import requests
from bs4 import BeautifulSoup

# URL der Webseite
url = "https://www.cbssports.com/nba/scoreboard/"

# HTTP-GET-Anfrage senden, um die Inhalte der Webseite abzurufen.
response = requests.get(url)

# Überprüfen, ob die Anfrage erfolgreich war.
if response.status_code == 200:
    # HTML-Inhalte analysieren
    soup = BeautifulSoup(response.content, "html.parser")

    # Suche nach dem Bereich, der die Spiele enthält
    games_container = soup.find_all("div", class_="scoreboard")  # Passe die Klasse je nach Struktur an

    for game in games_container:
        # Extrahiere Teamnamen, Punkte oder andere relevante Daten
        teams = game.find_all("div", class_="team")  # Beispiel: Suche nach Teamnamen
        for team in teams:
            print(team.text.strip())  # Ausgabe des Teamnamens

        # Punkte, Zeit oder Status des Spiels (Beispielstruktur)
        game_status = game.find("div", class_="game-status")  # Beispiel: aktueller Spielstatus
        print(game_status.text.strip() if game_status else "Status nicht verfügbar")
else:
    print("Fehler beim Abrufen der Webseite. Statuscode:", response.status_code)

```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_67.py", line 2, in <module>
    from bs4 import BeautifulSoup
ModuleNotFoundError: No module named 'bs4'

```

## NEU_68.py

### Code
```python
import requests
from bs4 import BeautifulSoup

# URL der ursprünglichen Seite
base_url = "https://example.com"

# HTTP-Header hinzufügen, um die Anfrage wie von einem Browser aussehen zu lassen
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

# Abrufen der ursprünglichen Seite
response = requests.get(base_url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Extrahiere die Links (aktualisiere den Selektor entsprechend der HTML-Struktur)
    links = soup.find_all("a", class_="relevant-class")  # Passe Klasse/Selektor an
    for link in links:
        href = link.get("href")
        if href:
            full_url = href if href.startswith("http") else f"{base_url.rstrip('/')}/{href.lstrip('/')}"

            # Neue Seite abrufen
            new_response = requests.get(full_url, headers=headers)
            if new_response.status_code == 200:
                new_soup = BeautifulSoup(new_response.content, "html.parser")

                # Titel oder andere relevante Inhalte finden
                title_tag = new_soup.find("title")
                if title_tag:
                    page_title = title_tag.text.strip()
                    print(f"Seite: {full_url} - Titel: {page_title}")
                else:
                    print(f"Kein Titel auf der Seite: {full_url}")
            else:
                print(f"Fehler beim Abrufen der Seite: {full_url}")
else:
    print("Fehler beim Abrufen der ursprünglichen Seite. Statuscode:", response.status_code)
```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_68.py", line 2, in <module>
    from bs4 import BeautifulSoup
ModuleNotFoundError: No module named 'bs4'

```

## NEU_69.py

### Code
```python
import requests
from bs4 import BeautifulSoup

response = requests.get('https://example.com')
print(response.text)  # Gibt den HTML-Inhalt der Seite als Text zurück


```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_69.py", line 2, in <module>
    from bs4 import BeautifulSoup
ModuleNotFoundError: No module named 'bs4'

```

## NEU_7.py

### Code
```python
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

```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_7.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

```

## NEU_70.py

### Code
```python
import requests  # Importieren der requests-Bibliothek, um HTTP-Anfragen zu stellen und Webseiten abzurufen.
from bs4 import BeautifulSoup  # BeautifulSoup wird importiert, um HTML- oder XML-Inhalte zu parsen und zu analysieren.

# Die URL der Zielwebseite wird definiert.
url = "https://niklasstat.github.io/Statistik_R/index_4.html"

# Ein Dictionary mit HTTP-Headern wird erstellt.
# Der `User-Agent` wird hinzugefügt, um die Anfrage wie von einem Browser aussehen zu lassen (manche Seiten blockieren automatisierte Anfragen).
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Senden einer HTTP-GET-Anfrage an die definierte URL. Die Header werden mitgeschickt, um die Anfrage "legitim" erscheinen zu lassen.
response = requests.get(url, headers=headers)

# Überprüfen, ob die Anfrage erfolgreich war. Ein Statuscode von 200 bedeutet Erfolg (HTTP 200 = "OK").
if response.status_code == 200:
    # Wenn die Anfrage erfolgreich war, wird der HTML-Inhalt der Webseite mit BeautifulSoup geparst.
    # Der `html.parser` wird als Parser verwendet, um den HTML-Code zu analysieren.
    soup = BeautifulSoup(response.content, "html.parser")

    # Alle HTML-Tags, die Überschriften enthalten können (<h1> bis <h6>), werden gesucht.
    headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

    # Überschriften werden gefiltert, um nur die Überschriften zu finden, die das Wort "Quersummen" enthalten.
    # `heading.text.strip()` entfernt überflüssige Leerzeichen aus den Textinhalten der Überschriften.
    quersummen_headings = [heading.text.strip() for heading in headings if "Quersummen" in heading.text]

    # Überprüfen, ob Überschriften gefunden wurden, die "Quersummen" enthalten.
    if quersummen_headings:
        print("Gefundene Überschriften mit 'Quersummen':")
        # Jede gefundene Überschrift wird nacheinander ausgegeben.
        for heading in quersummen_headings:
            print(heading)
    else:
        # Wenn keine Überschriften mit "Quersummen" gefunden wurden, wird eine entsprechende Nachricht ausgegeben.
        print("Keine Überschriften mit 'Quersummen' gefunden.")
else:
    # Falls die Anfrage fehlschlägt, wird der HTTP-Statuscode ausgegeben, um den Fehler zu diagnostizieren.
    print(f"Fehler beim Abrufen der Webseite. Statuscode: {response.status_code}")

# Eine zusätzliche Zeile wird ausgegeben, um das Ende der Skriptausführung zu markieren.
print('_______')
soup = BeautifulSoup(response.content, "html.parser")
headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

for element in headings:
    print(element.text)
    print(element.text.strip())
```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_70.py", line 2, in <module>
    from bs4 import BeautifulSoup  # BeautifulSoup wird importiert, um HTML- oder XML-Inhalte zu parsen und zu analysieren.
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'bs4'

```

## NEU_71.py

### Code
```python
# Dash-Bibliothek für die Web-App importieren
from dash import Dash, dcc, html

# Pandas für Datenverarbeitung
import pandas as pd

# NumPy für mathematische Berechnungen
import numpy as np

# Plotly Express für einfache Diagramme
import plotly.express as px

# Plotly Graph Objects für detaillierte Diagrammgestaltung
import plotly.graph_objects as go

# Plotly IO für das Speichern von Diagrammen
import plotly.io as pio

# Daten vorbereiten: Zwei Tabellen mit Beispielwerten erstellen
data1 = pd.DataFrame({'Spalte A': ['A1', 'A2', 'A3'], 'Wert': [10, 20, 30]})
data2 = pd.DataFrame({'Spalte B': ['B1', 'B2', 'B3'], 'Wert': [40, 50, 60]})

# Werte für die Normalverteilung erstellen: X-Werte von 50 bis 110 mit 100 Punkten
x_values = np.linspace(50, 110, 100)

# Normalverteilungsfunktion N(80,100) berechnen
y_values = (1 / np.sqrt(2 * np.pi * 100)) * np.exp(-((x_values - 80) ** 2) / (2 * 100))

# Dash-App initialisieren
app = Dash(__name__)

# Layout der Dash-App definieren
app.layout = html.Div([
    html.H1("Dashboard mit Grid"),  # Titel des Dashboards

    # Erste Zeile: Zwei Spalten für Tabellen
    html.Div([
        # Erste Spalte mit Tabelle 1
        html.Div([
            html.H3("Tabelle 1"),
            html.Table([
                # Tabellenkopf erstellen
                html.Tr([html.Th(col) for col in data1.columns])
            ] + [
                # Tabelleninhalt einfügen
                html.Tr([html.Td(data1.iloc[i][col]) for col in data1.columns]) for i in range(len(data1))
            ])
        ], style={'width': '50%', 'display': 'inline-block', 'backgroundColor': 'orange'}),

        # Zweite Spalte mit Tabelle 2
        html.Div([
            html.H3("Tabelle 2"),
            html.Table([
                html.Tr([html.Th(col) for col in data2.columns])  # Tabellenkopf
            ] + [
                html.Tr([html.Td(data2.iloc[i][col]) for col in data2.columns]) for i in range(len(data2))
            ])
        ], style={'width': '50%', 'display': 'inline-block'}),
    ]),

    # Zweite Zeile: Normalverteilungsplot in voller Breite
    html.Div([
        html.H3("Normalverteilungsplot N(80, 100)"),
        dcc.Graph(
            figure=px.line(x=x_values, y=y_values, title="Normalverteilung N(80,100)")
        )
    ], style={'width': '100%', 'marginTop': '20px'}),
])

# **2. Normalverteilungsplot speichern**
# Eine neue Plotly-Figur erstellen
fig = go.Figure()

# Normalverteilung als Linienplot hinzufügen
fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name="Normalverteilung N(80,100)"))

# Diagramm konfigurieren: Titel und Achsentitel setzen
fig.update_layout(title="Normalverteilung N(80,100)", xaxis_title="Werte", yaxis_title="Dichte")

# **Speicherung als JPG und PDF**
pio.write_image(fig, "normalverteilung.jpg")  # Speichert das Diagramm als JPG
pio.write_image(fig, "normalverteilung.pdf")  # Speichert das Diagramm als PDF

# Hauptfunktion: Startet die Dash-App
if __name__ == '__main__':
    app.run(debug=True)
```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_71.py", line 2, in <module>
    from dash import Dash, dcc, html
ModuleNotFoundError: No module named 'dash'

```

## NEU_72.py

### Code
```python
import requests
from bs4 import BeautifulSoup as bs
import re

# Load webpage content

r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

# Convert to a beautiful soup object

soup = bs(r.content, "lxml")

print(soup)
print("_______j___")
print(soup.prettify())

print('________g____')
first_header = soup.find("h2")
print(first_header)

headers = soup.find_all("h2")
print(headers)

print("------r-----")

first_header = soup.find(["h2", "h1"])
print(first_header)

headers = soup.find_all(["h1", "h2"])
print(headers)

print("-------e---")

headings = [tag.get_text(strip=True) for tag in soup.find_all(["h1", "h2"])]

print(headings)  # Gibt die Überschriften als Liste aus

paragraph = soup.find_all("p", attrs = {"id": "paragraph-id"})
print(paragraph)
print("___f__")
body = soup.find('body')
print(body)

print("_____b______")

div = body.find('div')
print(div)
print('------k---')
header = div.find('h1')
print(header)

paragraphs = soup.find_all("p", string = "Some bold text") # ganzer string muss passen
print(paragraphs)
print("_______n____")
paragraphs = soup.find_all("p", string = re.compile("Some")) # ganzer string muss passen
print(paragraphs)

print("_----f-------")
headers = soup.find_all("h2", string = re.compile("(H|h)eader"))
print(headers)

print("-------l-----")

content = soup.select("p") # bei css selektoren
print(content)

print("___________j________")

print(soup.body.prettify())

content = soup.select("div p") # paragraphs inside divs
print(content)








```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_72.py", line 2, in <module>
    from bs4 import BeautifulSoup as bs
ModuleNotFoundError: No module named 'bs4'

```

## NEU_73.py

### Code
```python
from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://www.sportschau.de/live-und-ergebnisse/fussball/deutschland-bundesliga/tabelle"

import cloudscraper
scraper = cloudscraper.create_scraper()
response = scraper.get(url)
#print(response.text)

#if response.status_code == 200:
   # soup = BeautifulSoup(response.text, "lxml")
  #  visible_text = soup.get_text(separator="\n", strip=True)  # Entfernt Tags
    #print(visible_text)
#else:
   # None
    #print(f"Fehler {response.status_code}: Zugriff nicht möglich.")


print('_________________')
 # Gibt nur den Text innerhalb des <h2>-Tags aus

soup = BeautifulSoup(response.text, "lxml")
heading = soup.find("h2")
print(heading.get_text(strip=True))

print("HH" if "h2" in response.text else "NOOO")


links = soup.find_all("a")
links = [l.get("href") for l in links]
links = [l for l in links]
print(links)




# Webseite abrufen
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "lxml")
table = soup.find("table")

rows = table.find_all("tr")
data = [[cell.get_text(strip=True) for cell in row.find_all(["th", "td"])] for row in rows]

df = pd.DataFrame(data)
print(df)


```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_73.py", line 1, in <module>
    from bs4 import BeautifulSoup
ModuleNotFoundError: No module named 'bs4'

```

## NEU_74.py

### Code
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt



def split_fg(value):
    if value == "-":
        return "-", "-"
    else:
        getroffen, geworfen = value.split("/")
        return int(getroffen), int(geworfen)  # Optional: In Integer umwandeln

def tg(getroffen, geworfen):
    if geworfen == 0 or geworfen == '-':
        return '-'
    else:
        return round((getroffen / geworfen), 2)

# Anwenden der Funktion auf die Spalte 'FG'


url = "https://www.cbssports.com/nba/scoreboard/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Alle Links mit "Box Score" im Text finden
box_score_links = [a['href'] for a in soup.find_all("a", string="Box Score")]

print(box_score_links)

for link in box_score_links:
    full_url = f"https://www.cbssports.com{link}"  # Falls relative Links
    response = requests.get(full_url)
    soup = BeautifulSoup(response.text, "html.parser")

    away_team_div = soup.find("div", id="player-stats-away")

    if away_team_div:
        player_names = [cell.get_text(strip=True) for cell in
                        away_team_div.find_all(["td", "a"], class_=["number-element", "name-truncate"])]
        print(f"Spieler des Auswärtsteams von {full_url}: {player_names}")
    else:
        print(f"⚠️ Keine Daten für das Auswärtsteam auf {full_url} gefunden.")

        # Beispiel: Spielernamen aus Tabellen suchen
   # header = soup.find("th")  # Falls die Spaltenüberschrift im ersten <th> steht

   # player_names = [header.get_text(strip=True)] + [cell.get_text(strip=True) for cell in soup.find_all(["td", "a"],
                                                                                                    #    class_=[
                                                                                                        #    "number-element",
                                                                                                       #    "name-truncate"])]

   # print(f"Spieler von {full_url}: {player_names}")

    headers = ['NAME', 'PTS', 'REB', 'AST', 'FG', '3PT', 'FT', 'PF', 'MIN', 'STL', 'BLK', 'TO', 'OREB', 'DREB', '+/-', 'FPTS']


    # Tabelle anzeigen

    #print(df.iloc[0:5])
    #print(df.iloc[5:10])
    #print(df)

    #print(df)
   # print(player_names[110])
   # print(player_names[189])
   # print(player_names[205])
  #  print(player_names[205 + 10 * 16])
  #  print(player_names[-16])


    # Liste der Spieler aus bestimmten Indizes
    selected_players = player_names[110:190] + player_names[205:-15]

    # Daten zeilenweise in 16er-Gruppen aufteilen
    rows = [selected_players[i:i + 16] for i in range(0, len(selected_players), 16)]

    # DataFrame erstellen
    df_a= pd.DataFrame(rows, columns=headers)

    # Tabelle anzeigen
    df_a[['Getroffen', 'Geworfen']] = df_a['FG'].apply(split_fg).apply(pd.Series)
    df_a['Trefferquote_Feld'] = df_a.apply(lambda row: tg(row['Getroffen'], row['Geworfen']), axis=1)

    df_a['Trefferquote_Feld'] = pd.to_numeric(df_a['Trefferquote_Feld'], errors='coerce')

    # Entferne Zeilen mit NaN-Werten aus `Trefferquote_Feld`
    df_a = df_a.dropna(subset=['Trefferquote_Feld'])

    # Ausgabe der neuen Tabelle

    print(df_a)

    anzahl_werte = df_a[df_a['Trefferquote_Feld'].apply(lambda x:
                                                        isinstance(x, (int, float)))]['Trefferquote_Feld'].ge(0).sum()

    print(f"Anzahl der Werte ≥ 0: {anzahl_werte}")

    x_values = range(1, anzahl_werte + 1)  # Neue x-Achsen-Werte für die Grafik

    # Erstellen der y-Werte (Trefferquote)
    y_values = df_a['Trefferquote_Feld'][0:anzahl_werte]

    # Spielernamen für die Beschriftung
    player_names = df_a['NAME'][0:anzahl_werte]

    print(x_values)
    print(y_values)
    print(player_names)

    # Balkendiagramm erstellen
    plt.figure(figsize=(12, 6))
    plt.bar(x_values, y_values, color="dodgerblue")

    # Namen neben die Balken setzen
    valid_data = df_a[df_a['Trefferquote_Feld'].apply(lambda x: isinstance(x, (int, float)))]

    for x, y, name in zip(valid_data.index, valid_data['Trefferquote_Feld'], valid_data['NAME']):
        plt.text(x + 1, y / 2, str(name), ha="center", va="center", fontsize=6, color="black", fontweight="bold")
    # Achsenbeschriftungen und Titel
    plt.xlabel("Spieler-Nummer")
    plt.ylabel("Trefferquote")
    plt.title("Trefferquote der Spieler Auswärts")

    # Grafik anzeigen
    plt.show()

for link in box_score_links:
    full_url = f"https://www.cbssports.com{link}"  # Falls relative Links
    response = requests.get(full_url)
    soup = BeautifulSoup(response.text, "html.parser")

    home_team_div = soup.find("div", id="player-stats-home")

    if home_team_div:
        player_names = [cell.get_text(strip=True) for cell in
                        home_team_div.find_all(["td", "a"], class_=["number-element", "name-truncate"])]
        print(f"Spieler des Heimteams von {full_url}: {player_names}")
    else:
        print(f"⚠️ Keine Daten für das Heimteam auf {full_url} gefunden.")

        # Beispiel: Spielernamen aus Tabellen suchen
   # header = soup.find("th")  # Falls die Spaltenüberschrift im ersten <th> steht

   # player_names = [header.get_text(strip=True)] + [cell.get_text(strip=True) for cell in soup.find_all(["td", "a"],
                                                                                                    #    class_=[
                                                                                                        #    "number-element",
                                                                                                       #    "name-truncate"])]

   # print(f"Spieler von {full_url}: {player_names}")

    headers = ['NAME', 'PTS', 'REB', 'AST', 'FG', '3PT', 'FT', 'PF', 'MIN', 'STL', 'BLK', 'TO', 'OREB', 'DREB', '+/-', 'FPTS']


    # Tabelle anzeigen

    #print(df.iloc[0:5])
    #print(df.iloc[5:10])
    #print(df)

    #print(df)
   # print(player_names[110])
   # print(player_names[189])
   # print(player_names[205])
    #print(player_names[205 + 10 * 16])
    #print(player_names[-16])


    # Liste der Spieler aus bestimmten Indizes
    selected_players = player_names[110:190] + player_names[205:-15]

    # Daten zeilenweise in 16er-Gruppen aufteilen
    rows = [selected_players[i:i + 16] for i in range(0, len(selected_players), 16)]

    # DataFrame erstellen
    df_h = pd.DataFrame(rows, columns=headers)
    #print(player_names)
    # Tabelle anzeigen
    #print(df_h)

    #print(df_h['FG'])
    df_h[['Getroffen', 'Geworfen']] = df_h['FG'].apply(split_fg).apply(pd.Series)
    df_h['Trefferquote_Feld'] = df_h.apply(lambda row: tg(row['Getroffen'], row['Geworfen']), axis=1)

    df_h['Trefferquote_Feld'] = pd.to_numeric(df_h['Trefferquote_Feld'], errors='coerce')

    # Entferne Zeilen mit NaN-Werten aus `Trefferquote_Feld`
    df_h = df_h.dropna(subset=['Trefferquote_Feld'])

    # Ausgabe der neuen Tabelle

    print(df_h)



    # Erstellen der x-Werte (Durchnummerierung)

    anzahl_werte = df_h[df_h['Trefferquote_Feld'].apply(lambda x:
                                                        isinstance(x, (int, float)))]['Trefferquote_Feld'].ge(0).sum()

    print(f"Anzahl der Werte ≥ 0: {anzahl_werte}")

    x_values = range(1, anzahl_werte + 1)  # Neue x-Achsen-Werte für die Grafik

    # Erstellen der y-Werte (Trefferquote)
    y_values = df_h['Trefferquote_Feld'][0:anzahl_werte]

    # Spielernamen für die Beschriftung
    player_names = df_h['NAME'][0:anzahl_werte]

    print(x_values)
    print(y_values)
    print(player_names)

    # Balkendiagramm erstellen
    plt.figure(figsize=(12, 6))
    plt.bar(x_values, y_values, color="dodgerblue")

    # Namen neben die Balken setzen
    valid_data = df_h[df_h['Trefferquote_Feld'].apply(lambda x: isinstance(x, (int, float)))]

    for x, y, name in zip(valid_data.index, valid_data['Trefferquote_Feld'], valid_data['NAME']):
        plt.text(x + 1 , y / 2, str(name), ha="center", va="center", fontsize=6, color="black", fontweight="bold")
    # Achsenbeschriftungen und Titel
    plt.xlabel("Spieler-Nummer")
    plt.ylabel("Trefferquote")
    plt.title("Trefferquote der Spieler Home")

# Grafik anzeigen
    plt.show()






```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_74.py", line 2, in <module>
    from bs4 import BeautifulSoup
ModuleNotFoundError: No module named 'bs4'

```

## NEU_75.py

### Code
```python

```

### Ausgabe
_Keine Ausgabe_

## NEU_76.py

### Code
```python
from tabulate import tabulate
import pandas as pd
import numpy as np
import random



daten = [
    {"Alter": 11, "Name": "Armin"},
    {"Alter": 12, "Name": "Bert"},
    {"Alter": 15, "Name": "Conrad"},
    {"Alter": 13, "Name": "David"},
    {"Alter": 14, "Name": "Emil"}
]

namen = [eintrag["Name"] for eintrag in daten if eintrag["Alter"] > 13]
print(namen)  # Ausgabe: ['Conrad', 'Emil']

del daten[0]

tabelle = tabulate(daten, headers="keys", tablefmt="grid")
print(tabelle)

# Sortieren nach Name in umgekehrter alphabetischer Reihenfolge
daten_sortiert = sorted(daten, key=lambda x: x["Name"], reverse=True)

# Ausgabe als schön formatierte Tabelle
tabelle = tabulate(daten_sortiert, headers="keys", tablefmt="grid")
print(tabelle)

numbers = [4,6,5,2,8,1]
numbers.sort() #alternativ in Klammern:   reverse = True
print(numbers)

gerade = [i for i in numbers if i%2 == 0]
print(gerade)

gerade_copy = gerade.copy()
print(gerade_copy)

my_data = {'name': 'Frank', 'age': 26, 'height': 1.95}
my_data.pop('name')
print(my_data)
del my_data['age']
print(my_data)

# array

data = np.array([[1,4], [2,5], [3,6]])

# dataframe

df = pd.DataFrame(data, index = ['row1', 'row1', 'row3'],
                   columns = ['col1','col2'])

print(df)

data = [[1,2],[2,3],[4,5]]

df = pd.DataFrame(data, index = ['row1', 'row1', 'row3'],
                   columns = ['col1','col2'])


print(df)

states = ['California', 'Texas', 'Florida', 'New York']
population = [39613493, 29730311, 21944577, 19299981]

# dictionary

dict_states = {'States': states, 'Population': population}

print(dict_states)

df_population = pd.DataFrame(dict_states)
print(df_population)

df_exams = pd.read_csv('statistische_kennwerte.csv')
print(df_exams.head())

df_exams = df_exams.rename(columns = {"Unnamed: 0": "Kennwerte"})
print(df_exams)

df_exams.columns = [df_exams.columns[0], "Grösse"] + list(df_exams.columns[2:])

print(df_exams)

df_exams = pd.read_csv('StudentsPerformance.csv')
print(df_exams.head(7))
print(df_exams.tail(7))

print(df_exams.isnull().values.sum()) # anzahl Missings values



# display n rows  alle reihen anzeigen

#  pd.set_option('display.max_rows', 1000)
#  print(df_exams)

print(df_exams.shape) # attribut
print(df_exams.index)

print(df_exams.columns)

print(df_exams.dtypes) # object = string

# methods


print(df_exams.head())
print(df_exams.info()) # no empty data

print(df_exams.describe())

# functions

print(len(df_exams))
print(max(df_exams.index), min(df_exams.index)) # niedrigester, höchster index

# selecting column

print(df_exams['gender'])

print(type(df_exams['gender']))
print(df_exams['gender'].index)

print(df_exams['math score'])
print(df_exams[['math score', 'gender']])

df_exams['language score'] = 70
print(df_exams)

language_score = np.arange(0, 1000)
print(len(language_score))
df_exams['language score'] = language_score
print(df_exams)

def klasse(zahl):
    parameter = 0
    if zahl < 334:
        parameter = 1
    elif zahl < 667:
        parameter = 2
    else:
        parameter = 3
    return parameter

print(klasse(222))
print(klasse(555))
print(klasse(888))

df_exams['parameter_123'] = df_exams['language score'].apply(klasse)
print(df_exams)

int_language_score = np.random.randint(1, 100, size = 1000)
print(min(int_language_score), max(int_language_score))

df_exams['language score'] = int_language_score
print(df_exams)

def klasse(zahl):
    parameter = 0
    if zahl < 34:
        parameter = 1
    elif zahl < 67:
        parameter = 2
    else:
        parameter = 3
    return parameter

df_exams['parameter_123'] = df_exams['language score'].apply(klasse)
print(df_exams)

df = pd.DataFrame({
    'Spalte_2': [3, 5, 6, 10],
    'Spalte_3': [2, 4, 5, 1]
})

# Funktion definieren
def berechne_spalte_4(row):
    if row['Spalte_2'] + row['Spalte_3'] < 10:
        return 99
    else:
        return 11

# apply auf Zeilenebene (axis=1)
df['Spalte_4'] = df.apply(berechne_spalte_4, axis=1)

# Ergebnis anzeigen
print(df)

# Beispiel-DataFrame
df = pd.DataFrame({
    'Spalte_2': [3, 5, 6, 10],
    'Spalte_3': [2, 4, 5, 1]
})

# Lambda-Ausdruck verwenden
df['Spalte_4'] = df.apply(lambda row: 99 if row['Spalte_2'] + row['Spalte_3'] < 10 else 11, axis=1)

# Ergebnis anzeigen
print(df)

print(np.random.uniform(1, 100, size = 100))

score1 = np.random.randint(1, 100, size = 1000)
score2 = np.random.randint(1, 100, size = 1000)

series1 = pd.Series(score1, index = np.arange(0, 1000))
series2 = pd.Series(score2, index = np.arange(0, 1000))

print(series1)

print(df_exams.assign(score1=series1, score2=series2))
print("----")
print(df_exams.iloc[:6, -1])
print(df_exams)

df_exams = df_exams.assign(score1=series1, score2=series2) # overwrite
print(df_exams)

df_exams.insert(1, 'test', series1)
print(df_exams)

df_exams = df_exams.assign(E = lambda x: x["math score"] + x["reading score"])
print(df_exams["E"])

print(df_exams['math score'].sum())

print(
df_exams['math score'].count(),
df_exams['math score'].mean(),
df_exams['math score'].std(),
df_exams['math score'].min(),
df_exams['math score'].max())

print(df_exams.describe())

print(df_exams['math score'] + df_exams['reading score'] + df_exams['writing score'])

df_exams['average'] = (df_exams['math score'] + df_exams['reading score'] + df_exams['writing score'])/3
print(df_exams.round(2))


print(len(df_exams['gender']), df_exams['gender'].count())


print(df_exams['gender'].value_counts())

print(df_exams['gender'].value_counts(normalize=True))

print(df_exams['gender'].value_counts())

print(df_exams['parental level of education'].value_counts())

print(df_exams['parental level of education'].value_counts(normalize = True).round(2))

print(df_exams.sort_values(by='average'))

print(df_exams[df_exams['gender'] == 'male'])

print(df_exams.sort_values(by='average', ascending=False))

print(df_exams.sort_values(by=['average', 'reading score'], ascending=False))

print(df_exams.sort_values(by=['average', 'reading score'], ascending=False,
                           inplace = True)) # updated in df_exams

print(df_exams.sort_values('race/ethnicity', ascending=True,
                           key = lambda x: x.str.lower()))


new_index = np.arange(0, 1000)

random.shuffle(new_index)

print(new_index)

df_exams['new_index'] = new_index
print(df_exams)

# neuen Index setzen
print("___")
df_exams.set_index('new_index', inplace=True)

print(df_exams)

df_exams.sort_index(ascending=True, inplace = True)
print(df_exams)

# rename column

df_exams.rename(columns = {'gender':'Gender'}, inplace = True)
print(df_exams)

df_exams.rename(columns = {'math score':'MS',
                           'reading score':'RS',
                           'writing score':'WS'}, inplace = True)

df_exams.drop(columns = ['score2', 'E', 'average', 'score1', 'parameter_123', 'language score', 'test'], inplace = True)

print(df_exams)

df_exams.rename(index={0:'A', 1:'B', 2:'C'}, inplace = True)

print(df_exams.head(3))








```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_76.py", line 1, in <module>
    from tabulate import tabulate
ModuleNotFoundError: No module named 'tabulate'

```

## NEU_77.py

### Code
```python
import pandas as pd

#https://www.football-data.co.uk/data.php

data = pd.read_csv('https://www.football-data.co.uk/mmz4281/2425/E0.csv')

#https://www.football-data.co.uk/mmz4281/2425/E0.csv
#https://www.football-data.co.uk/mmz4281/2425/E1.csv
#https://www.football-data.co.uk/mmz4281/2425/E2.csv
#https://www.football-data.co.uk/mmz4281/2425/E3.csv
#https://www.football-data.co.uk/mmz4281/2425/EC.csv

#print(data)


data.rename(columns = {'FTHG': 'home_goals',
                       'FTAG': 'away_goals'}, inplace = True)

print(data.iloc[:10,0:7])

print('https://www.football-data.co.uk/mmz4281/' +'2425' + '/' + 'E0' + '.csv')

root = 'https://www.football-data.co.uk/mmz4281/'

leagues2 = ['E0', 'E1', 'E2', 'E3', 'EC']

leagues = [f'E{i}' for i in range(0, 4)] + ['EC']
print(leagues)

for league in leagues2:
    print(f'https://www.football-data.co.uk/mmz4281/2425/{league}.csv')




data_all = []
for league in leagues2:
    df = pd.read_csv(f'https://www.football-data.co.uk/mmz4281/2425/{league}.csv')
    data_all.append(df)

print(data_all[0].iloc[0:5, :5])

print(data_all[0].columns.tolist())

print(data_all[0]['B365H'][:30])


print('https://www.football-data.co.uk/mmz4281/' +'2425' + '/' + 'E0' + '.csv')

leagues2 = ['E0', 'E1', 'E2', 'E3', 'EC']
frames = []

root = 'https://www.football-data.co.uk/mmz4281/'
for league in leagues2:
    df = pd.read_csv(root + '2425' + '/' + league + '.csv')
    frames.append(df)

print(frames)
print(len(frames))
print(frames[0])

leagues = ['E0', 'E2', 'E3']
frames = []

print('__________')
for league in leagues:
    for season in range(18, 24):
        df = pd.read_csv(root + str(season) + str(season+1) + '/' + league + '.csv', encoding = 'latin1')
        df.insert(1, 'season', season) # Als 2. Spalte die Saison, das Jahr in dem die Saison beginnt.
        frames.append(df)

print(len(frames))

print(frames[0])

df = frames[0]

# Kopie des DataFrames für separate Bearbeitung
df_home = df[['HomeTeam', 'FTHG', 'FTAG']].copy()
df_away = df[['AwayTeam', 'FTHG', 'FTAG']].copy()

# Umbenennen für konsistente Verarbeitung
df_home.columns = ['Team', 'GoalsFor', 'GoalsAgainst']
df_away.columns = ['Team', 'GoalsAgainst', 'GoalsFor']  # Auswärts: Tore umgekehrt

# Punkte berechnen
df_home['Points'] = df_home.apply(lambda row: 3 if row.GoalsFor > row.GoalsAgainst else (1 if row.GoalsFor == row.GoalsAgainst else 0), axis=1)
df_away['Points'] = df_away.apply(lambda row: 3 if row.GoalsFor > row.GoalsAgainst else (1 if row.GoalsFor == row.GoalsAgainst else 0), axis=1)

print(df_home)

# Alles zusammenfügen
df_all = pd.concat([df_home, df_away], ignore_index=True)
print(df_all)


# Gruppieren & zusammenfassen
table = df_all.groupby('Team').agg(
    Matches=('Points', 'count'),
    Wins=('Points', lambda x: (x == 3).sum()),
    Draws=('Points', lambda x: (x == 1).sum()),
    Losses=('Points', lambda x: (x == 0).sum()),
    GoalsFor=('GoalsFor', 'sum'),
    GoalsAgainst=('GoalsAgainst', 'sum'),
    Points=('Points', 'sum')
)
print('*****')
print(table)
# Tordifferenz berechnen
table['GoalDiff'] = table['GoalsFor'] - table['GoalsAgainst']

# Sortieren nach Punkten, dann Tordifferenz
table = table.sort_values(by=['Points', 'GoalDiff'], ascending=False)

# Index zurücksetzen für schöne Ausgabe
table = table.reset_index()

print(table)

import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'category': ['Electronics', 'Clothing', 'Electronics', 'Books', 'Clothing'],
    'sales': [1200, 900, 1500, 600, 750]
})

# Group by category and calculate mean sales
grouped_sales = df.groupby('category')['sales'].mean()
print(grouped_sales)

# Multiple aggregation methods
multi_agg = df.groupby('category').agg(
    Test = ('sales', 'mean'),
    Summe = ('sales', 'sum'),
    Anzahl = ('sales', 'count'),
    Groesser800 = ('sales', lambda x: (x > 800).sum())
)
print(multi_agg)

# Custom transformation
def sales_difference(x):
    return x - x.mean()

group_transform = df.groupby('category')['sales'].transform(sales_difference)
print(group_transform)

print('-------------')

dict_countries = {
    'Spanish La Liga': 'SP1', 'Spanish Segunda Division': 'SP2',
    'German Bundesliga': 'D1', 'English Premier League': 'E0',
    'English League 1': 'E2', 'English League 2': 'E3'
}

print(dict_countries['Spanish La Liga'])

dict_historical_data = {}

# leagues = ['E0', 'E2', 'E3']


for league in dict_countries:
    frames = []
    for season in range(18, 24):
        df = pd.read_csv(root + str(season) + str(season+1) + '/' + dict_countries[league] + '.csv', encoding = 'latin1')
        df.insert(1, 'season', season) # Als 2. Spalte die Saison, das Jahr in dem die Saison beginnt.
        frames.append(df)
    df_concat = pd.concat(frames)
    dict_historical_data[league] = df_concat

print(dict_historical_data)
print(len(dict_historical_data))
print(dict_historical_data.keys())
print(dict_historical_data['English Premier League'])
print(dict_historical_data['English Premier League'])
print(dict_historical_data['English Premier League'][dict_historical_data['English Premier League']['season']==18])












```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_77.py", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'

```

## NEU_78.py

### Code
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_laptops = pd.read_csv('laptop_price.csv', encoding='latin1')
print(df_laptops.head(3))


dd = df_laptops['Company']=="Apple"
print(dd.sum())
print(len(dd))

apple_rows = df_laptops[df_laptops['Company'] == "Apple"]
print(apple_rows.index.tolist())

print(df_laptops[dd])
print(df_laptops[dd].value_counts('Company'))


no_HP_rows = df_laptops[df_laptops['Company'] != "HP"]
print(df_laptops[df_laptops['Company'] != "HP"].value_counts('Company'))

print(no_HP_rows.index.tolist())

laptops_2000_rows = df_laptops[df_laptops['Price_euros'] > 2000]
print(laptops_2000_rows)

print(df_laptops['Price_euros'] > 2000)

df_laptops['Price_tier'] = np.where(df_laptops['Price_euros'] > 2000, 'Expensive', 'Cheap')
print(df_laptops.head())
print(df_laptops.value_counts('Price_tier'))

print(len(df_laptops[df_laptops['Inches'] > 15]))
df_laptops['Size30+'] = np.where(df_laptops['Inches'] > 15, 'Big', 'Small')
print(df_laptops.head())
print(df_laptops['Size30+'].value_counts())

print(df_laptops[(df_laptops['Company'] == 'Apple') & (df_laptops['Price_tier'] == 'Expensive')])

# and -> &  in PANDAS !!!!!!!!!!!!!!!
# or |



print((df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell'))

print(df_laptops[(df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell')].value_counts('Company'))

print(df_laptops[((df_laptops['Company'] == 'Apple') | (df_laptops['Company'] == 'Dell')) & (df_laptops['Price_euros'] > 2000)].value_counts('Company'))

conditions = [
    df_laptops['Price_euros'] > 3000,
    (df_laptops['Price_euros'] > 2000) & (df_laptops['Price_euros'] <= 3000),
    (df_laptops['Price_euros'] > 800) & (df_laptops['Price_euros'] <= 2000),
    df_laptops['Price_euros'] <= 800
]

values = ['Too Expensive', 'Expensive', 'Affordable', 'Cheap']

df_laptops['Preiskat'] = np.select(conditions, values, default='Unbekannt')
print(df_laptops['Preiskat'].value_counts())



conditions = [
    df_laptops['Inches'] > 16,
    (df_laptops['Inches'] > 14) & (df_laptops['Inches'] <= 16),
    (df_laptops['Inches'] > 12) & (df_laptops['Inches'] <= 14),
    df_laptops['Inches'] <= 12
]

values = ['Too Big', 'Big', 'Small', 'Too Small']

df_laptops['Groesse4'] = np.select(conditions, values, default='Unbekannt')
print(df_laptops['Groesse4'].value_counts())

print('----------------')
print(df_laptops['Company'].isin(['Apple', 'HP']))
print(df_laptops[df_laptops['Company'].isin(['Apple', 'HP'])].value_counts('Company'))

filter1 = df_laptops['TypeName'].isin(['Notebook', 'Ultrabook'])
filter2 = df_laptops['Company'].isin(['Apple', 'HP'])

print(df_laptops[filter1 & filter2].iloc[0:10,0:5])

print(df_laptops.duplicated('laptop_ID'))

print(df_laptops[df_laptops.duplicated('laptop_ID')])

print(df_laptops.duplicated(['Product', 'TypeName', 'Inches']))

print(df_laptops.duplicated(['Product', 'TypeName', 'Inches']).sum())

print(df_laptops[df_laptops.duplicated(['Product', 'TypeName', 'Inches'])].iloc[0:10, 0:5])

duplicated = df_laptops.duplicated(['Product', 'TypeName', 'Inches'])

print('++++++++')
print(df_laptops[duplicated].sort_values(['Product', 'TypeName']))

df_laptops = df_laptops.sort_values(['Company', 'Price_euros'])
print(df_laptops[['Price_euros', 'Company']])

print(df_laptops.value_counts('Company'))
duplicated_first = df_laptops.duplicated('Company', keep = 'first')

print(df_laptops[duplicated_first])

print(df_laptops[~duplicated_first]) # opposite

data_test = {
    'Name': ['Anna', 'Ben', 'Clara', 'Anna', 'Nik', 'Anna'],
    'Alter': [25, 30, 27, 28, 31, 25],
    'Stadt': ['Berlin', 'Köln', 'Hamburg', 'München', 'Stuttgart', 'Berlin']
}

df = pd.DataFrame(data_test)
print(df)

print(df.duplicated('Name'))
print(df[df.duplicated('Name')])
print(df[~df.duplicated('Name')])

print(df_laptops[~duplicated_first]) # opposite

# laptops with cheapest price since 1st value of sorted list was
# cheapest of Company and others are dupicats and deleted

print(df_laptops[~duplicated_first][['Company', 'Price_euros']])

print(df_laptops[~duplicated_first].value_counts('Company'))

# get last duplicated value
duplicated_last = df_laptops.duplicated('Company', keep = 'last')

print(df_laptops[~duplicated_last][['Company', 'Price_euros']])

print('------')

duplicated_false = df_laptops.duplicated('Company', keep = False)


# empty since only duplicated values
print(df_laptops[~duplicated_false][['Company', 'Price_euros']])
# proof
print(df_laptops.value_counts('Company'))

print(df_laptops.drop_duplicates(['Company'])[['Company', 'Price_euros']].value_counts('Company'))

df_laptops = df_laptops.sort_values(['Company', 'Price_euros'])
print(df_laptops.drop_duplicates(['Company'], keep = 'first')[['Company', 'Price_euros']])
df_laptops.drop_duplicates(['Company'], keep = 'last', inplace = True, ignore_index = True)
print(df_laptops[['Company', 'Price_euros']])


```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_78.py", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'

```

## NEU_79.py

### Code
```python
total = 0
for n in range(-1, 31):
    term = (1/5) ** (2 * n + 4)
    total += term

print(f"Summe der Reihe von n = -1 bis 30: {total:.10f}")



k = 2
N = 0
while True:
    Zahlen = [x for x in range(2,k)
              if all(x%y !=0 for y in range(2, int(x**0.5) + 1))]
    if len(Zahlen) < 11:
        k = k + 1
        N = len(Zahlen)
    else: break

print(Zahlen)



Zahlen2 = [x for x in range(2,3)
              if all(x%y !=0 for y in range(2, int(x**0.5) + 1))]

print(Zahlen2)

```

### Ausgabe
```
Summe der Reihe von n = -1 bis 30: 0.0416666667
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
[2]

```

## NEU_8.py

### Code
```python
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

```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_8.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

```

## NEU_9.py

### Code
```python
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

```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_9.py", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

```

## Test_1.py

### Code
```python
print("Hallo Welt")
import pandas as pd

data = {
    'Name': ['Anna', 'Bastian', 'Clara', 'David', 'Elena', 'Felix', 'Greta', 'Hans', 'Isabel', 'Jonas',
             'Klara', 'Lukas', 'Mara', 'Niklas', 'Olivia', 'Paul', 'Quentin', 'Rebecca', 'Samuel', 'Tina',
             'Uwe', 'Valerie', 'Wolfgang', 'Xenia', 'Yannik', 'Zoe', 'Alexander', 'Brigitte', 'Christian', 'Daniela'],
    'Alter': [25, 34, 28, 45, 32, 29, 31, 40, 27, 33, 35, 41, 30, 36, 29, 38, 26, 39, 37, 24,
              42, 43, 44, 23, 22, 28, 34, 27, 31, 32],
    'Größe': [165, 178, 172, 180, 168, 175, 169, 182, 163, 177,
              164, 181, 170, 179, 167, 176, 162, 183, 174, 160,
              185, 179, 184, 161, 159, 173, 180, 169, 178, 171],
    'Gewicht': [60, 75, 68, 82, 65, 70, 62, 80, 58, 72,
                59, 78, 66, 76, 64, 73, 57, 81, 74, 56,
                85, 77, 83, 55, 53, 67, 71, 63, 79, 69]
}

df = pd.DataFrame(data)
print(df)

```

### Ausgabe
```
Hallo Welt

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\Test_1.py", line 2, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'

```

## test.py

### Code
```python
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__)
app.layout = html.Div()
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)


```

### Ausgabe
```

[Fehler]
Traceback (most recent call last):
  File "C:\Users\nikla\PycharmProjects\pythonProject\test.py", line 1, in <module>
    from dash import Dash, html, dcc
ModuleNotFoundError: No module named 'dash'

```

