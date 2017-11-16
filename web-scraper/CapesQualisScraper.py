#!/usr/bin/python3

import requests, sys
from selenium import webdriver
# from time import sleep
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






# res = requests.get(url)
# res.raise_for_status()


# # create a soup object to parse hmtl
# soup = BeautifulSoup(res.text, 'html.parser')



# get web element of the column names
cols_name = browser.find_elements_by_xpath('//*[@id="form"]/div[7]/div/table/thead/tr/th')

# store in labels list the column names
labels = []
for name in cols_name:
	labels.append(name.text)






numRows = browser.find_element_by_xpath('//*[@id="form:j_idt63:div_paginacao"]/ul/li').text

import re
regex = re.compile(r'\d{1,2} a \d{1,2}')
numRows = regex.findall(numRows)[0].split()
numRows = int(numRows[-1])-int(numRows[0])+1


xpath = '//*[@id="form"]/div[7]/div/table/tbody/tr'


data = []
for i in range(numRows):
	issn = browser.find_element_by_xpath(xpath+'['+str(i+1)+']/td[1]/span').text
	title = browser.find_element_by_xpath(xpath+'['+str(i+1)+']/td[2]').text
	area = browser.find_element_by_xpath(xpath+'['+str(i+1)+']/td[3]').text
	classf = browser.find_element_by_xpath(xpath+'['+str(i+1)+']/td[4]').text
	data.append((issn, title, area, classf))



import pandas as pd
df = pd.DataFrame.from_records(data, columns=labels)


print(df.head())
print(df.shape)


browser.quit()




# //*[@id="form"]/div[7]/div/table/tbody/tr[1]


# //*[@id="form"]/div[7]/div/table/tbody/tr[1]/td[1]/span
# //*[@id="form"]/div[7]/div/table/tbody/tr[1]/td[2]
# //*[@id="form"]/div[7]/div/table/tbody/tr[1]/td[3]
# //*[@id="form"]/div[7]/div/table/tbody/tr[1]/td[4]




# //*[@id="form"]/div[7]/div/table/tbody/tr[2]/td[1]/span