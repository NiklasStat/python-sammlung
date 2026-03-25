from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

# Hauptfenster erstellen
root = Tk()
root.title("Spielfeld mit Ergebnis-Liste speichern")

def open_file():
    # Dateidialog öffnen
    root.filename = filedialog.askopenfilename(
        initialdir="C:\\Users\\nikla\\Downloads\\",
        title="Select a file",
        filetypes=(("png files", "*.png"), ("all files", "*.*"))
    )

    # Label aktualisieren, nachdem der Benutzer eine Datei ausgewählt hat
    if root.filename:
        my_label.config(text=f"Ausgewählte Datei: {root.filename}")

        # Bild laden und anzeigen
        img = Image.open(root.filename)
        my_image = ImageTk.PhotoImage(img)

        # Bild-Label aktualisieren oder neues Label erstellen
        my_image_label.config(image=my_image)
        my_image_label.image = my_image  # Referenz speichern, damit das Bild nicht gelöscht wird
    else:
        my_label.config(text="Keine Datei ausgewählt.")

# Label für Dateiname erstellen (initial leer)
my_label = Label(root, text="Noch keine Datei ausgewählt.")
my_label.pack(pady=20)

# Button zum Öffnen des Dialogs hinzufügen
my_button = Button(root, text="Datei auswählen", command=open_file)
my_button.pack(pady=20)

# Platzhalter für Bild
my_image_label = Label(root)
my_image_label.pack(pady=20)

root.mainloop()