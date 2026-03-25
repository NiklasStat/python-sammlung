import requests
from bs4 import BeautifulSoup

# URL der ursprünglichen Seite
base_url = "https://example.com"

# HTTP-Header hinzufügen, um die Anfrage wie von einem Browser aussehen zu lassen
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

# Abrufen der ursprünglichen Seite
response = requests.get(base_url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Extrahiere die Links (aktualisiere den Selektor entsprechend der HTML-Struktur)
    links = soup.find_all("a", class_="relevant-class")  # Passe Klasse/Selektor an
    for link in links:
        href = link.get("href")
        if href:
            full_url = href if href.startswith("http") else f"{base_url.rstrip('/')}/{href.lstrip('/')}"

            # Neue Seite abrufen
            new_response = requests.get(full_url, headers=headers)
            if new_response.status_code == 200:
                new_soup = BeautifulSoup(new_response.content, "html.parser")

                # Titel oder andere relevante Inhalte finden
                title_tag = new_soup.find("title")
                if title_tag:
                    page_title = title_tag.text.strip()
                    print(f"Seite: {full_url} - Titel: {page_title}")
                else:
                    print(f"Kein Titel auf der Seite: {full_url}")
            else:
                print(f"Fehler beim Abrufen der Seite: {full_url}")
else:
    print("Fehler beim Abrufen der ursprünglichen Seite. Statuscode:", response.status_code)