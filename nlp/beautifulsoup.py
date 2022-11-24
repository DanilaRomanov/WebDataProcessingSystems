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
    links = article.find_all('a')
    title = article.find_all('h1')
    text = article.find_all('p')
    subtitles = article.find_all('span')

    # article text
    for p in text:
        # print(p.get_text())
        text = np.append(text, p.get_text())

    # article titles
    for h1 in title:
        # print(h1.get_text())
        text = np.append(text, h1.get_text())

    # article links
    for l in links:
        link = l.get('href')

        if 'http' not in link:
            # replace with general link (or not??)
            link = 'https://www.bbc.co.uk' + link

        # print(f'link text "{l.get_text()}"')
        # print(f'link url "{link}"')

    # return
    return text
