# %% imports
from spacy import displacy
from beautifulsoup import scraping_bbc, scraping_wikipedia, scraping_cnn
# from spacy_time import spacy_time
import spacy
import pandas as pd
import numpy as np
import claucy
import sys


# %% ============================================================================================

# pipeline
nlp = spacy.load("en_core_web_md")
nlp.add_pipe("entityLinker", last=True)  # entity linker
claucy.add_to_pipe(nlp)  # Open IE


# %% ============================================================================================

# html document
url = "https://www.bbc.com/news/uk-63743259"
stripped_text = scraping_bbc(url)

# url_cnn = 'https://edition.cnn.com/2022/12/02/china/china-covid-lockdown-protests-2022-intl-hnk-dst/index.html'
# stripped_text = scraping_cnn(url_cnn)

# convert stripped_text array to string for processing
text = ''.join(map(str, stripped_text))


print('\n============= RAW TEXT =============\n')
print(text)


# %% ============================================================================================

# SPACY - read text and return doc to work with
print('\n============= STRIPPED TEXT =============\n')
try:
    doc = nlp(text)
    print(doc)
except:
    print("Oops!", sys.exc_info()[0], "occurred.")


# %% ============================================================================================

# NLP Preprocessing
print('\n============= NLP PRE-PROCESSING =============\n')

tokens_df = pd.DataFrame()
token_text = np.array([])
pos = np.array([])
lemma = np.array([])
ent_type = np.array([])
synt_dep = np.array([])

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


# %% ============================================================================================

# Named Entity Recognition
print('\n============= NAMED ENTITY RECOGNITION =============\n')

ner_df = pd.DataFrame()
named_entities = np.array([])
ner_types = np.array([])

# doc.ents are the named entities in the document.
# Returns a tuple of named entity Span objects, if the entity recognizer has been applied.
# recognizes when whitespace is necessary, such as in a persons name

for ent in doc.ents:
    named_entities = np.append(named_entities, ent.text)
    ner_types = np.append(ner_types, ent.label_)

ner_df['label'] = named_entities
ner_df['ner_type'] = ner_types

# ner_df.head(10)
ner_df = ner_df.drop_duplicates()
ner_df.head(10)

# REMEMBER TO REMOVE DUPLICATES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11


# %%  ============================================================================================


# Open Relation Extraction - ClausIE
print('\n============= CLAUSES =============\n')

clauses_df = pd.DataFrame()
subjects = np.array([])
preposition = np.array([])
objects = np.array([])

for clause in doc._.clauses:
    clause_structure = clause
    clause = clause.to_propositions(
        as_text=False, inflect=None)[0]

    subjects = np.append(subjects, str(clause[0]))
    preposition = np.append(preposition, str(clause[1]))

    object = str(clause[2:])
    # remove parentheses and commas
    object = object.replace(
        '(', '').replace(')', '').replace(',', '')
    objects = np.append(objects, object)

    # print(clause_structure)
    # print(clause)

clauses_df['subject'] = subjects
clauses_df['preposition'] = preposition
clauses_df['object'] = objects

clauses_df = clauses_df.drop_duplicates()
clauses_df.head(10)


# %% ============================================================================================

# Open Relation Extraction - Get the relations in which the usbject and object are named entities

named_entities = ner_df['label'].to_numpy()
related_entities = np.array([[]])

clauses_df.head()
for index, row in clauses_df.iterrows():
    # find subj, obj and prep from dataframe
    subject = row['subject']
    object = row['object']
    relation = row['preposition']

    if subject in named_entities and object in named_entities:
        # if subj and obj exist in NER-list, save them and their relation to a new list
        relation = [subject, relation, object]
        related_entities = np.append(related_entities, relation)

print(related_entities)


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
