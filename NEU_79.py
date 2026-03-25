total = 0
for n in range(-1, 31):
    term = (1/5) ** (2 * n + 4)
    total += term

print(f"Summe der Reihe von n = -1 bis 30: {total:.10f}")



k = 2
N = 0
while True:
    Zahlen = [x for x in range(2,k)
              if all(x%y !=0 for y in range(2, int(x**0.5) + 1))]
    if len(Zahlen) < 11:
        k = k + 1
        N = len(Zahlen)
    else: break

print(Zahlen)



Zahlen2 = [x for x in range(2,3)
              if all(x%y !=0 for y in range(2, int(x**0.5) + 1))]

print(Zahlen2)
