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