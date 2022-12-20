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

# Constants
DIR_DATA = Path("data")
FNAME_WARC = "warcs/sample.warc.gz"

# Step 1: Read warc file and iterate through the warc file and extract the html-documents and the warc-trec-ids
print(f"Reading warc file...")
first_page = read_warc(DIR_DATA / FNAME_WARC).iloc[0]
# Step 2: NLP Preprocessing
print(first_page)
# Step 3: Named Entity Recognition

# Step 4: Entity linking

# Step 5: Open Relation Extraction

# Step 6: Get the relations in which the subject and object are named entities
