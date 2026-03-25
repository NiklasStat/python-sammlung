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
