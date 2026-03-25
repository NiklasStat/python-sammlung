def AddiSubbi(x, y):
    return x + y, x - y

print(AddiSubbi(3, 4))

def Multi(x, y):
    return x * y

print(Multi(3, 4))
print(AddiSubbi(3, 5))

# Aufteilen des Tupels in zwei Variablen
add_result, sub_result = AddiSubbi(2, 3)

# Aufruf der Multi-Funktion mit den einzelnen Werten
print(Multi(add_result, sub_result))  # -5

k = 0
liste = []
zahlen = [x for x in range(1, 11)]
print(zahlen, liste)

for i in zahlen:
    k = k + i
    liste.append(k)

print(liste)


liste_2 = []
k = 1

def leere_i(i):
    L = [[" " for _ in range(i)] for _ in range(i)]
    return L

print(leere_i(5))




def Binomial(L):
    matrix = leere_i(L)
    for i in range(1, L+1):
        matrix[i-1][i-1] = i
    return matrix

print(Binomial(5))

def Binomial(L):
    result = []
    for i in range(L):
        row = [1] * (i+1)
        for j in range(1, i):
            row[j] = result[i-1][j-1] + result[i-1][j]
        result.append(row)
    return result

print(Binomial(5))


for row in Binomial(7):
    print(" ".join(map(str, row)))

liste = [1]
k = 10
h = 1
for i in range(2, k+2):
    h = h * 2
    liste.append(h)
    print(liste)

namen = ["Armin", "Bert", "Conrad", "Damian", "Emil"]

for i, j in enumerate(namen):
    print(i+1, j)