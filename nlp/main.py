# %% imports
from beautifulsoup import scraping_bbc
from spacy_time import spacy_time
import spacy
import pandas as pd
import numpy as np

# %% nlp load
nlp = spacy.load("en_core_web_sm")
lemmatizer = nlp.get_pipe("lemmatizer")

# list to hold tokens
processed_tokens = np.array([])

# %% html document
url = "https://www.bbc.co.uk/news/uk-63743259"

stripped_text = scraping_bbc(url)

# %% array to string

# text = np.array_str(stripped_text)
# text = np.array2string(stripped_text, precision=2, separator=",")
text = ' '.join(map(str, stripped_text))

# print(text)

# %% SPACY TIME - read text and return doc to work with

doc = spacy_time(text, nlp)

# %% creating df and empty arrays

df = pd.DataFrame()

token_text = np.array([])
pos = np.array([])
lemma = np.array([])

# %% tokenize, pos tag, lemma and add to dataframe

tokens = doc

for token in tokens[:50]:
    print(token, token.pos_)
    token_text = np.append(token_text, token)
    pos = np.append(pos, token.pos_)
    lemma = np.append(lemma, token.lemma_)

df['token'] = token_text
df['pos tag'] = pos
df['lemma'] = lemma

# %% print df

print(df.head())

# %% for each token, add a lemma tag?

# lemmatizer requires pos-tags
# %%
