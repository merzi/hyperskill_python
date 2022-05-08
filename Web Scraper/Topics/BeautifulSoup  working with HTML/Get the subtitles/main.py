import requests

from bs4 import BeautifulSoup


def get_subtitles(uri, index):
    r = requests.get(uri)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find_all('h2')[index].get_text()


i = int(input())
url = input()
print(get_subtitles(url, i))
