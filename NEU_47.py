from tkinter import *

root = Tk()
root.title("Canvas")
root.geometry("500x500")

my_canvas = Canvas(root, width = 300, height = 200, bg = "white")
my_canvas.pack(pady = 20)

#x1 y1 x2 y2
my_canvas.create_rectangle(50, 150, 250, 50, fill = "pink")
my_canvas.create_oval(50, 150, 250, 50, fill = "cyan")
my_canvas.create_line(0, 100, 300, 100, fill = "red")
my_canvas.create_line(150, 0, 150, 200, fill = "red")

def show():
    myLabel = Label(root, text = var.get()).pack()

def show_2():
    myLabel = Label(root, text = clicked.get()).pack()

var = StringVar()

c = Checkbutton(root, text = "Check box", variable = var, onvalue = "Pizza", offvalue = "Off")
c.deselect()
c.pack()


options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

clicked = StringVar()
clicked.set(options[0])

myButton = Button(root, text = "Show Selection", command = show).pack()

drop = OptionMenu(root, clicked, *options)
drop.pack()


myButton_2 = Button(root, text = "Show Selection", command = show_2).pack()
root.mainloop()