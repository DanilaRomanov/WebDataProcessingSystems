# %% imports
from get_nlp_doc import get_nlp_doc
from nlp_preprocessing import nlp_preprocessing
from clausie_relation_extraction import clausie_rel_extract
from entity_relation_linking import entity_relation_linking
from ner import ner
import spacy
import pandas as pd
import numpy as np
import claucy

# %% ============================================================================================

# pipeline
nlp = spacy.load("en_core_web_md")
nlp.add_pipe("entityLinker", last=True)  # entity linker
claucy.add_to_pipe(nlp)  # Open IE


# html document
url = "https://www.cbc.ca/news/world/trump-organization-taxes-guilty-1.6676368"

# SPACY - read text and return doc to work with
doc = get_nlp_doc(url, nlp)


# %% ============================================================================================

# NLP Preprocessing
tokens_df = nlp_preprocessing(doc)
tokens_df.head(10)


# %% ============================================================================================

# Named Entity Recognition
ner_df = ner(doc)
ner_df.head(20)


# %%  ============================================================================================

# Open Relation Extraction - ClausIE
clauses_df = clausie_rel_extract(doc)
clauses_df.head(20)


# %% ============================================================================================

# Open Relation Extraction - Get the relations in which the usbject and object are named entities
entity_relation_linking(ner_df, clauses_df)

# %% ============================================================================================

# checking the first article's similarity to another article (uses word2vec on document level, i think)

# url2 = 'https://www.bbc.com/news/business-63715388'
# stripped_text2 = scraping_bbc(url2)
# text2 = ' '.join(map(str, stripped_text2))
# doc2 = spacy_time(text2, nlp)

# print(doc.similarity(doc2))  # the two articles were 98% similar!!

# %% ============================================================================================

# Entity Linking

# Not allowed to do this :(

# for en in doc._.linkedEntities:

#     print(
#         f'entity: {en.get_span()} | {en.get_label()} | {en.get_description()} | {en.get_url()}')
