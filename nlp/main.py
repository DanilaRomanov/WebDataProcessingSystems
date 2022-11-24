# %% imports
from spacy import displacy
from beautifulsoup import scraping_bbc
from spacy_time import spacy_time
import spacy
import pandas as pd
import numpy as np

# %% nlp load
nlp = spacy.load("en_core_web_sm")
# lemmatizer = nlp.get_pipe("lemmatizer")
# ner = nlp.add_pipe("ner")

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

tokens_df = pd.DataFrame()

token_text = np.array([])
pos = np.array([])
lemma = np.array([])
ent_type = np.array([])
synt_dep = np.array([])

# %% tokenize, pos tag, lemma and add to dataframe

tokens = doc

for token in tokens[:50]:
    print(token, token.ent_type_)
    token_text = np.append(token_text, token)
    pos = np.append(pos, token.pos_)
    lemma = np.append(lemma, token.lemma_)
    ent_type = np.append(ent_type, token.ent_type_)
    synt_dep = np.append(synt_dep, token.dep_)

tokens_df['token'] = token_text
tokens_df['pos tag'] = pos
tokens_df['lemma'] = lemma
tokens_df['entity type'] = ent_type
tokens_df['syntactic dependency'] = synt_dep

# %% print df

print(tokens_df.head(20))

# %% prints

# token = tokens[0]
# print(token)
# print(token.text)
# print(token.ent_type_)  # geopolitical entity
# print(token.left_edge)


sentence1 = list(tokens.sents)
print(list(tokens.sents))
displacy.render(sentence1, style="dep")  # cool pics


# %% Named Entity Recognition

# doc.ents are the named entities in the document.
# Returns a tuple of named entity Span objects, if the entity recognizer has been applied.
# recognizes when whitespace is necessary, such as in a persons name

# save entities to df i guess

ent_labels = np.array([])


for ent in doc.ents[:50]:
    print(ent.text, ent.label_)

# %%

# %%
