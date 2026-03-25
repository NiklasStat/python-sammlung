from tkinter import *

root = Tk() # erzeuge Fenster

# Creating a Label Widget
myLabel1 = Label(root, text = "Hello World!")
myLabel2 = Label(root, text = "I am cool")
myLabel3 = Label(root, text = "Nächste Reihe").grid(row = 2, column = 2)


# Shoving it onto the screen = schieben
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 4) # relativ, 1 = 4 = 5


root.mainloop()

root = Tk() # erzeuge Fenster

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text = "Click me!", padx = 50, pady = 50)

myButton.pack()


root.mainloop()

root = Tk() # erzeuge Fenster

def myClick():
    myLabel = Label(root, text = "I clicked")
    myLabel.pack()

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text = "Click me!",
                  command = myClick, fg = "blue", bg = "#000000")
myButton.pack()


root.mainloop()

root = Tk() # erzeuge Fenster

e = Entry(root, width = 40, bg = "blue", fg = "white",
          borderwidth = 5) # Textzeile zur Eingabe
e.pack()


def myClick():
    myLabel = Label(root, text = "I clicked")
    myLabel.pack()

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text = "Click me!",
                  command = myClick)
myButton.pack()


root.mainloop()

root = Tk() # erzeuge Fenster

e = Entry(root, width = 40) # Textzeile zur Eingabe
e.pack()


def myClick():
    myLabel = Label(root, text = e.get())
    myLabel.pack()

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text = "Enter name",
                  command = myClick)
myButton.pack()


root.mainloop()

root = Tk() # erzeuge Fenster

e = Entry(root, width = 40) # Textzeile zur Eingabe
e.pack()


def myClick():
    myLabel = Label(root, text = "Hello " + e.get())
    myLabel.pack()

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text =  "Enter name",
                  command = myClick)
myButton.pack()


root.mainloop()


root = Tk() # erzeuge Fenster

e = Entry(root, width = 40) # Textzeile zur Eingabe
e.pack()


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()

# myButton = Button(root, text = "Click me!", state = DISABLED) # disabled
myButton = Button(root, text =  "Enter name",
                  command = myClick)
myButton.pack()


root.mainloop()

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