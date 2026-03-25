from tabulate import tabulate
import pandas as pd
import numpy as np
import random



daten = [
    {"Alter": 11, "Name": "Armin"},
    {"Alter": 12, "Name": "Bert"},
    {"Alter": 15, "Name": "Conrad"},
    {"Alter": 13, "Name": "David"},
    {"Alter": 14, "Name": "Emil"}
]

namen = [eintrag["Name"] for eintrag in daten if eintrag["Alter"] > 13]
print(namen)  # Ausgabe: ['Conrad', 'Emil']

del daten[0]

tabelle = tabulate(daten, headers="keys", tablefmt="grid")
print(tabelle)

# Sortieren nach Name in umgekehrter alphabetischer Reihenfolge
daten_sortiert = sorted(daten, key=lambda x: x["Name"], reverse=True)

# Ausgabe als schön formatierte Tabelle
tabelle = tabulate(daten_sortiert, headers="keys", tablefmt="grid")
print(tabelle)

numbers = [4,6,5,2,8,1]
numbers.sort() #alternativ in Klammern:   reverse = True
print(numbers)

gerade = [i for i in numbers if i%2 == 0]
print(gerade)

gerade_copy = gerade.copy()
print(gerade_copy)

my_data = {'name': 'Frank', 'age': 26, 'height': 1.95}
my_data.pop('name')
print(my_data)
del my_data['age']
print(my_data)

# array

data = np.array([[1,4], [2,5], [3,6]])

# dataframe

df = pd.DataFrame(data, index = ['row1', 'row1', 'row3'],
                   columns = ['col1','col2'])

print(df)

data = [[1,2],[2,3],[4,5]]

df = pd.DataFrame(data, index = ['row1', 'row1', 'row3'],
                   columns = ['col1','col2'])


print(df)

states = ['California', 'Texas', 'Florida', 'New York']
population = [39613493, 29730311, 21944577, 19299981]

# dictionary

dict_states = {'States': states, 'Population': population}

print(dict_states)

df_population = pd.DataFrame(dict_states)
print(df_population)

df_exams = pd.read_csv('statistische_kennwerte.csv')
print(df_exams.head())

df_exams = df_exams.rename(columns = {"Unnamed: 0": "Kennwerte"})
print(df_exams)

df_exams.columns = [df_exams.columns[0], "Grösse"] + list(df_exams.columns[2:])

print(df_exams)

df_exams = pd.read_csv('StudentsPerformance.csv')
print(df_exams.head(7))
print(df_exams.tail(7))

print(df_exams.isnull().values.sum()) # anzahl Missings values



# display n rows  alle reihen anzeigen

#  pd.set_option('display.max_rows', 1000)
#  print(df_exams)

print(df_exams.shape) # attribut
print(df_exams.index)

print(df_exams.columns)

print(df_exams.dtypes) # object = string

# methods


print(df_exams.head())
print(df_exams.info()) # no empty data

print(df_exams.describe())

# functions

print(len(df_exams))
print(max(df_exams.index), min(df_exams.index)) # niedrigester, höchster index

# selecting column

print(df_exams['gender'])

print(type(df_exams['gender']))
print(df_exams['gender'].index)

print(df_exams['math score'])
print(df_exams[['math score', 'gender']])

df_exams['language score'] = 70
print(df_exams)

language_score = np.arange(0, 1000)
print(len(language_score))
df_exams['language score'] = language_score
print(df_exams)

def klasse(zahl):
    parameter = 0
    if zahl < 334:
        parameter = 1
    elif zahl < 667:
        parameter = 2
    else:
        parameter = 3
    return parameter

print(klasse(222))
print(klasse(555))
print(klasse(888))

df_exams['parameter_123'] = df_exams['language score'].apply(klasse)
print(df_exams)

int_language_score = np.random.randint(1, 100, size = 1000)
print(min(int_language_score), max(int_language_score))

df_exams['language score'] = int_language_score
print(df_exams)

def klasse(zahl):
    parameter = 0
    if zahl < 34:
        parameter = 1
    elif zahl < 67:
        parameter = 2
    else:
        parameter = 3
    return parameter

df_exams['parameter_123'] = df_exams['language score'].apply(klasse)
print(df_exams)

df = pd.DataFrame({
    'Spalte_2': [3, 5, 6, 10],
    'Spalte_3': [2, 4, 5, 1]
})

# Funktion definieren
def berechne_spalte_4(row):
    if row['Spalte_2'] + row['Spalte_3'] < 10:
        return 99
    else:
        return 11

# apply auf Zeilenebene (axis=1)
df['Spalte_4'] = df.apply(berechne_spalte_4, axis=1)

# Ergebnis anzeigen
print(df)

# Beispiel-DataFrame
df = pd.DataFrame({
    'Spalte_2': [3, 5, 6, 10],
    'Spalte_3': [2, 4, 5, 1]
})

# Lambda-Ausdruck verwenden
df['Spalte_4'] = df.apply(lambda row: 99 if row['Spalte_2'] + row['Spalte_3'] < 10 else 11, axis=1)

# Ergebnis anzeigen
print(df)

print(np.random.uniform(1, 100, size = 100))

score1 = np.random.randint(1, 100, size = 1000)
score2 = np.random.randint(1, 100, size = 1000)

series1 = pd.Series(score1, index = np.arange(0, 1000))
series2 = pd.Series(score2, index = np.arange(0, 1000))

print(series1)

print(df_exams.assign(score1=series1, score2=series2))
print("----")
print(df_exams.iloc[:6, -1])
print(df_exams)

df_exams = df_exams.assign(score1=series1, score2=series2) # overwrite
print(df_exams)

df_exams.insert(1, 'test', series1)
print(df_exams)

df_exams = df_exams.assign(E = lambda x: x["math score"] + x["reading score"])
print(df_exams["E"])

print(df_exams['math score'].sum())

print(
df_exams['math score'].count(),
df_exams['math score'].mean(),
df_exams['math score'].std(),
df_exams['math score'].min(),
df_exams['math score'].max())

print(df_exams.describe())

print(df_exams['math score'] + df_exams['reading score'] + df_exams['writing score'])

df_exams['average'] = (df_exams['math score'] + df_exams['reading score'] + df_exams['writing score'])/3
print(df_exams.round(2))


print(len(df_exams['gender']), df_exams['gender'].count())


print(df_exams['gender'].value_counts())

print(df_exams['gender'].value_counts(normalize=True))

print(df_exams['gender'].value_counts())

print(df_exams['parental level of education'].value_counts())

print(df_exams['parental level of education'].value_counts(normalize = True).round(2))

print(df_exams.sort_values(by='average'))

print(df_exams[df_exams['gender'] == 'male'])

print(df_exams.sort_values(by='average', ascending=False))

print(df_exams.sort_values(by=['average', 'reading score'], ascending=False))

print(df_exams.sort_values(by=['average', 'reading score'], ascending=False,
                           inplace = True)) # updated in df_exams

print(df_exams.sort_values('race/ethnicity', ascending=True,
                           key = lambda x: x.str.lower()))


new_index = np.arange(0, 1000)

random.shuffle(new_index)

print(new_index)

df_exams['new_index'] = new_index
print(df_exams)

# neuen Index setzen
print("___")
df_exams.set_index('new_index', inplace=True)

print(df_exams)

df_exams.sort_index(ascending=True, inplace = True)
print(df_exams)

# rename column

df_exams.rename(columns = {'gender':'Gender'}, inplace = True)
print(df_exams)

df_exams.rename(columns = {'math score':'MS',
                           'reading score':'RS',
                           'writing score':'WS'}, inplace = True)

df_exams.drop(columns = ['score2', 'E', 'average', 'score1', 'parameter_123', 'language score', 'test'], inplace = True)

print(df_exams)

df_exams.rename(index={0:'A', 1:'B', 2:'C'}, inplace = True)

print(df_exams.head(3))







