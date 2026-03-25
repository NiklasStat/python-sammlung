import requests
from bs4 import BeautifulSoup

# URL der Webseite
url = "https://www.cbssports.com/nba/scoreboard/"

# HTTP-GET-Anfrage senden, um die Inhalte der Webseite abzurufen.
response = requests.get(url)

# Überprüfen, ob die Anfrage erfolgreich war.
if response.status_code == 200:
    # HTML-Inhalte analysieren
    soup = BeautifulSoup(response.content, "html.parser")

    # Suche nach dem Bereich, der die Spiele enthält
    games_container = soup.find_all("div", class_="scoreboard")  # Passe die Klasse je nach Struktur an

    for game in games_container:
        # Extrahiere Teamnamen, Punkte oder andere relevante Daten
        teams = game.find_all("div", class_="team")  # Beispiel: Suche nach Teamnamen
        for team in teams:
            print(team.text.strip())  # Ausgabe des Teamnamens

        # Punkte, Zeit oder Status des Spiels (Beispielstruktur)
        game_status = game.find("div", class_="game-status")  # Beispiel: aktueller Spielstatus
        print(game_status.text.strip() if game_status else "Status nicht verfügbar")
else:
    print("Fehler beim Abrufen der Webseite. Statuscode:", response.status_code)
