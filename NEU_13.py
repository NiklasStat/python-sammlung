import NEU_12 # import NEU_12 as N12
help(NEU_12)
print(NEU_12.fkt([6,7,8]))

print(NEU_12.wert_mal_faktor(7))
print(NEU_12.faktor)
NEU_12.faktor = 20
print(NEU_12.wert_mal_faktor(7))
print(NEU_12.letztes_ergebnis)
print("---------")
from random import uniform as mit_komma, randint
zufallszahl = mit_komma(1, 10)
print(randint(1, 10))

import pandas as pd
import numpy as np

# Beispiel-Daten
data = {
    'Größe': [175, 160, 180, 165, 170],
    'Gewicht': [70, 55, 80, 60, 75]
}

df = pd.DataFrame(data)

# Berechnungen
size_var = np.var(df['Größe'], ddof=1)
size_median = np.median(df['Größe'])
size_mean = np.mean(df['Größe'])
size_mode = df['Größe'].mode().iloc[0] if not df['Größe'].mode().empty else None
size_range = np.ptp(df['Größe'])

weight_var = np.var(df['Gewicht'], ddof=1)
weight_median = np.median(df['Gewicht'])
weight_mean = np.mean(df['Gewicht'])
weight_mode = df['Gewicht'].mode().iloc[0] if not df['Gewicht'].mode().empty else None
weight_range = np.ptp(df['Gewicht'])

# Ergebnisse in eine Tabelle einfügen
result_df = pd.DataFrame({
    '': ['Varianz', 'Median', 'Arithmetisches Mittel', 'Modus', 'Spannweite'],
    'Größe': [size_var, size_median, size_mean, size_mode, size_range],
    'Gewicht': [weight_var, weight_median, weight_mean, weight_mode, weight_range]
})

print(result_df)


# Beispiel-Daten
data = {
    'Größe': [175, 160, 180, 165, 170],
    'Gewicht': [70, 55, 80, 60, 75]
}

df = pd.DataFrame(data)

# Initialisiere Ergebnis-DataFrame
result_df = pd.DataFrame({
    '': ['Varianz', 'Median', 'Arithmetisches Mittel', 'Modus', 'Spannweite']
})

# Schleife durch alle numerischen Spalten
for column in df.select_dtypes(include=[np.number]).columns:
    var = np.var(df[column], ddof=1)
    median = np.median(df[column])
    mean = np.mean(df[column])
    mode = df[column].mode().iloc[0] if not df[column].mode().empty else None
    range_ = np.ptp(df[column])

    result_df[column] = [var, median, mean, mode, range_]

print(result_df)

# Beispiel-Daten
data = {
    'Größe': [175, 160, 180, 165, 170],
    'Geschlecht': ['männlich', 'weiblich', 'männlich', 'weiblich', 'männlich'],
    'Gewicht': [70, 55, 80, 60, 75]
}

df = pd.DataFrame(data)

# Initialisiere Ergebnis-DataFrame
result_df = pd.DataFrame({
    '': ['Varianz', 'Median', 'Arithmetisches Mittel', 'Modus', 'Spannweite']
})

# Schleife durch alle numerischen Spalten
for column in df.select_dtypes(include=[np.number]).columns:
    var = np.var(df[column], ddof=1)
    median = np.median(df[column])
    mean = np.mean(df[column])
    mode = df[column].mode().iloc[0] if not df[column].mode().empty else None
    range_ = np.ptp(df[column])

    result_df[column] = [var, median, mean, mode, range_]

# Speichern der Tabelle als CSV-Datei
result_df.to_csv('statistische_kennwerte.csv', index=False)

print("Daten erfolgreich gespeichert in 'statistische_kennwerte.csv'")

import os

print("Arbeitsverzeichnis:", os.getcwd())
