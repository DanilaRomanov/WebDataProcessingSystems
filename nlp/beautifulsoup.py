from bs4 import BeautifulSoup
import requests
import numpy as np


def get_soup(html_doc):
    soup = BeautifulSoup(html_doc, parser="html.parser", features="lxml")
    return soup


def scraping_bbc(url):
    web_page = requests.get(url)
    html_doc = web_page.text
    text = np.array([])

    soup = get_soup(html_doc)

    # getting text
    article = soup.find("article")
    article_links = article.find_all('a')
    article_title = article.find_all('h1')
    article_text = article.find_all('p')
    subtitles = article.find_all('span')

    # article titles
    for h1 in article_title:
        # print(h1.get_text())
        text = np.append(text, h1.get_text())

    # article text
    for p in article_text:
        # print(p.get_text())
        text = np.append(text, p.get_text())

    # article links
    for l in article_links:
        link = l.get('href')

        if 'http' not in link:
            # replace with general link (or not??)
            link = 'https://www.bbc.co.uk' + link

        # print(f'link text "{l.get_text()}"')
        # print(f'link url "{link}"')

    # return
    return text
