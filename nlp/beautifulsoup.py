from bs4 import BeautifulSoup
import requests
import numpy as np
import re


def get_soup(html_doc):
    soup = BeautifulSoup(html_doc, parser="html.parser", features="lxml")
    return soup


def scraping_bbc(url):
    web_page = requests.get(url)
    html_doc = web_page.content
    text = np.array([])

    soup = get_soup(html_doc)

    # saving text
    article = soup.find("article")

    print('text', article.find_all(text=re.compile("[.]{2,}")))

    article_links = article.find_all('a')
    article_title = article.find_all('h1')
    article_text = article.find_all('p')
    subtitles = article.find_all('span')

    # getting article titles
    for h1 in article_title:
        # print(h1.get_text())
        text = np.append(text, h1.get_text())

    # getting article text
    for p in article_text:
        # print(p.get_text())
        text = np.append(text, p.get_text())

    # getting article links
    # for l in article_links:
    #     link = l.get('href')

    #     if 'http' not in link:
    #         # replace with general link (or not??)
    #         link = 'https://www.bbc.co.uk' + link

        # print(f'link text "{l.get_text()}"')
        # print(f'link url "{link}"')

    # return
    return text


url = "https://www.bbc.co.uk/news/uk-63743259"
scraping_bbc(url)
