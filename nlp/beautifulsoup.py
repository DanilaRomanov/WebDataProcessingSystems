from bs4 import BeautifulSoup


def bs_time(html_doc):
    soup = BeautifulSoup(html_doc, features="lxml")
    # print(soup.prettify())
    # return soup.prettify()
    return soup.get_text()