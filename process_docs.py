import spacy
import pandas as pd
import numpy as np
import re
import requests
import sys

sys.path.insert(0, "../")
# Imports for NLP
from nlp.read_warc2 import read_warc

# Constants
DIR_DATA = Path("data")
FNAME_WARC = "warcs/sample.warc.gz"

# Step 1: Read warc file and iterate through the warc file and extract the html-documents and the warc-trec-ids
print(f"Reading warc file...")
read_warc(DIR_DATA / FNAME_WARC)
# Step 2: NLP Preprocessing

# Step 3: Named Entity Recognition

# Step 4: Entity linking

# Step 5: Open Relation Extraction

# Step 6: Get the relations in which the subject and object are named entities
