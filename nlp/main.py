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
# print('Stripped of HTML: \n', stripped_text)

# %%


# %% Tokenization

doc = spacy_time(stripped_text, nlp)

# %%
print('len text', len(stripped_text))
print('len doc', len(doc))


# %% Print tokens collected (doc)
tokens = doc

for token in tokens[:50]:
    print(token, token.pos_)
    # print(token.pos_)
# %% for each token, add a lemma tag?

# lemmatizer requires pos-tags
# %%
