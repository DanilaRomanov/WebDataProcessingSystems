import spacy
import pathlib
import numpy as np
import pandas as pd
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_md")


def find_verbs(doc):
    matcher = Matcher(nlp.vocab)
    pattern = [[{"POS": "VERB"}]]
    matcher.add("Verbs", pattern)
    matches = matcher(doc.doc)
    verbs = []
    for _, start, end in matches:
        verbs.append(doc.doc[start:end].text)
    return verbs


def longest_span(spans):
    if len(spans) == 0:
        return None
    sorted_spans = sorted(spans, key=lambda s: len(s), reverse=True)
    return sorted_spans[0]


def create_spans(verbs, doc):
    patterns = [
        [{"POS": "VERB"}, {"POS": "PART", "OP": "*"}, {"POS": "ADV", "OP": "*"}],
        [
            {"POS": "VERB"},
            {"POS": "ADP", "OP": "*"},
            {"POS": "DET", "OP": "*"},
            {"POS": "AUX", "OP": "*"},
            {"POS": "ADJ", "OP": "*"},
            {"POS": "ADV", "OP": "*"},
        ],
    ]

    matcher = Matcher(nlp.vocab)
    matcher.add("Fluff", patterns)
    matches = matcher(doc)
    spans = []
    for match_id, start, end in matches:
        spans.append(doc.doc[start:end].text)
    res = []
    for verb in verbs:
        verbspans = [span for span in spans if verb in span]
        span = longest_span(verbspans)
        res.append(span)

    return res


def create_relation(span, span_index, entities):
    # Find left
    left_ent = None
    for ent in entities:
        if ent.end_char < span_index:
            if left_ent is None or left_ent.end_char < ent.end_char:
                left_ent = ent
    # Right ent
    right_ent = None
    for ent in entities:
        if ent.start_char > (span_index + len(span)):
            if right_ent is None or right_ent.start_char > ent.start_char:
                right_ent = ent
    relation = (span, left_ent, right_ent)
    return relation


def relation_extraction(text):
    doc = nlp(text)
    entities = doc.ents
    entities = [e for e in entities if e.label_ not in ("DATE")]

    verbs = find_verbs(doc)
    verbspans = create_spans(verbs, doc)
    relations = []
    for span in verbspans:
        span_index = doc.text.index(span)
        relation = create_relation(span, span_index, entities)

        relations.append(relation)
    return relations
