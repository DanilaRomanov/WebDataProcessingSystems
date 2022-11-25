# %% imports
from spacy import displacy
from beautifulsoup import scraping_bbc
from spacy_time import spacy_time
import spacy
import pandas as pd
import numpy as np

# %% pipeline
nlp = spacy.load("en_core_web_md")
# this gives an error in spacy_time function
nlp.add_pipe("entityLinker", last=True)

# %% list to hold tokens
processed_tokens = np.array([])

# html document
url = "https://www.bbc.co.uk/news/uk-63743259"
stripped_text = scraping_bbc(url)

# %%
# array to string
text = ' '.join(map(str, stripped_text))

# THIS GIVES AN ERROR BECAUSE OF '...' IN THE TEXT. lets fix it

text = text[:4960]
print(text)

# %% SPACY - read text and return doc to work with
doc = spacy_time(text, nlp)

# %% creating df and empty arrays
tokens_df = pd.DataFrame()

token_text = np.array([])
pos = np.array([])
lemma = np.array([])
ent_type = np.array([])
synt_dep = np.array([])

# %% tokenize, pos tag, lemma and add to dataframe

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

# %% checking the first article's similarity to another article (uses word2vec on document level, i think)

url2 = 'https://www.bbc.com/news/business-63715388'
stripped_text2 = scraping_bbc(url2)
text2 = ' '.join(map(str, stripped_text2))
doc2 = spacy_time(text2, nlp)

print(doc.similarity(doc2))  # the two articles were 98% similar!!

# %% Entity Linking

sentences = list(doc.sents)
named_entities = list(doc.ents)

print(doc._.linkedEntities.pretty_print())

# cool pics showing relations between tokens
# displacy.render(sentence1, style="dep")
# display which highlights entities in the text!!
# displacy.render(doc, style="ent")


# %%
