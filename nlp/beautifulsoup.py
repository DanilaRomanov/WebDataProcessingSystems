from bs4 import BeautifulSoup
import requests
import numpy as np
import re


def _get_soup(html_doc):
    soup = BeautifulSoup(html_doc, parser="html.parser", features="lxml")
    return soup


def _apply_regex_pattern(regex_pattern, p_text):
    text = p_text
    if re.findall((regex_pattern), p_text):
        matches = re.findall(regex_pattern, p_text)

        for match in matches:

            if regex_pattern == "\d+,\d+":
                match_comma = match.replace(",", "")

                print("match:", match)
                p_text = p_text.replace(match, match_comma)
            else:
                p_text = p_text.replace(match, "")
            for match in matches:
                print("match:", match)
                p_text = p_text.replace(match, " ")

        # avoid cascading punctuation
        if " ... " in p_text:
            text = np.append(text, p_text.replace(" ... ", ".."))

        else:
            text = np.append(text, p_text)

    return text


def fetch_webpage(url):
    # get html document
    web_page = requests.get(url)
    return web_page.content


def scrape_webpage(html_doc):
    text = np.array([])
    soup = _get_soup(html_doc)
    # saving text
    article_text = soup.find_all("p")
    # getting article text
    for p in article_text:
        p_text = p.get_text()
        pattern_citation = "\[\d\]"
        # remove citations
        p_text = _apply_regex_pattern(pattern_citation, p_text)
        text = np.append(text, p_text)

    return text
