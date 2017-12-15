# Store url

url = 'http://www.gutenberg.org/files/28885/28885-h/28885-h.htm'

# Import `requests`package

import requests

# Make the request and check object type

r = requests.get(url)

#print (type (r))

# Extract HTML from Response object and print

html = r.text

#print (html)

# Import BeautifulSoup from bs4

from bs4 import BeautifulSoup

# Create a BeautifulSoup object from the HTML

soup = BeautifulSoup (html, 'html5lib')


#Check the type and print some reassuring objects from soup: get soup title, get soup title as a string
'''
print(type(soup))

print(soup.title.string)

print(soup.title)

print(soup.find_all('a')[:8])
'''

# Get the text out of the soup and print it

text = soup.get_text()

#print(text)



# Import RegexpTokenizer from nltk.tokenize
#Import Natural Language TooKit package


import nltk

from nltk.tokenize import RegexpTokenizer


#Create the tokenizer

tokenizer = RegexpTokenizer('\w+')

#Create the tokens

tokens = tokenizer.tokenize (text)

#print (tokens [:14])


#We are going to clean the data and convert all capital letters to avoid the duplications 

words = []


#We loop through the tokens and make everything to lower case

for word in tokens :
    words.append (word.lower())
    
#We import all the English stopwords to clean the data    
    
sw = nltk.corpus.stopwords.words('English')

#Initialize a list to loop through the words all the stopwords

words_ns = []

for word in words:
    if word not in sw:
        words_ns.append (word)

#Just a final sanity check

#print(words_ns[:5])

#Now we do a frequency plot to visualize the frequency of words in the novel

import matplotlib.pyplot as plt
import seaborn as sns

#we create a frequency distribution using the frequency object from NLTK

freqdist1 = nltk.FreqDist(words_ns)

freqdist1.plot(25)

plt.show()



        




















