dateiname = "Autotext-lesexn.JPG"
print(dateiname[1:])
print(dateiname[-3:])
print(dateiname.lower()[:-2])
print(dateiname[1:3])

name = "Autotext-lesen.JPG"
only_letters = ''.join([char for char in name if char.isalpha()])
print(only_letters)

name = "Autotext-lesen.JPG"
words = name.replace("-", " ").replace(".", " ").split()
print(words)

neu = " ".join(words)
print(neu)

text = "SCHRÖDINGER"
suche = "IN"
print(text.find(suche))

text = "SCHRÖDINGER"
suche = "INDE"
print(text.find(suche))  # -1, wenn nicht drinnen

neu = "exempeltext mit mehreren ex"
substring = "ex"
start = 0

while start < len(neu):
    pos = neu.find(substring, start) # beginnt such ab position start
    if pos == -1:
        break
    print("Gefunden an Position:", pos)
    start = pos + 1


neu = "exempeltext miiiiiiiiiiit mehreren ex"
substring = "ex"
start = 0

print("_______")


while start < len(neu):
    pos = neu.find(substring, start)
    if pos == -1:
        break
    print(pos)
    start = pos + 1

















