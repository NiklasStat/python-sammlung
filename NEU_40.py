from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learn Coding.")
root.iconbitmap(r"C:\Users\nikla\Downloads\bnb_crypto_icon_264371.ico")



frame = LabelFrame(root, text = "This is my Frame...", padx = 50, pady = 50)
frame.pack(padx = 10, pady = 10) # Abstand zu Fensterrand

b = Button(frame, text = "Do not Click Here!")
b2 = Button(frame, text = "ohhhh")

b.grid(row = 0, column = 0)
b2.grid(row = 1, column = 1)

#r = IntVar()
#r.set("2")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushrooms", "Mushrooms"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text = text, variable = pizza, value = mode).pack(anchor = W)


def clicked(value):
    myLabel = Label(root, text = value)
    myLabel.pack()

#Radiobutton(root, text = "Option 1", variable = r, value = 1, command = lambda: clicked(r.get())).pack()
#Radiobutton(root, text = "Option 2", variable = r, value = 2, command = lambda: clicked(r.get())).pack()

myLabel = Label(root, text = pizza.get())
myLabel.pack()

myButton = Button(root, text = "Click", command = lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()

