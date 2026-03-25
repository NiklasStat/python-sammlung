from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tag = soup.find('h5') # stops at first h5 element!
    courses_html_tags = soup.find_all('h5')
    for course in courses_html_tags:
        print(course.text)
    print('_________')
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print('_________---------------')
        print(f"{course_name} costs {course_price}")


import matplotlib.pyplot as plt
import numpy as np

# Beispiel-Daten für die Tabellen generieren
def create_random_data():
    return np.random.randint(1, 100, size=(5, 5))  # 5x5 Tabelle mit Zufallswerten

# Dashboard (3x2 Grid) erstellen
fig = plt.figure(figsize=(12, 8))  # Größe des Dashboards
grid = fig.add_gridspec(3, 2, wspace=0.4, hspace=0.6)  # 3x2 Grid mit Abständen

# 6 Tabellen aufteilen
for i in range(3):  # Zeilen
    for j in range(2):  # Spalten
        ax = fig.add_subplot(grid[i, j])  # Subplot für Tabelle
        ax.axis('tight')  # Grenzen anpassen
        ax.axis('off')  # Achsen deaktivieren
        data = create_random_data()  # Daten generieren
        table = ax.table(cellText=data, colLabels=[f"Spalte {k+1}" for k in range(5)],
                         loc='center', cellLoc='center', colColours=['#cccccc']*5)
        table.auto_set_font_size(False)  # Schriftgröße festlegen
        table.set_fontsize(8)  # Schriftgröße
        ax.set_title(f"Tabelle {i*2 + j + 1}")  # Titel jeder Tabelle

# Dashboard anzeigen
plt.show()


