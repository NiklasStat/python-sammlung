import csv
import io
import pandas as pd

data = """
Name, Adresse, Größe
Hans, Straße 33, 55
Peter,      Weg 10, 100
"""

# Daten aus dem String einlesen
file = io.StringIO(data)
reader = csv.reader(file)

# Leerzeichen entfernen und Daten in eine Liste von Listen konvertieren
cleaned_data = [[cell.strip() for cell in row] for row in reader]

# Bereinigte Daten ausgeben
for row in cleaned_data:
    print(row)



# Daten aus dem String in einen Pandas DataFrame einlesen und Leerzeichen entfernen
file = io.StringIO(data)
df = pd.read_csv(file, skipinitialspace=True)

# Bereinigte Daten als Tabelle anzeigen
print(df)

df["Gewicht"] = [44, 55]
print(df)

new_row = pd.DataFrame([["Jan", "Gasse 11", 88, 99]], columns=["Name", "Adresse", "Größe", "Gewicht"])
df = pd.concat([df, new_row], ignore_index = True)
print(df)

df.loc[len(df)] = ["Kurt", "Platz 1", 45, 77]
print(df)
print(df.dtypes)

daten = ["A", "B", "C", "E"]
daten.insert(3, "D")
print(daten)

print(daten.index("C"))

# Gegebene Liste
liste = ["A", "B", "C", "A"]

# Indizes aller "A" finden
indices = [index for index, value in enumerate(liste) if value == "A"]

# Indizes ausgeben
print(indices)

tupel = "EINS", "ZWEI"
print(tupel)

dict = {"Peter": 3}
print(dict)

print(dict.get("Peter"))

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Wertebereich definieren
x = np.linspace(-4, 4, 1000)

# Dichtefunktion der Standardnormalverteilung berechnen
y = norm.pdf(x)

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$\frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}$', color='blue')
plt.title('Standardnormalverteilung')
plt.xlabel('x')
plt.ylabel('Dichte')
plt.legend()
plt.grid(True)
plt.show()








