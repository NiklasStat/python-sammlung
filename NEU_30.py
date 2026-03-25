from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

# Hauptfenster erstellen
root = Tk()
root.title("Normalverteilung Plotter")

# Eingabefelder für Erwartungswert und Varianz
mean_label = Label(root, text="Erwartungswert (Mean):")
mean_label.pack()
mean_entry = Entry(root, width=20)
mean_entry.pack()

variance_label = Label(root, text="Varianz:")
variance_label.pack()
variance_entry = Entry(root, width=20)
variance_entry.pack()

# Funktion zum Plotten der Normalverteilung
def plot_normal_distribution():
    try:
        mean = float(mean_entry.get())
        variance = float(variance_entry.get())
        if variance <= 0:
            raise ValueError("Die Varianz muss positiv sein.")

        # Normalverteilung berechnen
        std_dev = np.sqrt(variance)
        x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 500)
        y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

        # Plot erstellen
        plt.figure(figsize=(8, 5))
        plt.plot(x, y, label=f"Mean = {mean}, Variance = {variance}")
        plt.title("Normalverteilung")
        plt.xlabel("x")
        plt.ylabel("Wahrscheinlichkeit")
        plt.ylim(0, 0.4)  # Begrenzung der y-Achse auf maximal 0.4
        plt.legend()
        plt.grid()
        plt.show()
    except ValueError as e:
        error_label = Label(root, text=f"Fehler: {e}", fg="red")
        error_label.pack()

# Button zum Plotten erstellen
plot_button = Button(root, text="Normalverteilung zeichnen", command=plot_normal_distribution)
plot_button.pack()

# Hauptschleife starten
root.mainloop()



from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Hauptfenster erstellen
root = Tk()
root.title("Normalverteilung Plotter")

# Eingabefelder für Erwartungswert und Varianz
mean_label = Label(root, text="Erwartungswert (Mean):")
mean_label.pack()
mean_entry = Entry(root, width=20)
mean_entry.pack()

variance_label = Label(root, text="Varianz:")
variance_label.pack()
variance_entry = Entry(root, width=20)
variance_entry.pack()

# Rahmen für den Plot
plot_frame = Frame(root)
plot_frame.pack()

# Funktion zum Plotten der Normalverteilung
def plot_normal_distribution():
    try:
        mean = float(mean_entry.get())
        variance = float(variance_entry.get())
        if variance <= 0:
            raise ValueError("Die Varianz muss positiv sein.")

        # Normalverteilung berechnen
        std_dev = np.sqrt(variance)
        x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 500)
        y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

        # Plot erstellen
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x, y, label=f"Mean = {mean}, Variance = {variance}")
        ax.set_title("Normalverteilung")
        ax.set_xlabel("x")
        ax.set_ylabel("Wahrscheinlichkeit")
        ax.set_ylim(0, 0.4)
        ax.legend()
        ax.grid()

        # Vorherigen Plot entfernen (falls vorhanden)
        for widget in plot_frame.winfo_children():
            widget.destroy()

        # Plot in Tkinter einbetten
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()
        canvas.draw()
    except ValueError as e:
        error_label = Label(root, text=f"Fehler: {e}", fg="red")
        error_label.pack()

# Button zum Plotten erstellen
plot_button = Button(root, text="Normalverteilung zeichnen", command=plot_normal_distribution)
plot_button.pack()

# Hauptschleife starten
root.mainloop()


