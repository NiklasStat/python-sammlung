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

# Hauptlogik: Vergleiche sicherstellen
def ensure_minimum_comparisons(min_comparisons=3):
    global elo_ratings

    # Verfolgen, wie oft jedes Bild in einem Vergleich vorkam
    comparison_counts = {image: 0 for image in images}
    pair_counts = {image: 0 for image in images}
    total_comparisons = 0

    while any(count < min_comparisons for count in comparison_counts.values()):
        # Zufällige Auswahl von zwei verschiedenen Bildern
        image_a, image_b = random.sample(images, 2)

        # Aktualisiere Paarzählungen für die beiden Bilder
        pair_counts[image_a] += 1
        pair_counts[image_b] += 1

        # Benutzerinteraktion
        print(f"Welches Bild gefällt dir besser? (1 für {image_a}, 2 für {image_b})")
        choice = input()

        if choice == "1":
            elo_ratings[image_a], elo_ratings[image_b] = update_elo(
                elo_ratings[image_a], elo_ratings[image_b], 1
            )
            comparison_counts[image_a] += 1
        elif choice == "2":
            elo_ratings[image_a], elo_ratings[image_b] = update_elo(
                elo_ratings[image_a], elo_ratings[image_b], 0
            )
            comparison_counts[image_b] += 1
        else:
            print("Ungültige Eingabe. Bitte wähle 1 oder 2.")
            continue  # Ungültige Eingaben überspringen

        total_comparisons += 1

    # Rangliste erstellen
    sorted_images = sorted(elo_ratings.items(), key=lambda x: x[1], reverse=True)
    print("\nRangliste der Bilder:")
    for rank, (image, rating) in enumerate(sorted_images, 1):
        print(f"{rank}. {image} (ELO: {rating:.1f})")

    # Vergleichsanzahl pro Bild anzeigen
    print("\nVergleichshäufigkeit pro Bild:")
    for image, count in pair_counts.items():
        print(f"{image}: {count} Mal im Paarvergleich verwendet")

    # Zeige die Gesamtzahl der Vergleiche an
    print(f"\nInsgesamt durchgeführte Vergleiche: {total_comparisons}")

# Starte die Vergleiche
ensure_minimum_comparisons(min_comparisons=3)
