from beautifulsoup import scraping_bbc
import sys
import numpy as np
import re
import shutil
from warcio.archiveiterator import ArchiveIterator


def get_nlp_doc(html_doc, nlp, print=False):
    # get url from warc file
    # (html_doc, warc_trec_id) = read_warc(warc_file)

    # process html-file, get raw text back
    stripped_text = scraping_bbc(html_doc)

    try:
        doc = nlp(text)
        return doc
    except:
        print("Error:", sys.exc_info())
