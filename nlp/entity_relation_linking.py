import pandas as pd
import numpy as np


# UNUSED FILE

def entity_relation_linking(ner_df, clauses_df):
    # Open Relation Extraction - Get the relations in which the usbject and object are named entities

    print('\n============= RELATIONS INVOLVING NERs =============\n')

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
    return related_entities
