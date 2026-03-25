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