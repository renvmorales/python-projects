#!/usr/bin/python3

import requests, sys
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup



# url address 
url = 'https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/veiculoPublicacaoQualis/listaConsultaGeralPeriodicos.xhtml'




# try:	
# 	res = requests.get(url) # get data from address
# 	res.raise_for_status() # test if connection is successful
# except (requests.exceptions.HTTPError, MissingSchema):
# 	print('\nYou have entered an incorrect address.')
# 	sys.exit()




# launch browser
browser = webdriver.Chrome()



# open the url on the browser
browser.get(url)




# select option: CLASSIFICAÇÕES DE PERIÓDICOS QUADRIÊNIO 2013-2016
browser.find_element_by_xpath('//*[@id="form:evento"]/option[2]').click()



# select option: MATEMÁTICA PROBABILIDADE E ESTATÍSTICA
browser.find_element_by_xpath('//*[@id="form:area"]/option[36]').click()



# add this option
browser.find_element_by_xpath('//*[@id="form:adicionarArea"]/span').click()



# select option: A1
browser.find_element_by_xpath('//*[@id="form:estrato"]/option[2]').click()



# left-click to generate the table
browser.find_element_by_xpath('//*[@id="form:consultar"]').click()
# sleep(3)






res = requests.get(url)
res.raise_for_status()


# create a soup object to parse hmtl
soup = BeautifulSoup(res.text, 'html.parser')

