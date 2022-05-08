import requests

from bs4 import BeautifulSoup


def get_heading(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find('h1').get_text()


print(get_heading(input()))
