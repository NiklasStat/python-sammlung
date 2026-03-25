# Ein Dictionary erstellen
student = {
    "name": "Anna",
    "age": 23,
    "subjects": ["Mathematics", "Physics", "Chemistry"]
}

# Zugriff auf Werte mithilfe der Keys
print(student["name"])  # Ausgabe: Anna
print(student["age"])   # Ausgabe: 23
print(student["subjects"])  # Ausgabe: ['Mathematics', 'Physics', 'Chemistry']

# Ein bestimmtes Fach aus der Liste der Fächer abrufen
print(student["subjects"][1])  # Ausgabe: Physics

# Hinzufügen eines neuen Key-Value-Paares
student["graduation_year"] = 2025
print(student)

# Überprüfen, ob ein Key existiert
if "name" in student:
    print("Name ist vorhanden.")
else:
    print("Name fehlt.")

# Ein Dictionary erstellen
person = {
    "name": "Niklas",
    "age": 25,
    "city": "Köln"
}

# Wert abrufen mit .get()
name = person.get("name")  # Gibt "Niklas" zurück
print(name)

# Key existiert nicht, Standardwert zurückgeben
country = person.get("country", "Deutschland")  # Gibt "Deutschland" zurück
print(country)

# Key existiert nicht, ohne Standardwert
job = person.get("job")  # Gibt None zurück
print(job)

print("-------------------------------------")

print('F' + 'G')

print("Fisch")
line = '*'
max_length = 10
while len(line) <= max_length:
    print(line)
    line += '*'
while len(line) > 0:
    print(line)
    line = line[:-1]

print("Fisch reverse")

max_length = 6
k, l = 0, 6
while k <= max_length:
    print(" " * l, "*" * k)
    k += 1
    l -= 1
max_length = 6
k, l = 0, 6
while k <= max_length:
    print(" " * (7-l), "*" * (5-k))
    k += 1
    l -= 1

# print(515 434 353 272 191 0110)
print("Raute")
k = 5
l = 1
while l <= 11:
    print(" " * k, "*" * l, " " * k)
    k -= 1
    l += 2

k = 1
l = 9
while l > 0:
    print(" " * k, "*" * l, " " * k)
    l -= 2
    k += 1

for i in range(5):
    if i == 2:
        continue
    print(i)


def error():
    ''' teste errordivision'''
    try:
        result = 5/0
        print("success")
    except ZeroDivisionError:
        print("Failed divided zero")
        result = 5
        return result

print(error())


k = 0
l = 5
for i in range(5):
    print("" * k,"*" * l )
    k += 1
    l -= 1

k = 1
l = 4
for i in range(5):
    print(" " * l,"-" * k, " " * l )
    k += 2
    l -= 1

k = 7
l = 1
for i in range(4):
    print(" " * l,"-" * k, " " * l )
    k -= 2
    l += 1


k = [print(i) for i in range(5)]
print("___")
k = [print(i) for i in range(5) if i % 2 == 0 and i != 2]

liste_rot = [5, 6, 9, 0, 2, 3, 4]

def rot_fkt(liste, anzahl_rot):
    liste_neu = [0] * len(liste)
    k = 0
    for i in liste:
        if k < 3:
            liste_neu[k + anzahl_rot] = i
        else:
            liste_neu[k + anzahl_rot -7] = i
        k += 1
    return liste_neu

print(rot_fkt(liste_rot, 4))

def rot_fkt(liste, anzahl_rot):
    liste_neu = [0] * len(liste)  # Neue Liste mit Nullen
    for k in range(len(liste)):
        # benutze %, also Rest:
        # 4%7 4, 5%7 5, 6%7 6, 7%7 0, 8%7 1, 9%7 2, 10%7 3
        neue_pos = (k + anzahl_rot) % len(liste)
        liste_neu[neue_pos] = liste[k]
    return liste_neu

print(rot_fkt(liste_rot, 4))

ergebnis = [a-b for a, b in zip([1,2,4], [2,3,3])]
print(ergebnis)

lis = [5,7,9,11,2,3,4]
lis_n = (lis[-1], *lis)
print(lis_n)

lis_n = [*lis[-1:], *lis[:-1]]
print(lis[-1:])
print(lis[:-1])
print(lis_n)  # → [4, 5, 7, 9, 11, 2, 3]

lis = [5, 7, 9, 11, 2, 3, 4]
lisn = [1, 2, 3, 4, 5, 6, 7]

differenz = [a - b for a, b in zip(lis, lisn)]
print(differenz)
print(444)
liste = [4, 5, 6, 7, -3, -3, -3]
index = next(i for i, val in enumerate(liste) if val < 0)
print(index)


import numpy as np
result = np.array(lis) - np.array(lisn)
print(result)