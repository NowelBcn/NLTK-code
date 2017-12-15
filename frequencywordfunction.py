import requests
from bs4 import BeautifulSoup
import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer 

def word_frequency (url):
    
    r = requests.get (url)
    html = r.text
    soup = BeautifulSoup(html, "html5lib")
    text = soup.get_text()
    tokenizer = RegexpTokenizer('\w+')
    tokens = tokenizer.tokenize(text)
    words = []
    for word in tokens:
        words.append(word.lower())
    sw = nltk.corpus.stopwords.words('english')
    words_ns = []
    for word in words:
        if word not in sw:
            words_ns.append(word)
    freqdist1 = nltk.FreqDist(words_ns)
    freqdist1.plot(25)
    plt.show()
    

word_frequency ('http://www.gutenberg.org/files/55500/55500-h/55500-h.htm')
    
