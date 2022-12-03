from bs4 import BeautifulSoup
import requests
import numpy as np
import re


def get_soup(url):
    web_page = requests.get(url)
    html_doc = web_page.content
    soup = BeautifulSoup(html_doc, parser="html.parser", features="lxml")
    return soup


def scraping_wikipedia(url):
    soup = get_soup(url)
    text = np.array([])

    # saving text
    body_text = soup.find('div', id="mw-content-text")
    main_text = body_text.find_all('p')
    main_text_titles = body_text.find_all('span', {'class': 'mw-headline'})

    for p in main_text:
        # print(p.get_text())
        text = np.append(text, p.get_text())

    # for span in main_text_titles:
    #     # print(span.get_text())
    #     text = np.append(text, span.get_text())

    return text


def scraping_cnn(url):
    soup = get_soup(url)
    text = np.array([])

    # saving text
    article = soup.find('div', {'class': "article__content"})
    article_text = article.find_all('p')

    # avoid cascading punctuation
    print('text', article.find_all(text=re.compile("[.]{2,}")))

    # main_text_titles = article_text.find_all('span', {'class': 'mw-headline'})

    for p in article_text:
        text = np.append(text, p.get_text())

    return text


def scraping_bbc(url):
    text = np.array([])
    soup = get_soup(url)

    # saving text
    article = soup.find("article")

    # avoid cascading punctuation
    # print('text', article.find_all(text=re.compile("[.]{2,}")))

    article_links = article.find_all('a')
    article_title = article.find_all('h1')
    article_text = article.find_all('p')
    subtitles = article.find_all('span')

    # getting article titles
    # for h1 in article_title:
    # print(h1.get_text())
    # text = np.append(text, h1.get_text())

    # getting article text
    for p in article_text:
        # print(p.get_text())

        if ' ... ' in p.get_text():
            text = np.append(text, p.get_text().replace(' ... ', ' .'))
        else:
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


# url = "https://www.bbc.com/news/uk-63743259"
# stripped_text = scraping_bbc(url)
# print('strip', stripped_text)
