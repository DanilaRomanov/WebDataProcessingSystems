from bs4 import BeautifulSoup
import requests
import numpy as np
import re


def get_soup(url):
    web_page = requests.get(url)
    html_doc = web_page.content
    soup = BeautifulSoup(html_doc, parser="html.parser", features="lxml")
    return soup


def scraping_bbc(url):
    text = np.array([])
    soup = get_soup(url)

    # saving text
    article_text = soup.find_all('p')

    # getting article text
    for p in article_text:
        p_text = p.get_text()
        pattern_citation = '\[\d\]'

        # remove citations
        p_text = apply_regex_pattern(pattern_citation, p_text)
        text = np.append(text, p_text)

    return text


def apply_regex_pattern(regex_pattern, p_text):
    if re.findall((regex_pattern), p_text):
        matches = re.findall(regex_pattern, p_text)

        for match in matches:

            if regex_pattern == '\d+,\d+':
                match_comma = match.replace(',', '')

                print('match:', match)
                p_text = p_text.replace(match, match_comma)
            else:
                p_text = p_text.replace(match, '')

    return p_text
