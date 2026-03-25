from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
# Hauptfenster erstellen

root = Tk()
root.title("Spielfeld mit Ergebnis-Liste speichern")


def popup():
 #   messagebox.showinfo("This is Popup.", "Hallo world")
 #   messagebox.showerror("This is Popup.", "Hallo world")
 #   messagebox.askquestion("This is Popup.", "Hallo world")
#    messagebox.askokcancel("This is Popup.", "Hallo world")
    #response = messagebox.askokcancel("This is Popup.", "Hallo world")
    # response = messagebox.askquestion("This is Popup.", "Hallo world")
     response = messagebox.showerror("This is Popup.", "Hallo world")

     Label(root, text = response).pack()
    # if response == 1:
   #     Label(root, text = "You clicked yes").pack()
  #   else:
   #     Label(root, text = "Clicked no").pack()

Button(root, text = "Popup", command = popup).pack()


root.mainloop()

