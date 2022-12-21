import spacy
nlp = spacy.load("en_coreference_web_trf")

def getClusters(text):
    #Returns co-reference clusters from a text
    doc = nlp(text)
    return doc

def coref_resolution(text):
    output = ""
    doc = getClusters(text)
    #Extract the clusters
    clusters = [val for key, val in doc.spans.items() if key.startswith("coref_cluster")]
    token_dict = {}
    for cluster in clusters:
        first = cluster[0] #The first mention in a cluster is usually the entity
        for repeats in list(cluster)[1:]:
            #Save the index of the repeat and what it should be replaced with
            token_dict[repeats[0].idx] = first.text
            for token in repeats[1:]:
                #Catch repeats that are many words
                token_dict[token.idx] = ""
    for token in doc:
        if token.idx in token_dict:
            if len(token_dict[token.idx]) > 0: #If it's empty, don't add extra whitespace
                output += token_dict[token.idx] + token.whitespace_ #Coreference resolution
        else:
            output += token.text + token.whitespace_

    return output