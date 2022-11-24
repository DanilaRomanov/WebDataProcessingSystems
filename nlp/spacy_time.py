from spacy.pipeline.ner import DEFAULT_NER_MODEL
import numpy as np


def spacy_time(text, nlp):

    # print('DOC:', doc)

    # Named Entity Recognition
    config = {
        "moves": None,
        "update_with_oracle_cut_size": 100,
        "model": DEFAULT_NER_MODEL,
        "incorrect_spans_key": "incorrect_spans",
    }

    # nlp.add_pipe("ner", config=config)

    # text = np.array_str(text)
    doc = nlp(text)

    # for token in doc:
    #     print(token.text, token.pos_, token.dep_)
    # print(nlp.ner())

    return doc
