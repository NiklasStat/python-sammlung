from tkinter import *


root = Tk() # erzeuge Fenster

e = Entry(root, width = 40) # Textzeile zur Eingabe
e.pack()
e.insert(0, "Enter Name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text =  "Enter name",
                  command = myClick)
myButton.pack()


root.mainloop()