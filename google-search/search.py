#!/usr/bin/python3

import webbrowser, requests, sys
from bs4 import BeautifulSoup


# execute with external argument:
# >> python search.py learning python programming 




# get only a string with all the keywords
keywords = ' '.join(sys.argv[1:])


print('\nGoogling the keywords:')
print('\t%s' % keywords)


# url to google using the keywords
google = 'https://www.google.com.br/search?q=' + keywords


# open a new window with the results 
webbrowser.open(google, new=1)



# get a response object for the google search
res_google = requests.get(google)



# get a soup object for parsing
soup = BeautifulSoup(res_google.text, 'html.parser')



# find all elements related to a link result
linkElem = soup.select('.r a')



ntabs = 5

for i in range(ntabs):
	webbrowser.open_new_tab('http://google.com' + 
		linkElem[i].get('href'))








