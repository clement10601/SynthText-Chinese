#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import nltk
from nltk.corpus import sinica_treebank

cnt = 0

sinica_fd=nltk.FreqDist(sinica_treebank.words())
# sinica_fd.keys()
# sinica_fd.values()
cnt = sum([float(x) for x in sinica_fd.values()])
print(cnt)

c = {}
for key, val in sinica_fd.items():
    c[key] = float(val) / cnt
    print(key, c[key])

d = dict(c)
# print(d)
with open("data/models/char_freq.cp", 'wb') as f:
    pickle.dump(d, f)

# with open("data/models/char_freq.cp", 'rb') as f:
#     print(pickle.load(f))