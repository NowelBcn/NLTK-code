# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 19:39:03 2018

@author: noelg
"""

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw ("C:/Users/noelg/Desktop/Call of the wild.txt")
testing_text = state_union.raw ("C:/Users/noelg/Desktop/Alice under the ground.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(testing_text)

def process_content():
    
    try:
        for i in tokenized [:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            
            namedEnt = nltk.ne_chunk(tagged, binary = False)
            namedEnt.draw()
            
         #If we put binary = True we find the name entity but not the kind of word
         

            
            
           
        
    except Exception as e:
        print(str(e))

process_content ()


#Would it be better if we use a same author's novels to train the algorithm?

