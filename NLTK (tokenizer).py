# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 11:08:57 2018

@author: noelg
"""

from nltk.tokenize import sent_tokenize, word_tokenize

example_tokenize = "Problemas de tramitación impiden gastar 500 millones en las ayudas a menores de 30 años que obtengan empleo"

tokenize = sent_tokenize(example_tokenize)

tokenize2 = word_tokenize (example_tokenize)

for i in word_tokenize (example_tokenize):
    print(i)



    