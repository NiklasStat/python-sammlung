import random


# Funktion zur Optimierung der Pivot-Wahl (Median of Three)
def choose_pivot(arr):
    if len(arr) < 3:
        return arr[0]
    else:
        # Wähle drei zufällige Elemente und finde deren Median
        samples = random.sample(arr, 3)
        samples.sort()
        return samples[1]


# QuickSort-Algorithmus mit optimierter Pivot-Wahl
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Pivot intelligent wählen (Median-of-Three oder zufällig)
        pivot = choose_pivot(arr)
        arr.remove(pivot)  # Entferne das Pivot aus der Liste

        # Zwei Listen für "kleiner" und "größer"
        less_than_pivot = []
        greater_than_pivot = []

        for item in arr:
            # Vergleiche das aktuelle Element mit dem Pivot
            print(f"Vergleich: {item} mit {pivot}. (1 für kleiner, 2 für größer)")
            choice = input()
            if choice == "1":
                less_than_pivot.append(item)
            elif choice == "2":
                greater_than_pivot.append(item)
            else:
                print("Ungültige Eingabe. Bitte wähle 1 oder 2.")

        # Rekursive Aufrufe und Zusammenfügen der Listen
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


# Hauptfunktion
def start_comparison():
    print("Wie viele Elemente möchtest du sortieren?")
    n = int(input())

    # Generiere eine Liste von Zahlen oder Items
    items = [f"ITEM{i}" for i in range(1, n + 1)]
    random.shuffle(items)  # Zufällige Reihenfolge für einen realistischen Test

    print("\nStarte QuickSort mit den folgenden Elementen:")
    print(", ".join(items))

    # QuickSort ausführen
    sorted_items = quicksort(items)

    # Ergebnis anzeigen
    print("\nSortierte Reihenfolge:")
    for rank, item in enumerate(sorted_items, 1):
        print(f"{rank}. {item}")


# Programm starten
start_comparison()
