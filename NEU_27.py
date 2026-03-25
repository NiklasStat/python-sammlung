import itertools

# Liste der Bilder
bilder = [f"BILD{i}" for i in range(1, 11)]

# Alle möglichen Paare generieren, 2 für 2 Bilder, aber mehr auc möglich.
paare = list(itertools.combinations(bilder, 2))

# Ausgabe der Paare
for paar in paare:
    print(paar)


def vergleiche():

    counter = {bild: 0 for bild in bilder}
    total_comparisons = 0

    for bild_a, bild_b in paare:
        while True:
            #choice = input(f"wähle 1 für {bild_a} und 2 für {bild_b}: ")
            choice = "1"
            if choice == "1":
                counter[bild_a] += 1
                break
            elif choice == "2":
                counter[bild_b] += 1
                break
            else:
                print("Ungültige Eingabe. Bitte wähle 1 oder 2.")

        total_comparisons += 1
    return counter

print(vergleiche())
