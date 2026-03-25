from tkinter import *
from PIL import ImageTk, Image

# Hauptfenster erstellen
root = Tk()
root.title("Spielfeld mit Ergebnis-Liste speichern")

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushrooms", "Mushrooms"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")  # Voreinstellung

# Liste zum Speichern der Ergebnisse
Liste_pizza = []

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value = topping).pack(anchor=W)

def clicked(value):
    global Liste_pizza
    Liste_pizza.append(value)  # Auswahl in Liste speichern
    myLabel = Label(root, text=f"Gespeichert: {value}")
    myLabel.pack()

def alle(wert):
    global Liste_pizza
    haeufigkeiten = {}
    for item in Liste_pizza:
        if item in haeufigkeiten:
            haeufigkeiten[item] += 1
        else:
            haeufigkeiten[item] = 1

    myLabel2 = Label(root, text = f"ALLE: {' '.join(Liste_pizza)}")
    myLabel2.pack()
    Label(root, text = "Bestellung:").pack(pady = 10)
    for key, value in haeufigkeiten.items():
        myLabel3 = Label(root, text = f"{value} mal {key}")
        myLabel3.pack(anchor = W)

#myLabel = Label(root, text=f"Voreinstellung: {pizza.get()}")
#myLabel.pack()

myButton = Button(root, text="Click", command=lambda: clicked(pizza.get()))
myButton.pack()
myButton2 = Button(root, text = "Liste", command = lambda: alle(pizza.get()))
myButton2.pack()

root.mainloop()

# Ergebnisse anzeigen
print("Auswahl-Liste:", Liste_pizza)