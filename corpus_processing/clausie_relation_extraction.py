import pandas as pd
import numpy as np
import sys


def clausie_rel_extract(doc):

    try:
        # Open Relation Extraction - ClausIE
        print('\n============= EXTRACTED RELATIONS =============\n')

        clauses_df = pd.DataFrame()
        subjects = np.array([])
        preposition = np.array([])
        objects = np.array([])

        for clause in doc._.clauses:
            clause = clause.to_propositions(
                as_text=False, inflect=None)[0]

            subjects = np.append(subjects, str(clause[0]))
            preposition = np.append(preposition, str(clause[1]))

            object = str(clause[2:])
            # remove parentheses and commas
            object = object.replace(
                '(', '').replace(')', '').replace(',', '')
            objects = np.append(objects, object)

        clauses_df['subject'] = subjects
        clauses_df['preposition'] = preposition
        clauses_df['object'] = objects

        # drop duplicates
        clauses_df = clauses_df.drop_duplicates()

        return clauses_df

    except:
        print("Error:", sys.exc_info())
