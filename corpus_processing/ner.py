import pandas as pd
import numpy as np
import sys


def detect_entities(doc):
    try:
        # Named Entity Recognition
        print("\n============= NAMED ENTITY RECOGNITION =============\n")

        ner_df = pd.DataFrame()
        named_entities = np.array([])
        ner_types = np.array([])

        # doc.ents are the named entities in the document.
        # Returns a tuple of named entity Span objects, if the entity recognizer has been applied.
        # recognizes when whitespace is necessary, such as in a persons name

        for ent in doc.ents:
            named_entities = np.append(named_entities, ent.text)
            ner_types = np.append(ner_types, ent.label_)

        ner_df["label"] = named_entities
        ner_df["ner_type"] = ner_types

        # drop duplicates
        ner_df = ner_df.drop_duplicates()

        return ner_df
    except:
        print("Error:", sys.exc_info())
