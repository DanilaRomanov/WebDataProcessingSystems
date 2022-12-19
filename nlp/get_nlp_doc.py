from beautifulsoup import scraping_bbc
import sys
import numpy as np
from warcio.archiveiterator import ArchiveIterator


def read_warc(warc_file):
    links = np.array([])

    # open warc file and save all links to an array
    with open(warc_file, 'rb') as stream:
        for record in ArchiveIterator(stream):
            if record.rec_type == 'response':
                print('headers', record.rec_headers.get_header('WARC-Trec-ID'))
                # links = np.append(
                #     links, record.rec_headers.get_header('WARC-Target-URI'))
    return
    # if links are found
    if len(links) > 0:
        link = ''

        #  find the first valid homepage url
        for link in links:
            if link[:4] == 'http' \
                    and (link[len(link)-4:] != '.jpg') \
                    and (link[len(link)-4:] != '.png') \
                    and (link[len(link)-4:] != '.gif') \
                    and (link[len(link)-5:] != '.jpeg')\
                    and (link[len(link)-3:] != '.js')\
                    and (link[len(link)-4:] != '.txt'):
                print('valid url', link)
                return link

        # print('First valid homepage url', links[0])
        return links[0]
    else:
        print('Oops! Found no url in warc file!')
        print(links)
        return Exception('Oops! Found no url in warc file!')


def get_nlp_doc(warc_file, nlp):
    # get url from warc file
    url = read_warc(warc_file)

    # process html-file, get raw text back
    stripped_text = scraping_bbc(url)

    try:
        # join the returned array together
        text = ' '.join(map(str, stripped_text))

        # create spacy doc file
        doc = nlp(text)
        return doc
    except:
        print("Error:", sys.exc_info())
