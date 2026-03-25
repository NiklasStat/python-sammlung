""" Das ist ein Modul zum ausprobieren.
"""
def fkt(vektor):
    ''' Diese Funktion nimmt das erste Zeichen. '''
    k = vektor[0]
    return k

if __name__ == '__main__':
    print("Ich wurde direkt aufgerufen.")
    #zu_pruefen = input("Vektor?")
    zu_pruefen = [5, 22]
    print(fkt(zu_pruefen))
else:
    print(f"Ich wurde als Modul {__name__} eingebunden")

print(fkt([6,7,8]))
print("___")


faktor = 10
letztes_ergebnis = None
def wert_mal_faktor(wert):
    global letztes_ergebnis
    letztes_ergebnis = wert * faktor
    return letztes_ergebnis

print(wert_mal_faktor(2))
print(letztes_ergebnis)