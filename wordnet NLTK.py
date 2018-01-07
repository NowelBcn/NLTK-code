# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 18:44:09 2018

@author: noelg
"""

import nltk
from nltk.corpus import wordnet

syns = wordnet.synsets ('cat')

#print (syns [0].name())
#print (syns [0].lemmas()[0].name())
#print (syns [0].definition())
#print (syns [0].examples())


synonyms = []
antonyms = []


for syn in wordnet.synsets ('good'):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append (l.antonyms()[0].name())
            
print (set(synonyms))
print (set(antonyms))

synonyms1 = []
antonyms1 = []


for syn in wordnet.synsets ('bad'):
    for l in syn.lemmas():
        synonyms1.append(l.name())
        if l.antonyms():
            antonyms1.append (l.antonyms()[0].name())
            
print (set(synonyms1))
print (set(antonyms1))


#syscompare = wordnet.synsets ('plane')
#syscompare2 = wordnet.synsets ('cloud')

#print (syscompare[0].name())
#print (syscompare2[0].name())

w1 = wordnet.synset ("airplane.n.01")
w2 = wordnet.synset ("balloon.n.01")

print (w1.wup_similarity(w2))



