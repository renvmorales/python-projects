#!/usr/bin/python3

import requests, bs4, sys


# weather conditions address to scrap 
weather = 'http://www.cptec.inpe.br/cidades/tempo/228'





try:	
	res = requests.get(weather) # get data from address
	res.raise_for_status() # test if connection is successful
except (requests.exceptions.HTTPError, MissingSchema):
	print('\nYou have entered an incorrect address.')
	sys.exit()




# create a soup object to parse hmtl
soup = bs4.BeautifulSoup(res.text, 'html.parser')


elems = soup.select("body > div.principal > div > div.meio_esquerda > div.cond.deg_azul > div.c2 > b")
elems_local = soup.select('body > div.principal > div > div.cidade > div.i')


temperature = elems[0].text.strip()
local = elems_local[0].text



print('\nLocal temperature today at %s is %s' % (local, temperature))
print('Source: INPE')

