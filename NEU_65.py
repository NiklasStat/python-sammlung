import requests  # Die requests-Bibliothek wird importiert, um HTTP-Anfragen an eine Webseite zu senden.
from bs4 import \
    BeautifulSoup  # BeautifulSoup wird importiert, um die HTML-Inhalte der Webseite zu analysieren und zu durchsuchen.

# Die URL der Bundesliga-Tabelle auf der Sportschau-Webseite.
url = "https://www.sportschau.de/live-und-ergebnisse/fussball/deutschland-bundesliga/tabelle"

# Sende eine HTTP-GET-Anfrage, um die Inhalte der Webseite abzurufen.
response = requests.get(url)

# Überprüfe, ob die Anfrage erfolgreich war (Statuscode 200 bedeutet Erfolg).
if response.status_code == 200:
    # Analysiere die HTML-Inhalte der Webseite mit BeautifulSoup.
    soup = BeautifulSoup(response.content, "html.parser")

    # Suche nach dem ersten Tabellen-Element auf der Seite.
    # Dies ist nur ein Beispiel und sollte an die spezifische Struktur der Webseite angepasst werden.
    team_table = soup.find("table")  # Hier wird angenommen, dass die Tabelle als <table>-Element dargestellt wird.

    # Finde alle Tabellenzeilen (<tr>), um durch die Teams zu iterieren.
    rows = team_table.find_all("tr")

    # Iteriere durch jede Zeile in der Tabelle.
    for row in rows:
        # Überprüfe, ob der Name "Bayer Leverkusen" in der Zeile vorkommt.
        if "Bayer Leverkusen" in row.text:
            # Finde alle Tabellenspalten (<td>) in der aktuellen Zeile.
            columns = row.find_all("td")

            # Nimm an, dass die Punkte in der letzten Spalte der Tabelle stehen.
            points = columns[-1].text.strip()  # Extrahiere den Text und entferne zusätzliche Leerzeichen.

            # Gib die Punkte von Bayer Leverkusen aus.
            print(f"Bayer Leverkusen's points: {points}")
else:
    # Falls die Anfrage fehlschlägt, gib den HTTP-Statuscode aus.
    print("Failed to retrieve the webpage. Status code:", response.status_code)