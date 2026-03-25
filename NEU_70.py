import requests  # Importieren der requests-Bibliothek, um HTTP-Anfragen zu stellen und Webseiten abzurufen.
from bs4 import BeautifulSoup  # BeautifulSoup wird importiert, um HTML- oder XML-Inhalte zu parsen und zu analysieren.

# Die URL der Zielwebseite wird definiert.
url = "https://niklasstat.github.io/Statistik_R/index_4.html"

# Ein Dictionary mit HTTP-Headern wird erstellt.
# Der `User-Agent` wird hinzugefügt, um die Anfrage wie von einem Browser aussehen zu lassen (manche Seiten blockieren automatisierte Anfragen).
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Senden einer HTTP-GET-Anfrage an die definierte URL. Die Header werden mitgeschickt, um die Anfrage "legitim" erscheinen zu lassen.
response = requests.get(url, headers=headers)

# Überprüfen, ob die Anfrage erfolgreich war. Ein Statuscode von 200 bedeutet Erfolg (HTTP 200 = "OK").
if response.status_code == 200:
    # Wenn die Anfrage erfolgreich war, wird der HTML-Inhalt der Webseite mit BeautifulSoup geparst.
    # Der `html.parser` wird als Parser verwendet, um den HTML-Code zu analysieren.
    soup = BeautifulSoup(response.content, "html.parser")

    # Alle HTML-Tags, die Überschriften enthalten können (<h1> bis <h6>), werden gesucht.
    headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

    # Überschriften werden gefiltert, um nur die Überschriften zu finden, die das Wort "Quersummen" enthalten.
    # `heading.text.strip()` entfernt überflüssige Leerzeichen aus den Textinhalten der Überschriften.
    quersummen_headings = [heading.text.strip() for heading in headings if "Quersummen" in heading.text]

    # Überprüfen, ob Überschriften gefunden wurden, die "Quersummen" enthalten.
    if quersummen_headings:
        print("Gefundene Überschriften mit 'Quersummen':")
        # Jede gefundene Überschrift wird nacheinander ausgegeben.
        for heading in quersummen_headings:
            print(heading)
    else:
        # Wenn keine Überschriften mit "Quersummen" gefunden wurden, wird eine entsprechende Nachricht ausgegeben.
        print("Keine Überschriften mit 'Quersummen' gefunden.")
else:
    # Falls die Anfrage fehlschlägt, wird der HTTP-Statuscode ausgegeben, um den Fehler zu diagnostizieren.
    print(f"Fehler beim Abrufen der Webseite. Statuscode: {response.status_code}")

# Eine zusätzliche Zeile wird ausgegeben, um das Ende der Skriptausführung zu markieren.
print('_______')
soup = BeautifulSoup(response.content, "html.parser")
headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

for element in headings:
    print(element.text)
    print(element.text.strip())