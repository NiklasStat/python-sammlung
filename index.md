# Python Code Sammlung
Generiert am: 2026-03-25 20:41:08.387396

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
Counter({3: 6, 4: 6, 5: 3, 14: 3, 6: 2, 11: 2, 12: 2, 21: 2, 2: 1, 9: 1, 24: 1, 15: 1, 18: 1, 10: 1, 8: 1, 22: 1})
34 24 2 2 24
9.029411764705882
6.0
Counter({3: 6, 4: 6, 5: 3, 14: 3, 6: 2, 11: 2, 12: 2, 21: 2, 2: 1, 9: 1, 24: 1, 15: 1, 18: 1, 10: 1, 8: 1, 22: 1})
6
_____________
dict_keys([2, 3, 4, 5, 6, 9, 11, 14, 12, 21, 24, 15, 18, 10, 8, 22])
dict_values([1, 6, 6, 3, 2, 1, 2, 3, 2, 2, 1, 1, 1, 1, 1, 1])
dict_items([(2, 1), (3, 6), (4, 6), (5, 3), (6, 2), (9, 1), (11, 2), (14, 3), (12, 2), (21, 2), (24, 1), (15, 1), (18, 1), (10, 1), (8, 1), (22, 1)])
____________
[3, 4]
6.47365427278085
________
0.2533435821533203
_________--------
0.890332155496805
0.11578191198449861
0.04795275594335069
NNNNNNNNNNNNNNNNNNNN
1
0
0.1
0.30000000000000004
0.6
[1, 30] [2, 50] 0.30000000000000004 0.6

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
{'k', 'a', 'ü', 'b', 'h', 'c', 'o', 'e', 't', 'r', 'n', 'u'}
{'a': 2, 'u': 1, 't': 1, 'o': 1, 'b': 2, 'h': 1, 'n': 1, 'r': 1, 'ü': 1, 'c': 1, 'k': 1, 'e': 1}
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
{'d': 26, 'b': 6, 'e': 56, 'm': 32, 'u': 30, 'c': 12, 'y': 4, 'q': 2, 'r': 32, 'a': 46, 'i': 30, 'l': 22, 'o': 42, 'p': 10, 'j': 2, 't': 50, 'g': 8, 'v': 6, 'k': 4, 's': 38, 'n': 20}

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
C:\Users\nikla\PycharmProjects\pythonProject\NEU_10.py:6: RuntimeWarning: divide by zero encountered in divide
  return -1 / np.cbrt(x) * np.log(1 / (x + 1))

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
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_101.py", line 3, in <module>
    from sklearn.experimental import enable_iterative_imputer
ModuleNotFoundError: No module named 'sklearn'

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
  File "C:\Users\nikla\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\tensorflow\__init__.py", line 40, in <module>
    from tensorflow.python import pywrap_tensorflow as _pywrap_tensorflow  # pylint: disable=unused-import
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'tensorflow.python'

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
_Keine Ausgabe_

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
ReLU: 0.513993919380205
tanh: 0.4901370059852074
sigmoid: 0.5021350787800262

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
         x1        x2  y
0 -3.094166  1.737748  0
1 -1.500972  8.202048  0
2 -4.765768  2.226821  0
3 -0.693222  0.598575  0
4 -2.990707  3.492044  0
Epoch 0, Loss = 0.6817
Epoch 200, Loss = 0.5055
Epoch 400, Loss = 0.2863
Epoch 600, Loss = 0.1509
Epoch 800, Loss = 0.0951
Epoch 1000, Loss = 0.0706
Epoch 1200, Loss = 0.0563
Epoch 1400, Loss = 0.0468
Epoch 1600, Loss = 0.0400
Epoch 1800, Loss = 0.0350
Wahrscheinlichkeiten:
(-5.0, 0.0) -> 0.0003
(-3.9, 1.1) -> 0.0001
(-2.8, 2.2) -> 0.0002
(-1.7, 3.3) -> 0.9997
(-0.6, 4.4) -> 0.9998
(0.6, 5.6) -> 0.9997
(1.7, 6.7) -> 0.9958
(2.8, 7.8) -> 0.0461
(3.9, 8.9) -> 0.0001
(5.0, 10.0) -> 0.0001

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
  File "C:\Users\nikla\PycharmProjects\pythonProject\NEU_106.py", line 51, in <module>
    visualize_layer(net, layer_index=0, num_neurons=16, title_prefix="Layer 1")
                    ^^^
NameError: name 'net' is not defined. Did you mean: 'next'?

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
5
                          Größe  Gewicht
0                Varianz   62.5    107.5
1                 Median  170.0     70.0
2  Arithmetisches Mittel  170.0     68.0
3                  Modus  160.0     55.0
4             Spannweite   20.0     25.0
                          Größe  Gewicht
0                Varianz   62.5    107.5
1                 Median  170.0     70.0
2  Arithmetisches Mittel  170.0     68.0
3                  Modus  160.0     55.0
4             Spannweite   20.0     25.0
Daten erfolgreich gespeichert in 'statistische_kennwerte.csv'
Arbeitsverzeichnis: C:\Users\nikla\PycharmProjects\pythonProject

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
_Keine Ausgabe_

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
_Keine Ausgabe_

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
C:\Users\nikla\PycharmProjects\pythonProject\NEU_16.py:5: RuntimeWarning: invalid value encountered in log
  y = (1/np.tan(x))**(1/np.log(x))

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
