daten = """
Name,Alter,Stadt
Anna,28,Berlin
Max,35,Hamburg
Sophie,22,München
Lukas,30,Köln
"""

# Daten in Zeilen aufteilen
zeilen = daten.strip().split('\n')

# Überschriften extrahieren
header = zeilen[0].split(',')

# Daten in eine Liste von Dictionaries umwandeln
personen = [
    {header[i]: eintrag for i, eintrag in enumerate(zeile.split(','))}
    for zeile in zeilen[1:]
]

# Ausgabe der eingelesenen Daten
for person in personen:
    print(person)

import pandas as pd

# Daten in einem Dictionary speichern
daten = {
    "Name": ["Anna", "Max", "Sophie", "Lukas"],
    "Alter": [28, 35, 22, 30],
    "Stadt": ["Berlin", "Hamburg", "München", "Köln"]
}

print(daten)
# DataFrame erstellen
df = pd.DataFrame(daten)
print(df)
wert_1 = df.iloc[3, 1]
wert_2 = df.iloc[3]
neue_zeile = pd.DataFrame([{'Name': 'Nik', 'Alter': '39', 'Stadt': 'Köln'}])

df = pd.concat([df, neue_zeile], ignore_index=True)
print(df)

neue_zeilen_2 = pd.DataFrame([
    {"Name": "AA", "Alter": 33, "Stadt": "Nürnberg"},
    {"Name": "BB", "Alter": 55, "Stadt": "München"}
])

df = pd.concat([df, neue_zeilen_2], ignore_index=True)
print(df)

df.loc[len(df)] = ["AA", 33, "Nürnberg"]
df.loc[len(df)] = ["BB", None, "München"]
print(df)


# Assuming 'df' is already defined and 'Alter' column exists

import pandas as pd
import numpy as np

# Assuming 'df' is already defined and 'Alter' column exists

# Convert the 'Alter' column to numeric, forcing non-numeric values to NaN
df['Alter'] = pd.to_numeric(df['Alter'], errors='coerce')

# Calculate the mean of the 'Alter' column, ignoring NaN values
mean_alter = df['Alter'].mean()

# Replace None and NaN values with the mean of the 'Alter' column
for i in range(len(df)):
    for j in range(df.shape[1]):
        if pd.isna(df.iloc[i, j]):
            df.iloc[i, j] = mean_alter
            print(df.iloc[i, j])

import statistics
import numpy as np

def boxpl(x):
    mean_value = statistics.mean(x)
    variance_value = statistics.variance(x)
    return mean_value, variance_value

# Generate 100 random numbers from the standard normal distribution
random_numbers = np.random.standard_normal(100)

# Call the function and print the result
mean, variance = boxpl(random_numbers)
print(f"Mean: {mean:.2f}, Variance: {variance:.2f}")

print(df)

df["Geschlecht"] = np.tile(["w", "m"], len(df) // 2 + 1)[:len(df)]

print(df)
print(5//2, 4//2, 3//2)
zahlen_liste = list(range(1, 101))
print(zahlen_liste)
zahlen_liste_2 = [x for x in range(1, 11)]
print(zahlen_liste_2)
df["Nummerierung"] = np.tile(zahlen_liste_2, 1)[:len(df)]
print(df)

df["Nummerierung"] = [i if i % 2 == 0 else 0 for i in df["Nummerierung"]]
print(df)

mean_by_gender = df.groupby(["Geschlecht", "Stadt"])["Alter"].mean()

print(mean_by_gender)