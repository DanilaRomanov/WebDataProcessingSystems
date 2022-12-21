import pandas as pd
import numpy as np
import re


def read_warc(warc_file):

    # put docs and ids in arrays to use in dataframe
    html_list = np.array([])
    warc_trec_id_list = np.array([])
    doc_and_id_df = pd.DataFrame()

    # read warc file and split by "WARC/number"
    with open(warc_file, 'rt') as stream:
        # print('reading warc file...')

        read = stream.read()
        split_list = re.split('WARC\/\d\.\d', read)

        # loop through the data and check for trec id's and html-tags
        for warc_data in split_list:
            if len(warc_data) < 1:
                continue
            if 'WARC-TREC-ID' not in warc_data:
                continue
            if '</html>' not in warc_data:
                continue

            one_warc_data = warc_data

            # get html document
            html_index_1 = one_warc_data.index('<html')
            html_index_2 = one_warc_data.index('</html>') + 7
            html_doc = one_warc_data[html_index_1:html_index_2]
            html_list = np.append(html_list, html_doc)
            # print('HTML DOC', html_doc)

            # get warc trec id
            warc_trec_id = re.search(
                'WARC-TREC-ID: [\d\w\-\ ]+', one_warc_data)
            warc_trec_id = warc_trec_id.group(0)[len('WARC-TREC-ID: '):]
            warc_trec_id_list = np.append(warc_trec_id_list, warc_trec_id)
            # print('WARC-TREC-ID', warc_trec_id)

    # invalid warc data, throw error
    if len(html_list) < 1 or len(warc_trec_id_list) < 1:
        raise Exception(
            'No valid warc data found! Missing WARC-TREC-ID or html-tags')

    # if data is found, save to dataframe
    print('warc list', warc_trec_id_list)

    doc_and_id_df['HTML_DOC'] = html_list
    doc_and_id_df['WARC-TREC-ID'] = warc_trec_id_list

    return doc_and_id_df
