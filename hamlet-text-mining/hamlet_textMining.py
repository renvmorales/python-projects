#!/usr/bin/python3

import requests
from string import punctuation
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer


# url address with an online version of Shakespeare's Hamlet
url = 'http://erdani.com/tdpl/hamlet.txt'
print('\nOpening the following address:')
print('\t%s' % url)



# access url and check for failure
try:
	res = requests.get(url)
	res.raise_for_status()
except requests.exceptions.HTTPError:
	print('\nIncorrect or inexistent url address.')



# get the integral work into a single string
hamlet = res.text


# get all characters back with no punctuation
nopunc = [char for char in hamlet if char not in punctuation]


# join all characters into a single string
nopunc = ''.join(nopunc)



# word stemming object
ps = PorterStemmer()

# stem words and get all text back 
text = []
for w in nopunc.split():
	text.append(ps.stem(w.lower()))





# word counts









# create a custom word cloud
wordcloud = WordCloud(max_words=50, width=800, height=400, 
	collocations=False, #stopwords=[],
	background_color='white').generate(nopunc)




print('\nCreating a word cloud of all words ...')

# display word cloud
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
