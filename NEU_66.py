from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python&cboWorkExp1=-1&txtLocation=').text


soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_ ="ui-tabs-active ui-state-active")

print(jobs)

#jobs_2 = soup.find_all('li', id = "expLiAnchor")
#print(jobs_2)

jobs = soup.find_all(class_ ="ui-tabs-active ui-state-active")
print(jobs)

#print(soup.prettify())  # Gibt den gesamten HTML-Code schön formatiert aus
# Um sicherzustellen, dass du den richtigen HTML-Code durchsuchst, kannst du die Inhalte ausgeben:

hh = soup.find_all('h2')
for element in hh:
    print(element.text)
    print(element.text.strip())





# Beispiel 1: Entfernen von Leerzeichen
text = "   Hallo Welt!   "
bereinigt = text.strip()
print(f"Original: '{text}'")
print(f"Bereinigt: '{bereinigt}'")

# Beispiel 2: Entfernen von bestimmten Zeichen
text2 = "###Python ist toll###"
bereinigt2 = text2.strip("#")
print(f"Original: '{text2}'")
print(f"Bereinigt: '{bereinigt2}'")