# python build_eval_classifier.py ../../data/v3/full/biased.train.pre ../../data/v3/full/biased.train.post ../../data/v3/full/vocab /Users/rpryzant/persuasion/data/v3/full/eval_classifier
# python build_eval_classifier.py ../../data/v3/words/biased.train.pre ../../data/v3/words/biased.train.post ../../data/v3/words/vocab /Users/rpryzant/persuasion/data/v3/words/eval_classifier


# builds the classifier needed for "classifier eval" metric

import time

import sys
sys.path.append('../../src/generation')
import data
import models

corpus1 = sys.argv[1]
corpus2 = sys.argv[2]
vocab_path = sys.argv[3]
save_prefix = sys.argv[4]

vocab, _ = data.build_vocab_maps(vocab_path)

tc = models.TextClassifier(vocab)

print('FITTING...')
start = time.time()
tc.fit(corpus1, corpus2)
print('DONE. TOOK ', time.time() - start)

tc.save(save_prefix)
