# Interview Master 100
# Summe aus 2 Zahlen einer Liste muss genau 9 sein-
# gib beide indices an. es müssen verschiedene zahlen sein.
from collections import Counter


num = [2,3,4,3,4,3,6,5,3,4,5,3,5]
friend_counts = Counter(num)
print(friend_counts)
xs = range(101)
ys = [friend_counts[x] for x in xs]
print(list(xs))
print(ys)
print(len(num))

print("___________")
def addi(nums):
    pos = 0
    kos = pos + 1
    for zahl in nums:
        while kos < len(nums):
            if zahl + nums[kos] == 9:
                return [pos, kos]
            else:
                kos += 1
        pos += 1
        kos = pos + 1

    return -99



a = [2, 11, 15, 7]
b = [3, 2, 4, 1, 0, 7, 3]
c = [1, 2, 3, 2, 6, 22]

print(addi(a))
print(addi(b))
print(addi(c))

print('_______________')
def addi2(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            num_indices[num] = i
            print(num_indices)
            return [num_indices[complement], i]

        num_indices[num] = i
        print(num_indices)
    return []

print(addi2(a, 9))

hh = {"aa": "bb", "cc": "dd"}
print("aa" in hh)
print("bb" in hh)
stack = []
print(stack if not stack else 0)

print("___________")
def klammern_string(klammern) -> bool:
    dic = {')': '(', ']': '[', '}': '{'}
    offen = []
    for k in klammern:
        if k in dic:
            if not offen or offen[-1] != dic[k]:
                return [False, 77]
            offen.pop()
        else:
            offen.append(k)
    return len(offen) == 0

print(klammern_string("[()]"))
print(klammern_string("[()"))
print(klammern_string("][()"))
print(klammern_string("[(])"))

print('_______________')
def kl(string):
    dict = {')': '(', ']': '[', '}': '{'}
    bisher = []
    for i in string:
        if i in dict:
            if bisher == [] or bisher[-1] != dict[i]:
                return [False, 77]
            bisher.pop()
        else:
            bisher.append(i)

    return len(bisher) == 0

print(kl("[()]"))
print(kl("[()"))
print(kl("][()"))
print(kl("[(])"))

Liste1 = [1, 4, 5]
Liste2 = [2, 3, 6]

print('______+++______')
def listlist(list1, list2):
    Liste_neu = []
    i, k = 0, 0
    while i < len(list1) and k < len(list2):
        if list2[k] < list1[i]:
            Liste_neu.append(list2[k])
            k += 1
        else:
            Liste_neu.append(list1[i])
            i += 1



    return Liste_neu

print(listlist(Liste1, Liste2))






def sumtest(data):
    for a in range(len(data) - 1):
        b = a + 1
        while b < len(data):
            if data[a] + data[b] == 10:
                return a, b
            b += 1
    return -1, -1

v = [1,2,3,4,5,6]
print(sumtest(v))



d = [2, 4, 5, 6, 8]
def test(x):
    if x == 4:
        return 99
    else:
        return x

print(list(map(test, d)))


# if ... else ... goes before the for loop
d = [2, 4, 5, 6, 8]
fff = [99 if i == 4 else i for i in d]
print(fff)

import matplotlib.pyplot as plt
import pandas as pd

# 1. Daten definieren (basierend auf Ihrer Eingabe)
# Die Werte müssen als Dezimalzahlen (float) für die Grafik konvertiert werden
daten = {
    'Jahr': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Neuzulassungen': [3.20, 3.35, 3.44, 3.44, 3.61, 2.90, 2.62, 2.65, 2.83, 2.80]
}

df = pd.DataFrame(daten)

# 2. Grafik erstellen (Liniendiagramm für Zeitreihen)
plt.figure(figsize=(10, 6)) # Größe des Diagramms festlegen

# Liniendiagramm zeichnen
plt.plot(df['Jahr'], df['Neuzulassungen'], marker='o', linestyle='-', color='#0077b6')

# Höchstwert (2019) und Tiefstwert (2021) markieren und beschriften
plt.annotate(
    'Höchstwert (3.61 Mio.)',
    xy=(2019, 3.61),
    xytext=(2018.5, 3.7),
    arrowprops=dict(facecolor='red', shrink=0.05, width=1, headwidth=6),
    fontsize=9,
    color='red'
)
plt.annotate(
    'Tiefstwert (2.62 Mio.)',
    xy=(2021, 2.62),
    xytext=(2020.5, 2.45),
    arrowprops=dict(facecolor='green', shrink=0.05, width=1, headwidth=6),
    fontsize=9,
    color='green'
)

# 3. Grafik beschriften
plt.title('PKW-Neuzulassungen in Deutschland (2015–2024)', fontsize=14, fontweight='bold')
plt.xlabel('Jahr', fontsize=12)
plt.ylabel('Neuzulassungen (in Millionen)', fontsize=12)

# X-Achsen-Ticks als ganze Zahlen festlegen
plt.xticks(df['Jahr'], rotation=45, ha='right')

# Gitternetzlinien hinzufügen
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Layout anpassen und Grafik speichern/anzeigen
plt.tight_layout()
plt.savefig('neuzulassungen_grafik.png') # Grafik als PNG-Datei speichern

print("✅ Der Python-Code wurde ausgeführt. Die Grafik wurde als 'neuzulassungen_grafik.png' gespeichert.")
print("Um die Grafik anzuzeigen, benötigen Sie die lokalen Bibliotheken 'matplotlib' und 'pandas'.")