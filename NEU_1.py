k = 2
N = 0
while True:
    Zahlen = [x for x in range(2, k)
              if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]
    if len(Zahlen) < 11:
        k = k + 1
        N = len(Zahlen)
    else: break

print("_____")
print(N)
print(Zahlen)
print(k)

k = 2
N = 0
while True:
    Zahlen = [x for x in range(2, k)
              if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]
    k = k + 1
    if len(Zahlen) == 50:
        N = len(Zahlen)
        break

print("_____")
print(N)
print(Zahlen)
print(Zahlen[-1])
print(f"Es gibt insgesamt {N} Primzahlen, und die 50. lautet {Zahlen[-1]}.")


wort = "Autobahnbrücke"
print(wort.lower())
buchstaben_liste = [buchstabe for buchstabe in wort.lower()]
print(set(buchstaben_liste))
test = {i: wort.lower().count(i) for i in wort.lower()} # ist set deshalb automatisch für i jeder buchstabe nur einmal
print(test)

text = ("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
        "sed diam nonumy eirmod tempor invidunt ut labore et dolore"
        " magna aliquyam erat, sed diam voluptua. At vero eos et "
        "accusam et justo duo dolores et ea rebum. Stet clita kasd "
        "gubergren, no sea takimata sanctus est Lorem ipsum dolor "
        "sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing "
        "elitr, sed diam nonumy eirmod tempor invidunt ut labore "
        "et dolore magna aliquyam erat, sed diam voluptua. "
        "At vero eos et accusam et justo duo dolores et ea rebum. "
        "Stet clita kasd gubergren, no sea takimata sanctus est"
        " Lorem ipsum dolor sit amet.")

print(text)

buchstaben_liste_2 = [buchstabe for buchstabe in text.lower() if buchstabe.isalpha()]
test_2 = {i: buchstaben_liste_2.count(i) for i in set(buchstaben_liste_2)} # ist set deshalb automatisch für i jeder buchstabe nur einmal
print(test_2)


import matplotlib.pyplot as plt

# Der Text, den du analysieren möchtest
text = "Autobahnbrücke"

# Buchstaben aus dem Text filtern und zählen
buchstaben_liste = [buchstabe for buchstabe in text.lower() if buchstabe.isalpha()]
buchstaben_haeufigkeit = {i: buchstaben_liste.count(i) for i in set(buchstaben_liste)}

# Daten für das Diagramm vorbereiten
buchstaben = sorted(test_2.keys())
haeufigkeiten = list(test_2.values())

# Diagramm erstellen
plt.bar(buchstaben, haeufigkeiten)
plt.xlabel('Buchstaben')
plt.ylabel('Häufigkeit')
plt.title('Häufigkeit der Buchstaben in "lorem ip..."')
plt.show()
