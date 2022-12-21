import pandas as pd
from pathlib import Path
from nlp.read_warc2 import read_warc
import extract_info as ei
import argparse

# DIR_DATA = Path("data/warcs")
# FNAME_WARC = "sample.warc.gz"


def main(file_name: str) -> None:
    if not file_name:
        print("No WARC file present! Usage: python main.py --file <file_name>")
    else:
        warc_df = read_warc(file_name)
        selected_doc = warc_df.iloc[18]
        result_entities, result_relations = ei.extract_info_from_warc(
            selected_doc["HTML_DOC"], selected_doc["WARC-TREC-ID"]
        )
        ei.print_results(result_entities, result_relations)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file", type=str, required=True, help="The file to be processed"
    )
    args = parser.parse_args()
    main(args.file)
