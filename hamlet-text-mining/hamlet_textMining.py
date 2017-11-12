#!/usr/bin/python3

import requests
import nltk




# url address with an online version of Hamlet' Shakespeare
url = 'http://erdani.com/tdpl/hamlet.txt'
print('\nOpening the following address:')
print('\t%s' % url)



# access url and check for failure
try:
	res = requests.get(url)
	res.raise_for_status()
except requests.exceptions.HTTPError:
	print('\nIncorrect or inexistent url address.')



# get all the work in a single string
hamlet = res.text


