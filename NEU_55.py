from os import times
import time
import numpy as np

a = [1,2,3]
b = [10, 20, 30]

def Summ(a, b):
    result = 0
    for x, y in zip(a, b):
        result += x * y
    return result
print(Summ(a, b))

kanto = [73, 67, 43]
johto = [91, 88, 64]
hoenn = [87, 134, 58]
sinnoh = [102, 43, 37]
unova = [69, 96, 70]

w1, w2, w3 = 0.3, 0.2, 0.5
weights = [w1, w2, w3]

kanto_temp = 73
kanto_rainfall = 67
kanto_humidity = 43

kanto_yield_apples = kanto_temp*w1 + kanto_rainfall*w2 + kanto_humidity*w3
print(kanto_yield_apples)

def crop_yield(region, weights):
    result = 0
    for x, y in zip(region, weights):
        result += x * y
    return result

print(crop_yield(johto, weights))

kanto_np = np.array([73, 67, 43])
print(kanto_np)
weights_np = np.array([w1, w2, w3])

print(np.dot(kanto, weights))
print((kanto_np * weights_np).sum())

arr1 = list(range(1000000))
arr2 = list(range(1000000, 2000000))

arr1_np = np.array(arr1)
arr2_np = np.array(arr2)

print("-------------")


start_time = time.time()
# Dein Code hier
result = 0
for x1, x2 in zip(arr1, arr2):
    result += x1 * x2
print(result)
end_time = time.time()
print("Dauer:", end_time - start_time, "Sekunden")
print(33333344444444555555555)
print(f"Laufzeit: {end_time - start_time:.5f} Sekunden")

start_time2 = time.time()
print(np.dot(arr1_np, arr2_np))
end_time2 = time.time()
print(f"Laufzeit: {end_time2 - start_time2:.5f} Sekunden")

x = [1,2,3]
x.extend([4,5,6])
y = x + [7,8,9]
print(y)

dic = {"Name": "Nik", "Alter": 40, "Groeße": 180}
print(dic.keys(), dic.values())
print(dic["Name"])

zaehlen = [0 for i in range(4)]
zaehlen2 = [0 for _ in range(4)]
print(zaehlen, zaehlen2)

paare = [(x, y) for x in range(2,4) for y in range(11, 13)]
print(paare)

k = [2, 4, 6, 8]
dict = {}
for i in k:
    dict[i] = True

print(dict)

print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
class Set:

    def __init__(self, values = None):
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        return "Set: " + str(self.dict.keys())

    def add(self, value):
        self.dict[value] = True

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

s = Set([1,2,3])
s.add(4)
print(s.contains(4)) # True
s.remove(3)
print(s.contains(3)) # False
print(s.__repr__())
print(s)


def gutu(x, y):
    return 2 * x * y

print(list(map(gutu, [3, 4], [4, 5])))

result = map(gutu, [3, 4], [5, 6])
print(next(result))  # Gibt den ersten Wert aus: 30
print(next(result))  # Gibt den zweiten Wert aus: 48

durch_3 = [x for x in range(1, 101) if x % 3 == 0]
def durch6(x):
    return x % 6 == 0
list_6 = filter(durch6, durch_3)
print(list(list_6))

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print(letters, numbers)





