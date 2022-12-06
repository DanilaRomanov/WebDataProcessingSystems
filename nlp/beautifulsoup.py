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
    # article = soup.find("article")

    # article_links = article.find_all('a')
    # article_title = article.find_all('h1')
    article_text = soup.find_all('p')
    # subtitles = article.find_all('span')

    # getting article titles
    # for h1 in article_title:
    # print(h1.get_text())
    # text = np.append(text, h1.get_text())

    # article_text = [
    #     'Carl Friedrich Busky (1743-1808), a wealthy merchant and Prussian consul, acquired the mansion in 1775.\n']

    # getting article text
    for p in article_text:
        p_text = p.get_text()
        pattern = '\[\d\]'

        if re.findall(pattern, p_text):
            print('hhhhhhh', p_text)

            matches = re.findall(pattern, p_text)

            for match in matches:
                print('match', match)
                p_text = p_text.replace(match, '')

        # avoid cascading punctuation
        if ' ... ' in p_text:
            text = np.append(text, p_text.replace(' ... ', ' .. '))

        else:
            text = np.append(text, p_text)

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
