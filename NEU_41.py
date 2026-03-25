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