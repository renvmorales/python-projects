#!/usr/bin/python3

import requests
from string import punctuation




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



# get the integral work into a single string
hamlet = res.text


# get all characters back with no punctuation
nopunc = [char for char in hamlet if char not in punctuation]


# join all characters into a single string
nopunc = ''.join(nopunc)