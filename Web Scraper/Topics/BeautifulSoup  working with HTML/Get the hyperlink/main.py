import requests

from bs4 import BeautifulSoup

number = int(input())
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
for link in soup.find_all('a'):
    href = link.get('href')
    if href and href.find(str(number)) > -1:
        position = link.get('href').find('#')
        print(link.get('href')[position:])
