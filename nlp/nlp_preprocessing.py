import pandas as pd
import numpy as np
import sys


def nlp_preprocessing(doc):
    # NLP Preprocessing

    try:
        print('\n============= NLP PRE-PROCESSING =============\n')

        tokens_df = pd.DataFrame()
        token_text = np.array([])
        pos = np.array([])
        lemma = np.array([])
        ent_type = np.array([])
        synt_dep = np.array([])

        tokens = doc

        for token in tokens:
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

        return tokens_df
    except:
        print("Error:", sys.exc_info())
