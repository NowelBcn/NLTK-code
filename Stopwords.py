# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 18:29:11 2018

@author: noelg
"""
#Import the libraries

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


example_sentence = " Nasa's Curiosity rover has discovered something looking like trace fossils on camer, which may signal a new chapter in the age-old investigation of the Red Planet."

stop_words = set(stopwords.words("English"))

#print(stop_words)

words = word_tokenize (example_sentence)

#print(words)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

'''
this is another way to make the code above
   '''
   
#filtered_sentence = [w for w in words if not w in stop_words]
        
print (filtered_sentence)
        
    