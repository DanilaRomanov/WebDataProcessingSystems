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
    article_text = soup.find_all("p")

    # getting article text
    for p in article_text:
        p_text = p.get_text()
        pattern = "\[\d\]"

        # remove citations
        if re.findall(pattern, p_text):
            matches = re.findall(pattern, p_text)

            for match in matches:
                print("match:", match)
                p_text = p_text.replace(match, " ")

        # avoid cascading punctuation
        if " ... " in p_text:
            text = np.append(text, p_text.replace(" ... ", ".."))

        else:
            text = np.append(text, p_text)

    return text
