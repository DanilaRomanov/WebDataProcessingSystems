# %% imports
from spacy import displacy
from beautifulsoup import scraping_bbc, scraping_wikipedia
from spacy_time import spacy_time
import spacy
import pandas as pd
import numpy as np
import claucy

# %% pipeline
nlp = spacy.load("en_core_web_md")
# this gives an error in spacy_time function
nlp.add_pipe("entityLinker", last=True)
claucy.add_to_pipe(nlp)

# %% list to hold tokens
processed_tokens = np.array([])

# html document
url = "https://www.bbc.com/news/world-us-canada-58988523"
stripped_text = scraping_bbc(url)

# url_wikipedia = 'https://en.wikipedia.org/wiki/Dutch_conquest_of_the_Banda_Islands'
# stripped_text = scraping_wikipedia(url_wikipedia)

# %%
# array to string
text = ' '.join(map(str, stripped_text))

# THIS GIVES AN ERROR BECAUSE OF '...' IN THE TEXT. lets fix it
text = text[:4960]
print(text)

# %% SPACY - read text and return doc to work with
doc = spacy_time(text, nlp)
# print(doc)

# %% creating df and empty arrays
tokens_df = pd.DataFrame()

token_text = np.array([])
pos = np.array([])
lemma = np.array([])
ent_type = np.array([])
synt_dep = np.array([])

# %% NLP Preprocessing

tokens = doc

for token in tokens:
    # print(token, token.ent_type_)
    token_text = np.append(token_text, token)
    pos = np.append(pos, token.pos_)
    lemma = np.append(lemma, token.lemma_)
    ent_type = np.append(ent_type, token.ent_type_)
    synt_dep = np.append(synt_dep, token.dep_)

tokens_df['token'] = token_text
tokens_df['pos_tag'] = pos
tokens_df['lemma'] = lemma
tokens_df['entity_type'] = ent_type
tokens_df['syntactic_dependency'] = synt_dep

tokens_df.head(20)

# %% Named Entity Recognition

ner_df = pd.DataFrame()
ner_labels = np.array([])
ner_types = np.array([])

# doc.ents are the named entities in the document.
# Returns a tuple of named entity Span objects, if the entity recognizer has been applied.
# recognizes when whitespace is necessary, such as in a persons name

for ent in doc.ents[:50]:
    ner_labels = np.append(ner_labels, ent.text)
    ner_types = np.append(ner_types, ent.label_)

ner_df['label'] = ner_labels
ner_df['ner_type'] = ner_types

ner_df.head(10)


# REMEMBER TO REMOVE DUPLICATES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11

# %%  Open Relation Extraction - ClausIE

print('==================')

for clause in doc._.clauses:
    print(clause.to_propositions(as_text=False))
    # print(clause)

# %% checking the first article's similarity to another article (uses word2vec on document level, i think)

# url2 = 'https://www.bbc.com/news/business-63715388'
# stripped_text2 = scraping_bbc(url2)
# text2 = ' '.join(map(str, stripped_text2))
# doc2 = spacy_time(text2, nlp)

# print(doc.similarity(doc2))  # the two articles were 98% similar!!

# %% Entity Linking

# for en in doc._.linkedEntities:

#     print(
#         f'entity: {en.get_span()} | {en.get_label()} | {en.get_description()} | {en.get_url()}')
