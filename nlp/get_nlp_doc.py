from beautifulsoup import scraping_bbc
import sys
import numpy as np
import re
import shutil
from warcio.archiveiterator import ArchiveIterator


def read_warc(warc_file):

    # if .gz warc file, unzip it --- not sure if needed.
    # if warc_file[-3:] == '.gz':
    #     compressed_gz_file = warc_file
    #     with gzip.open(compressed_gz_file, 'rb') as f_in:
    #         warc_file = compressed_gz_file[:-3]
    #         with open(warc_file, 'wb') as f_out:
    #             shutil.copyfileobj(f_in, f_out)

    links = np.array([])

    # read warc file and split by "WARC/number"
    with open(warc_file, "rt") as stream:
        read = stream.read()
        split_list = re.split("WARC\/\d\.\d", read)

        # loop through the data and check for trec id's and html-tags
        for warc_data in split_list:
            if len(warc_data) < 1:
                continue
            if "WARC-TREC-ID" not in warc_data:
                continue
            if "</html>" not in warc_data:
                continue

            # print('ITS A VALID WARC DATA!?', warc_data)

        one_warc_data = warc_data

        # get html document
        html_index_1 = one_warc_data.index("<html")
        html_index_2 = one_warc_data.index("</html>") + 7
        html_doc = one_warc_data[html_index_1:html_index_2]
        # print('HTML DOC', html_doc)

        # get warc trec id
        warc_trec_id = re.search("WARC-TREC-ID: [\d\w\-\ ]+", one_warc_data)
        warc_trec_id = warc_trec_id.group(0)[len("WARC-TREC-ID: ") - 1 :]
        # print('WARC-TREC-ID', warc_trec_id)

        return [html_doc, warc_trec_id]

        # for record in ArchiveIterator(stream):
        #     # if record.rec_type == 'response':
        #     print('record', record.rec_headers)

        # warc_target_uri = record.rec_headers.get_header(
        #     'WARC-TARGET-URI')
        # if warc_target_uri[:4] == 'http' \
        #         and (warc_target_uri[len(warc_target_uri)-4:] != '.jpg') \
        #         and (warc_target_uri[len(warc_target_uri)-4:] != '.png') \
        #         and (warc_target_uri[len(warc_target_uri)-4:] != '.gif') \
        #         and (warc_target_uri[len(warc_target_uri)-5:] != '.jpeg')\
        #         and (warc_target_uri[len(warc_target_uri)-3:] != '.js')\
        #         and (warc_target_uri[len(warc_target_uri)-4:] != '.txt'):

        #         links = np.append(
        #             links, warc_target_uri)

    print(links)

    # return

    # if links are found
    if len(links) > 0:
        print("first link", links[0])
        return links[0]
    else:
        print("Oops! Found no url in warc file!")
        print(links)
        return Exception("Oops! Found no url in warc file!")


def get_nlp_doc(warc_file, nlp):
    # get url from warc file
    url = read_warc(warc_file)

    # process html-file, get raw text back
    stripped_text = scraping_bbc(url)

    try:
        # join the returned array together
        text = " ".join(map(str, stripped_text))

        # create spacy doc file
        doc = nlp(text)
        return doc
    except:
        print("Error:", sys.exc_info())
