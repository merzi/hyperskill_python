#  You can experiment here, it won’t be checked
import os
import re
import string

import requests

from bs4 import BeautifulSoup


def send_quote_request(uri):
    r = send_url_request(uri)
    if not r:
        return "Invalid quote resource!!"

    return r.content if 'content' in r.json() else "Invalid quote resource!!"


def send_movie_request(uri):
    if not check_movie_link(uri):
        return 'Invalid movie page!'

    soup = get_beautifulsoup_response(uri)
    title = soup.find('h1').get_text()
    description = soup.find('span', {'class', 'GenresAndPlot__TextContainerBreakpointXL-sc-cum89p-2'})
    if description:
        description = description.get_text()
    else:
        description = ""

    return {'title': title,
            'description': description}


def check_movie_link(uri):
    return uri.find('/title/') > -1 and uri.find('imdb.com') > -1


def send_url_request(uri):
    return requests.get(uri)


def get_beautifulsoup_response(uri):
    soup = BeautifulSoup(send_url_request(uri).text, "html.parser")
    return soup


def safe_url_content(uri, file_name="source.html"):
    r = send_url_request(uri)
    if r.status_code == 200:
        open_file = open(file_name, "wb")
        try:
            open_file.write(r.content)
        finally:
            open_file.close()
            return "Content saved."

    return f"The URL returned {r.status_code}!"


def save_article():
    domain = "https://www.nature.com"
    uri = domain + "/nature/articles?sort=PubDate&year=2020&page=3"
    soup = get_beautifulsoup_response(uri)
    saved_articles = process_articles(soup.find_all('article'), domain)

    print("Saved articles:", saved_articles)


def get_file_name(article_title):
    filename_template = string.Template("$article_title.txt")
    title = re.sub(f'[{string.punctuation}]', "", article_title)
    title = re.sub(r"\s+", "_", title)
    return filename_template.substitute(article_title=title)


def safe_article_file(uri):
    soup = get_beautifulsoup_response(uri)
    if type(soup.find("div", {"class", "c-article-body"})) == type(None):
        print(uri)
        return False

    article_text = soup.find("div", {"class", "c-article-body"}).get_text().strip()
    file_name = get_file_name(soup.find('h1', {"class", "c-article-magazine-title"}).get_text())
    try:
        file = open(file_name, "w+", encoding="utf-8")
        try:
            file.write(article_text)
        except Exception as e:
            result = False
        else:
            result = file_name
        finally:
            file.close()
    except OSError:
        result = False

    return result


def normalize_article_type(article_type):
    return article_type.replace(' ', '-')


def process_articles(articles, article_type, domain):
    saved_articles = []
    for article in articles:
        span = article.findChildren('span', {'class', 'c-meta__type'})[0]
        if span.get_text() == article_type:
            link = article.findChildren('a', {'class', 'c-card__link'})[0]
            res = safe_article_file(domain + link.get('href'))
            if res is not False:
                saved_articles.append(res)
    return saved_articles


def save_article2(page_numbers, article_type):
    dir_template = string.Template("Page_$page_number")
    base_path = os.getcwd()
    domain = "https://www.nature.com"
    base_uri = "/nature/articles?sort=PubDate&year=2020"
#    uri = string.Template("$domain$base_path&type=$article_type&page=$page_number")
    uri = string.Template("$domain$base_path&page=$page_number")
    saved_articles = []
#    article_type = normalize_article_type(article_type)
    for page_number in range(1, page_numbers + 1):
        os.chdir(base_path)
        soup = get_beautifulsoup_response(uri.substitute(domain=domain, base_path=base_uri,
                                                         page_number=page_number))
        os.mkdir(dir_template.substitute(page_number=page_number))
        os.chdir(dir_template.substitute(page_number=page_number))
        saved_articles.extend(process_articles(soup.find_all('article'), article_type, domain))

    print("Saved all articles.")
    return saved_articles


# print("Input the URL:")
# url = input()
# print(safe_url_content(url))
pages = int(input())
articles_type = input()
save_article2(pages, articles_type)
