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