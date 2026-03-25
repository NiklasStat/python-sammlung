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