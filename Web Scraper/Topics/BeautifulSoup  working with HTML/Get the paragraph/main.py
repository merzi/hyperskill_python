import requests

from bs4 import BeautifulSoup

word = input()
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
for paragraph in soup.find_all('p'):
    if paragraph.get_text().find(word) > -1:
        print(paragraph.get_text())
        break
