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
