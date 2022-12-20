import spacy
nlp = spacy.load("en_coreference_web_trf")

def getClusters(text):
    doc = nlp(text)
    return doc

def coref_resolution(text):
    output = ""
    doc = getClusters(text)
    clusters = [val for key, val in doc.spans.items() if key.startswith("coref_cluster")]
    token_dict = {}
    for cluster in clusters:
        first = cluster[0]
        for repeats in list(cluster)[1:]:
            token_dict[repeats[0].idx] = first.text

            for token in repeats[1:]:


                token_dict[token.idx] = ""
    for token in doc:
        if token.idx in token_dict:
            if len(token_dict[token.idx]) > 0:
                output += token_dict[token.idx] + token.whitespace_
        else:
            output += token.text + token.whitespace_

    return output

