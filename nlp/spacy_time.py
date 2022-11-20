import spacy
from spacy.pipeline.ner import DEFAULT_NER_MODEL

nlp = spacy.load("en_core_web_sm")


def spacy_time(doc):

    # print('DOC:', doc)

    # Named Entity Recognition
    config = {
        "moves": None,
        "update_with_oracle_cut_size": 100,
        "model": DEFAULT_NER_MODEL,
        "incorrect_spans_key": "incorrect_spans",
    }

    # nlp.add_pipe("ner", config=config)

    doc = nlp(doc)

    for token in doc:
        print(token.text, token.pos_, token.dep_)
        # print(nlp.ner())
