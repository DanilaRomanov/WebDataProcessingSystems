# imports
import gzip
from get_nlp_doc import get_nlp_doc
import spacy
import claucy
import numpy as np
from warcio.archiveiterator import ArchiveIterator
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from get_nlp_doc import read_warc
from starter_code import find_entities

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


# SPACY - read text and return doc to work with
doc = get_nlp_doc(warc_file, nlp)
print(doc)

# %%
