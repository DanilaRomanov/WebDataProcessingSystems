from beautifulsoup import scraping_bbc
import sys


def get_nlp_doc(url, nlp):
    stripped_text = scraping_bbc(url)

    # convert stripped_text array to string for processing
    # text = ' '.join(map(str, stripped_text))

    # print('\n============= RAW TEXT =============\n')
    # print(stripped_text)

    # try:
    for text in stripped_text[0:6]:
        if(len(text)) < 2:
            continue

        for char in text:
            if char.isascii():
                # char.encode(encoding='UTF-8').decode('ascii')
                continue
            else:
                print('========== char:', char)
                text = text.replace(char, '')

        print('\n============= RAW TEXT =============\n')
        print('length:', len(text))
        text = str(text)
        print('type:', type(text))
        print('text:', text)

        doc = nlp(str(text))

        print('\n============= STRIPPED TEXT =============\n')
        print(doc)

        # return doc
    # except:
    #     print("Error:", sys.exc_info())
