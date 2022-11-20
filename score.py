import sys
print('sys.argvs', sys.argv)

gold_file = sys.argv[1]
pred_file = sys.argv[2]
type = sys.argv[3]

# Load the gold standard
gold = {}
for line in open(gold_file):
    if type in line:
        if type == 'ENTITY':
            record, type, string, entity = line.strip().split('\t')
            gold[(record, string)] = entity
        if type == 'RELATION':
            record, type, string, s, o, rel_id = line.strip().split('\t')
            gold[(record, string)] = (s, o, rel_id)
            print('GOLD:', gold)
n_gold = len(gold)

# Load the predictions
pred = {}
for line in open(pred_file):
    if type in line:
        if type == 'ENTITY':
            record, string, entity = line.strip()[8:].split('\t')
            pred[(record, string)] = entity
        if type == 'RELATION':
            # removes whitespaces and split at tab
            tkns = line.strip()[10:].split('\t')

            print('TOKEN:', tkns)  # token

            if len(tkns) == 5:
                record, s, o, string, rel_id = tkns

            else:
                record, s, o, string = tkns
                rel_id = None

            print('RECORD:', record)  # The record of the token idk
            print('SUBJECT:', s)  # subject entity
            print('OBJECT:', o)  # object entity
            print('STRING:', string)  # relation in string
            print('RELATION ID:', rel_id)  # link to the relation in wikidata

            pred[(record, string)] = (s, o, rel_id)
            # print('PREDICTION:', pred)
n_predicted = len(pred)

# Evaluate predictions

# Calculate scores
if type == 'ENTITY':
    n_correct = sum(int(pred[i] == gold[i]) for i in set(gold) & set(pred))
    print("Evaluation ENTITY LINKING")
elif type == 'RELATION':
    matches = set(gold) & set(pred)
    n_correct = 0
    for match in matches:
        p = pred[match]
        o = gold[match]
        if len(p) == 3:  # There is also the wikidata_id. For now I ignore it, but during the grading it will be taken into account
            p = p[:2]
            o = o[:2]
        n_correct += int(p == o)

    print("Evaluation RELATION EXTRACTION")

print('gold: %s' % n_gold)
print('predicted: %s' % n_predicted)
print('correct: %s' % n_correct)
precision = float(n_correct) / float(n_predicted)
print('precision: %s' % precision)
recall = float(n_correct) / float(n_gold)
print('recall: %s' % recall)
f1 = 2 * ((precision * recall) / (precision + recall))
print('f1: %s' % f1)
