# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:09:29 2018

@author: noelg
"""

import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize ('better', pos = 'a'))

print(lemmatizer.lemmatize ('cats'))
