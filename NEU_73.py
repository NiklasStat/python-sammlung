from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://www.sportschau.de/live-und-ergebnisse/fussball/deutschland-bundesliga/tabelle"

import cloudscraper
scraper = cloudscraper.create_scraper()
response = scraper.get(url)
#print(response.text)

#if response.status_code == 200:
   # soup = BeautifulSoup(response.text, "lxml")
  #  visible_text = soup.get_text(separator="\n", strip=True)  # Entfernt Tags
    #print(visible_text)
#else:
   # None
    #print(f"Fehler {response.status_code}: Zugriff nicht möglich.")


print('_________________')
 # Gibt nur den Text innerhalb des <h2>-Tags aus

soup = BeautifulSoup(response.text, "lxml")
heading = soup.find("h2")
print(heading.get_text(strip=True))

print("HH" if "h2" in response.text else "NOOO")


links = soup.find_all("a")
links = [l.get("href") for l in links]
links = [l for l in links]
print(links)




# Webseite abrufen
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "lxml")
table = soup.find("table")

rows = table.find_all("tr")
data = [[cell.get_text(strip=True) for cell in row.find_all(["th", "td"])] for row in rows]

df = pd.DataFrame(data)
print(df)

