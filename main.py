import pandas as pd
from pathlib import Path
from nlp.read_warc2 import read_warc
import extract_info as ei


DIR_DATA = Path("data/warcs")
FNAME_WARC = "sample.warc.gz"

warc_df = read_warc(DIR_DATA / FNAME_WARC)

selected_doc = warc_df.iloc[18]

result, res = ei.extract_info_from_warc(
    selected_doc["HTML_DOC"], selected_doc["WARC-TREC-ID"]
)
