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