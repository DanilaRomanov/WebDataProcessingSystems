from beautifulsoup import scraping_bbc
import sys
import numpy as np


def get_nlp_doc(url, nlp):
    stripped_text = scraping_bbc(url)
    # doc_array = np.array([])

    try:
        # print('\n============= RAW TEXT =============\n')
        # print(str(stripped_text))

        # for text in stripped_text:
        #     if(len(text)) < 2:
        #         continue
        text = ' '.join(map(str, stripped_text))
        doc = nlp(text)

        # doc_array = np.append(doc_array, doc)

        # print('\n============= STRIPPED TEXT =============\n')
        return doc
    except:
        print("Error:", sys.exc_info())
