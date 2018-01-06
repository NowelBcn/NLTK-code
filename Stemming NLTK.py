# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 19:28:50 2018

@author: noelg
"""

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


ps = PorterStemmer()

new_text = "A closer look at the newly found angular, stick-shaped objects, led scientists to believe they could be related to crystals in the rock and even crystal molds that are typically found on Earth."

words = word_tokenize(new_text)

#for w in words:
#   print (ps.stem (w))
    
    
#You can define which words are you going to consider as stems"
    
stems = ["python", "pythonista", "pythoner","pythoning", "pythoned", "pythonly"]

for w in stems:
    print(ps.stem(w))
