



def fkt_leer(wert):
    drei_mal_drei_leer = [[" ", wert, " "] for i in range(3)]
    return drei_mal_drei_leer


print(fkt_leer(33))

def Summe(wert):
    S = sum(int(fkt_leer(wert)[i][1]) for i in range(3))
    return S

print(Summe(77))

# füge 9 objekte hinzu.
Liste = []
while True:
    einkaufen = input("Was willst du kaufen?")
    if len(Liste) > 8:
        break
    else:
        Liste.append(einkaufen)

print(Liste)