from spacy.pipeline.ner import DEFAULT_NER_MODEL
import numpy as np


def spacy_time(text, nlp):
    doc = nlp(text)

    return doc
