from tkinter import *
from tkinter import PhotoImage

from PIL import ImageTk, Image

# Hauptfenster erstellen

root = Tk()
root.title("Spielfeld mit Ergebnis-Liste speichern")

def open():
    top = Toplevel()
    top.title("Learn to code")
    img = ImageTk.PhotoImage(Image.open(r"C:\Users\nikla\Downloads\Hornbach.jpg"))
    label = Label(top, image=img)
    label.image = img  # Referenz speichern!
    label.pack()
    Button(top, text="Close Window", command=top.destroy).pack()


btn = Button(root, text = "Open Second Window", command = open).pack()


root.mainloop()
