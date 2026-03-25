import requests
from bs4 import BeautifulSoup

response = requests.get('https://example.com')
print(response.text)  # Gibt den HTML-Inhalt der Seite als Text zurück

