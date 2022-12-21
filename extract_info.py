import spacy
import pandas as pd
import numpy as np
import re
import requests
import sys
from tqdm import tqdm
from pathlib import Path

import claucy

sys.path.insert(0, "../")
# Imports for NLP
from nlp import beautifulsoup as bsp
from nlp import nlp_preprocessing as nlp_prep
from nlp.read_warc2 import read_warc
from corpus_processing import relation_extraction as cre
from corpus_processing import entity_relation_coupling as erc
from corpus_processing import ner
from corpus_processing import relation_extraction as re
from corpus_processing import relation_linking as rl
from corpus_processing import entity_linking as el
from corpus_processing import coref as cr


def print_results(entity_result, relations_result):
    # Printing entities
    entity_result.columns = ["entity_name", "ner_type", "wiki_link", "warc_trec_id"]
    entity_result = entity_result[["warc_trec_id", "entity_name", "wiki_link"]]

    for entity in entity_result.iterrows():
        print(
            f'ENTITY:{entity[1]["warc_trec_id"]}\t{entity[1]["entity_name"]}\t{entity[1]["wiki_link"]}'
        )
    # Printing relations
    relations_result = relations_result[
        ["warc_trec_id", "subject_wiki", "object_wiki", "relation"]
    ]
    for relation in relations_result.iterrows():
        print(
            f'RELATION:{relation[1]["warc_trec_id"]}\t{relation[1]["subject_wiki"]}\t{relation[1]["object_wiki"]}\t{relation[1]["relation"]}'
        )


def extract_info_from_warc(html_doc, warc_trec_id):
    # First strip the webpage of all the html tags)
    stripped_webpage = bsp.scrape_webpage(html_doc)
    print("[+] Removed HTML tags from webpage")

    # --- NLP Preprocessing ---
    spacy_processor = spacy.load("en_core_web_md")
    spacy_doc = nlp_prep.get_nlp_doc(stripped_webpage, spacy_processor)

    print("[+] NLP Preprocessing done")

    # --- Named Entity Recognition ---
    ner_page = ner.detect_entities(spacy_doc)
    warc_trec_id_ent = [warc_trec_id for x in range(len(ner_page))]
    print("[+] Named Entity Recognition done")

    # --- Entity Linking ---
    entities_to_link = ner_page["label"].to_list()
    linked_entities = []
    for entity in tqdm(entities_to_link, desc="Entity"):
        linked_entities.append(el.link_entity(entity))

    ner_page = ner_page.reset_index(drop=True)
    entity_result = pd.concat(
        [ner_page, pd.DataFrame(linked_entities), pd.DataFrame(warc_trec_id_ent)],
        axis=1,
    )
    print("[+] Entity Linking done")

    # --- Open Relation Extraction ---
    coref_doc = cr.coref_resolution(spacy_doc)
    relations = cre.extract_relations(coref_doc)

    # Turn list of tuples into dataframe
    relations_df = pd.DataFrame(relations, columns=["relation", "subject", "object"])
    relations_df = relations_df.dropna()

    relations_df["object"] = relations_df["object"].apply(lambda x: x.text)
    relations_df["subject"] = relations_df["subject"].apply(lambda x: x.text)
    print("[+] Relations extracted")
    obj_ents, subj_ents = [], []
    print(f"Linking object entities from relations")
    for entity in tqdm(relations_df["object"].to_list(), desc="Object"):
        obj_ents.append(el.link_entity(entity))
    print(f"Linking subject entities relations")
    for entity in tqdm(relations_df["object"].to_list(), desc="Subject"):
        subj_ents.append(el.link_entity(entity))

    relations_df["subject_wiki"] = subj_ents
    relations_df["object_wiki"] = obj_ents

    relations_df = relations_df.loc[
        (relations_df["object_wiki"].isin(linked_entities))
        | (relations_df["subject_wiki"].isin(linked_entities)),
        :,
    ]

    warc_trec_id_rel = [warc_trec_id for x in range(len(relations_df))]
    relations_df = relations_df.reset_index(drop=True)
    relations_result = pd.concat(
        [relations_df, pd.DataFrame({"warc_trec_id": warc_trec_id_rel})], axis=1
    )

    return entity_result, relations_result
