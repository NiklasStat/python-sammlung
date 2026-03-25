import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt



def split_fg(value):
    if value == "-":
        return "-", "-"
    else:
        getroffen, geworfen = value.split("/")
        return int(getroffen), int(geworfen)  # Optional: In Integer umwandeln

def tg(getroffen, geworfen):
    if geworfen == 0 or geworfen == '-':
        return '-'
    else:
        return round((getroffen / geworfen), 2)

# Anwenden der Funktion auf die Spalte 'FG'


url = "https://www.cbssports.com/nba/scoreboard/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Alle Links mit "Box Score" im Text finden
box_score_links = [a['href'] for a in soup.find_all("a", string="Box Score")]

print(box_score_links)

for link in box_score_links:
    full_url = f"https://www.cbssports.com{link}"  # Falls relative Links
    response = requests.get(full_url)
    soup = BeautifulSoup(response.text, "html.parser")

    away_team_div = soup.find("div", id="player-stats-away")

    if away_team_div:
        player_names = [cell.get_text(strip=True) for cell in
                        away_team_div.find_all(["td", "a"], class_=["number-element", "name-truncate"])]
        print(f"Spieler des Auswärtsteams von {full_url}: {player_names}")
    else:
        print(f"⚠️ Keine Daten für das Auswärtsteam auf {full_url} gefunden.")

        # Beispiel: Spielernamen aus Tabellen suchen
   # header = soup.find("th")  # Falls die Spaltenüberschrift im ersten <th> steht

   # player_names = [header.get_text(strip=True)] + [cell.get_text(strip=True) for cell in soup.find_all(["td", "a"],
                                                                                                    #    class_=[
                                                                                                        #    "number-element",
                                                                                                       #    "name-truncate"])]

   # print(f"Spieler von {full_url}: {player_names}")

    headers = ['NAME', 'PTS', 'REB', 'AST', 'FG', '3PT', 'FT', 'PF', 'MIN', 'STL', 'BLK', 'TO', 'OREB', 'DREB', '+/-', 'FPTS']


    # Tabelle anzeigen

    #print(df.iloc[0:5])
    #print(df.iloc[5:10])
    #print(df)

    #print(df)
   # print(player_names[110])
   # print(player_names[189])
   # print(player_names[205])
  #  print(player_names[205 + 10 * 16])
  #  print(player_names[-16])


    # Liste der Spieler aus bestimmten Indizes
    selected_players = player_names[110:190] + player_names[205:-15]

    # Daten zeilenweise in 16er-Gruppen aufteilen
    rows = [selected_players[i:i + 16] for i in range(0, len(selected_players), 16)]

    # DataFrame erstellen
    df_a= pd.DataFrame(rows, columns=headers)

    # Tabelle anzeigen
    df_a[['Getroffen', 'Geworfen']] = df_a['FG'].apply(split_fg).apply(pd.Series)
    df_a['Trefferquote_Feld'] = df_a.apply(lambda row: tg(row['Getroffen'], row['Geworfen']), axis=1)

    df_a['Trefferquote_Feld'] = pd.to_numeric(df_a['Trefferquote_Feld'], errors='coerce')

    # Entferne Zeilen mit NaN-Werten aus `Trefferquote_Feld`
    df_a = df_a.dropna(subset=['Trefferquote_Feld'])

    # Ausgabe der neuen Tabelle

    print(df_a)

    anzahl_werte = df_a[df_a['Trefferquote_Feld'].apply(lambda x:
                                                        isinstance(x, (int, float)))]['Trefferquote_Feld'].ge(0).sum()

    print(f"Anzahl der Werte ≥ 0: {anzahl_werte}")

    x_values = range(1, anzahl_werte + 1)  # Neue x-Achsen-Werte für die Grafik

    # Erstellen der y-Werte (Trefferquote)
    y_values = df_a['Trefferquote_Feld'][0:anzahl_werte]

    # Spielernamen für die Beschriftung
    player_names = df_a['NAME'][0:anzahl_werte]

    print(x_values)
    print(y_values)
    print(player_names)

    # Balkendiagramm erstellen
    plt.figure(figsize=(12, 6))
    plt.bar(x_values, y_values, color="dodgerblue")

    # Namen neben die Balken setzen
    valid_data = df_a[df_a['Trefferquote_Feld'].apply(lambda x: isinstance(x, (int, float)))]

    for x, y, name in zip(valid_data.index, valid_data['Trefferquote_Feld'], valid_data['NAME']):
        plt.text(x + 1, y / 2, str(name), ha="center", va="center", fontsize=6, color="black", fontweight="bold")
    # Achsenbeschriftungen und Titel
    plt.xlabel("Spieler-Nummer")
    plt.ylabel("Trefferquote")
    plt.title("Trefferquote der Spieler Auswärts")

    # Grafik anzeigen
    plt.show()

for link in box_score_links:
    full_url = f"https://www.cbssports.com{link}"  # Falls relative Links
    response = requests.get(full_url)
    soup = BeautifulSoup(response.text, "html.parser")

    home_team_div = soup.find("div", id="player-stats-home")

    if home_team_div:
        player_names = [cell.get_text(strip=True) for cell in
                        home_team_div.find_all(["td", "a"], class_=["number-element", "name-truncate"])]
        print(f"Spieler des Heimteams von {full_url}: {player_names}")
    else:
        print(f"⚠️ Keine Daten für das Heimteam auf {full_url} gefunden.")

        # Beispiel: Spielernamen aus Tabellen suchen
   # header = soup.find("th")  # Falls die Spaltenüberschrift im ersten <th> steht

   # player_names = [header.get_text(strip=True)] + [cell.get_text(strip=True) for cell in soup.find_all(["td", "a"],
                                                                                                    #    class_=[
                                                                                                        #    "number-element",
                                                                                                       #    "name-truncate"])]

   # print(f"Spieler von {full_url}: {player_names}")

    headers = ['NAME', 'PTS', 'REB', 'AST', 'FG', '3PT', 'FT', 'PF', 'MIN', 'STL', 'BLK', 'TO', 'OREB', 'DREB', '+/-', 'FPTS']


    # Tabelle anzeigen

    #print(df.iloc[0:5])
    #print(df.iloc[5:10])
    #print(df)

    #print(df)
   # print(player_names[110])
   # print(player_names[189])
   # print(player_names[205])
    #print(player_names[205 + 10 * 16])
    #print(player_names[-16])


    # Liste der Spieler aus bestimmten Indizes
    selected_players = player_names[110:190] + player_names[205:-15]

    # Daten zeilenweise in 16er-Gruppen aufteilen
    rows = [selected_players[i:i + 16] for i in range(0, len(selected_players), 16)]

    # DataFrame erstellen
    df_h = pd.DataFrame(rows, columns=headers)
    #print(player_names)
    # Tabelle anzeigen
    #print(df_h)

    #print(df_h['FG'])
    df_h[['Getroffen', 'Geworfen']] = df_h['FG'].apply(split_fg).apply(pd.Series)
    df_h['Trefferquote_Feld'] = df_h.apply(lambda row: tg(row['Getroffen'], row['Geworfen']), axis=1)

    df_h['Trefferquote_Feld'] = pd.to_numeric(df_h['Trefferquote_Feld'], errors='coerce')

    # Entferne Zeilen mit NaN-Werten aus `Trefferquote_Feld`
    df_h = df_h.dropna(subset=['Trefferquote_Feld'])

    # Ausgabe der neuen Tabelle

    print(df_h)



    # Erstellen der x-Werte (Durchnummerierung)

    anzahl_werte = df_h[df_h['Trefferquote_Feld'].apply(lambda x:
                                                        isinstance(x, (int, float)))]['Trefferquote_Feld'].ge(0).sum()

    print(f"Anzahl der Werte ≥ 0: {anzahl_werte}")

    x_values = range(1, anzahl_werte + 1)  # Neue x-Achsen-Werte für die Grafik

    # Erstellen der y-Werte (Trefferquote)
    y_values = df_h['Trefferquote_Feld'][0:anzahl_werte]

    # Spielernamen für die Beschriftung
    player_names = df_h['NAME'][0:anzahl_werte]

    print(x_values)
    print(y_values)
    print(player_names)

    # Balkendiagramm erstellen
    plt.figure(figsize=(12, 6))
    plt.bar(x_values, y_values, color="dodgerblue")

    # Namen neben die Balken setzen
    valid_data = df_h[df_h['Trefferquote_Feld'].apply(lambda x: isinstance(x, (int, float)))]

    for x, y, name in zip(valid_data.index, valid_data['Trefferquote_Feld'], valid_data['NAME']):
        plt.text(x + 1 , y / 2, str(name), ha="center", va="center", fontsize=6, color="black", fontweight="bold")
    # Achsenbeschriftungen und Titel
    plt.xlabel("Spieler-Nummer")
    plt.ylabel("Trefferquote")
    plt.title("Trefferquote der Spieler Home")

# Grafik anzeigen
    plt.show()





