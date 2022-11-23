# %% imports
from beautifulsoup import bs_time
from spacy_time import spacy_time
import spacy
import requests

# %% nlp load
nlp = spacy.load("en_core_web_sm")

# %% html document
url = "https://www.nytimes.com/international/"
web_page = requests.get(url)
html_doc = web_page.text

print('doc:', html_doc)

# %%
stripped_text = bs_time(html_doc)
print('Stripped of HTML: \n', stripped_text)


# %%

doc = spacy_time(stripped_text, nlp)

# %%

# print('doc:', doc)
print('len text', len(stripped_text))
print('len doc', len(doc))


# %%


for token in doc[:10]:
    print(token)
# %%
