from beautifulsoup import scraping_bbc
import sys


def get_nlp_doc(url, nlp):
    stripped_text = scraping_bbc(url)

    # convert stripped_text array to string for processing
    text = ' '.join(map(str, stripped_text))

    print('\n============= RAW TEXT =============\n')
    print(stripped_text)

    try:
        doc = nlp(text)

        print('\n============= STRIPPED TEXT =============\n')
        print(doc)

        return doc
    except:
        print("Error:", sys.exc_info())
