from tkinter import *

root = Tk()
root.title("Grid-Beispiel")

# Eingabefeld oben
entry = Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Beispiel-Funktion
def button_click(number):
    entry.insert(END, str(number))

# Buttons 1–9 in einem 3x3-Raster
buttons = []
row = 1
col = 0
for i in range(1, 10):
    btn = Button(root, text=str(i), padx=20, pady=20, command=lambda num=i: button_click(num))
    btn.grid(row=row, column=col)
    col += 1
    if col > 2:
        col = 0
        row += 1
    buttons.append(btn)

# Button 0 mittig unten
btn_zero = Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0))
btn_zero.grid(row=4, column=1)

# Weitere Buttons (z. B. Clear, =)
btn_clear = Button(root, text="Clear", padx=20, pady=20, command=lambda: entry.delete(0, END))
btn_clear.grid(row=4, column=0)

btn_equal = Button(root, text="=", padx=20, pady=20)
btn_equal.grid(row=4, column=2)

root.mainloop()
