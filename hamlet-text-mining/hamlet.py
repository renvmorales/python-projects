#!/usr/bin/python3

import requests
from string import punctuation
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer
import pandas as pd 
from util import abbrev2names, wordCount



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


# convert abbreviations to names
nopunc = abbrev2names(nopunc.split())


print('\nText preprocessing ...')
print('Total number of words: ', len(nopunc))


# # word stemming object
# ps = PorterStemmer()

# # stem words and get all text back 
# text = []
# for w in nopunc.split():
# 	text.append(ps.stem(w.lower()))





# get the word counts from the text
word_count = wordCount(nopunc)



# transform dicitonary to dataframe 
df = pd.DataFrame(data=list(word_count.values()), 
	index=word_count.keys(), columns=['Word_Count'])


# sort counts in descending order 
df = df.sort_values(by=['Word_Count'],ascending=False) 


print('\nThe most frequent used words:')
print(df.head(10))



print('\nPlotting the histogram of all word counts ...')
df.hist(column='Word_Count', bins=100, figsize=(10,8))
plt.title('Word Counts')
plt.show()




# join all words into a long string
text = ' '.join(nopunc)



# create a custom word cloud
wordcloud = WordCloud(max_words=50, width=800, height=400, 
	collocations=False, stopwords=[],
	background_color='white').generate(text)




print('\nCreating a word cloud of all words ...')

# display word cloud
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()





# create a second word cloud
wordcloud2 = WordCloud(max_words=50, width=800, height=400, 
	collocations=False, 
	background_color='white').generate(text)




print('\nCreating a word cloud discarding stopwords ...')

# display word cloud
plt.imshow(wordcloud2, interpolation="bilinear")
plt.axis("off")
plt.show()

