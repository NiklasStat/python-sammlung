import matplotlib.pyplot as plt
import numpy as np

def plot_nv():
    while True:
        try:
            # Eingaben für Erwartungswert und Varianz abfragen
            #e_wert = float(input("Erwartungswert: "))
            #varianz = float(input("Varianz: "))
            e_wert = 100
            varianz = 25
            # Überprüfen, ob die Varianz positiv ist
            if varianz <= 0:
                raise ValueError("Die Varianz muss positiv sein.")

            # Daten erstellen
            x = np.linspace(e_wert - 5 * np.sqrt(varianz), e_wert + 5 * np.sqrt(varianz), 500)
            y = (1 / np.sqrt(2 * np.pi * varianz)) * np.exp(-((x - e_wert) ** 2) / (2 * varianz))

            # Plot erstellen
            plt.plot(x, y,
                     label=f'Normalverteilung ($\\mu$={e_wert},'
                           f' $\\sigma^2$={varianz})',
                     color='blue', linewidth=2)

            # Achsenbeschriftungen hinzufügen
            plt.xlabel('x-Wert')
            plt.ylabel('Dichte der NV')

            # Titel hinzufügen
            plt.title('Dichtefunktion der Normalverteilung')

            # Legende hinzufügen
            # Legende hinzufügen und in die rechte obere Ecke platzieren
            plt.legend(loc='upper right')

            # Gitter anzeigen (optional)
            plt.grid(True)

            # Plot anzeigen
            plt.show()

            # Beende die Schleife, wenn der Plot erfolgreich angezeigt wurde
            break

        except ValueError as ve:
            print(f"Fehler: {ve} Bitte erneut versuchen.")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}. Bitte erneut versuchen.")

# Funktionsaufruf
plot_nv()