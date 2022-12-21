# imports
import gzip
from get_nlp_doc import get_nlp_doc
import spacy
import claucy
import numpy as np
from warcio.archiveiterator import ArchiveIterator
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from read_warc import read_warc
from starter_code import find_entities

# UNUSED FILE only for testing


# pipeline
nlp = spacy.load("en_core_web_md")
nlp.add_pipe("entityLinker", last=True)  # entity linker
claucy.add_to_pipe(nlp)  # Open IE


# html document
# url = "https://www.bbc.com/news/uk-63743259"
# warc_file = 'sample texts/IAH-20080430204825-00000-blackbook.warc.gz'
# warc_file = 'sample texts/UK_net_migration.warc'
# warc_file = 'sample texts/ClueWeb09_English_Sample_File.warc'
warc_file = 'sample texts/sample.warc'

df = read_warc(warc_file)
# df.head()

for index, row in df.head(1).iterrows():
    # print('HTML_DOC========================\n', row['HTML_DOC'])
    # print('WARC-TREC-ID==================\n', row['WARC-TREC-ID'])
    html_doc = row['HTML_DOC']
    warc_trec_id = row['WARC-TREC-ID']

    doc = get_nlp_doc(html_doc, nlp)
