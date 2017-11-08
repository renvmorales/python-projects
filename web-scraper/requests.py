#!/usr/bin/python3
#####################################################
# Web scraper using Requests module
# This is an example of using Requests module for getting 
# whole plain text, pdf, or ultimately, an html file.
#####################################################
import requests, sys


# set address to download (include 'raw' for GitHub and remove 'blob')
address1 = 'https://raw.github.com/renvmorales/Linear-Regression/master/linear_reg.pdf'
address2 = 'http://erdani.com/tdpl/hamlet.txt'


print('\n>>The following address(es) will be downloaded:')
print('\t' + address1)
print('\t' + address2)



try:	
	res1 = requests.get(address1) # get data from address
	res1.raise_for_status() # test if connection is successful
	res2 = requests.get(address2) 
	res2.raise_for_status() 
except requests.exceptions.HTTPError:
	print('\nYou have entered an incorrect address.')
	sys.exit()




# # some general information on the data
# print('\nDownload format: %s' % res1.headers['Content-Type'])
# print('Initial text of 100 characters:')
# print(res.text[0:100])



# create an object file (write on binary mode)
filePlay1 = open('test.pdf', 'wb')
filePlay2 = open('test.txt', 'wb')


# write every 'chunk' of data on the file
for chunk in res1.iter_content(10000):
	filePlay1.write(chunk)
filePlay1.close()

for chunk in res2.iter_content(10000):
	filePlay2.write(chunk)
filePlay2.close()

print('\n>>Download complete!')


