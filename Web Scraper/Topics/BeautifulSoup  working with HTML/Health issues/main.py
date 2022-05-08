import requests

from bs4 import BeautifulSoup

letter = 'S'
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

links = []
for link in soup.find_all('a'):
    text = link.get_text()
    href = link.get('href')
    if text.startswith('S') and len(text) > 1 and (href.find('topics') > -1 or href.find('entity') > -1):
        links.append(link.get_text())

print(links)
