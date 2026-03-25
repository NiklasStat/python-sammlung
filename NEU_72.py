import requests
from bs4 import BeautifulSoup as bs
import re

# Load webpage content

r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

# Convert to a beautiful soup object

soup = bs(r.content, "lxml")

print(soup)
print("_______j___")
print(soup.prettify())

print('________g____')
first_header = soup.find("h2")
print(first_header)

headers = soup.find_all("h2")
print(headers)

print("------r-----")

first_header = soup.find(["h2", "h1"])
print(first_header)

headers = soup.find_all(["h1", "h2"])
print(headers)

print("-------e---")

headings = [tag.get_text(strip=True) for tag in soup.find_all(["h1", "h2"])]

print(headings)  # Gibt die Überschriften als Liste aus

paragraph = soup.find_all("p", attrs = {"id": "paragraph-id"})
print(paragraph)
print("___f__")
body = soup.find('body')
print(body)

print("_____b______")

div = body.find('div')
print(div)
print('------k---')
header = div.find('h1')
print(header)

paragraphs = soup.find_all("p", string = "Some bold text") # ganzer string muss passen
print(paragraphs)
print("_______n____")
paragraphs = soup.find_all("p", string = re.compile("Some")) # ganzer string muss passen
print(paragraphs)

print("_----f-------")
headers = soup.find_all("h2", string = re.compile("(H|h)eader"))
print(headers)

print("-------l-----")

content = soup.select("p") # bei css selektoren
print(content)

print("___________j________")

print(soup.body.prettify())

content = soup.select("div p") # paragraphs inside divs
print(content)







