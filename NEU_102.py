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
