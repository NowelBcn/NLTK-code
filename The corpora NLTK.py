# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:46:46 2018

@author: noelg
"""

import nltk

#print(nltk.__file__)

from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import state_union

sample = state_union.raw ("2005-GWBush.txt")

tok = sent_tokenize (sample)

for x in range (5):
    print (tok [x])
