#!/usr/bin/python3


from selenium import webdriver
from time import sleep
import pandas as pd
from math import ceil




# Capes qualis data url address 
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



# include all previous area options
browser.find_element_by_xpath('//*[@id="form:adicionarArea"]/span').click()



# select option: A1
browser.find_element_by_xpath('//*[@id="form:estrato"]/option[2]').click()



# left-click to generate the table
browser.find_element_by_xpath('//*[@id="form:consultar"]').click()
sleep(1)








# get web element of the column names
cols_name = browser.find_elements_by_xpath('//*[@id="form"]/div[7]/div/table/thead/tr/th')

# store in labels list the column names
labels = []
for name in cols_name:
	labels.append(name.text)




# xpath that refers to the whole table structure for each page
xpath_table = '//*[@id="form"]/div[7]/div/table/tbody/tr'

# xpath that refers to the whole page for data scraping
xpath_page = '//*[@id="form:j_idt63:j_idt70"]/option'

# get general information of the table
numPages = browser.find_elements_by_xpath(xpath_page)
numPages = len(numPages)



data = []

# begin for loop for each page
for pag in range(numPages):
	print('\nScraping page %d ...' % (pag+1))
	browser.find_element_by_xpath(xpath_page+'['+str(pag+1)+']').click()
	sleep(1)
	controlPage = browser.find_element_by_xpath('//*[@id="form:j_idt63:div_paginacao"]/ul/li').text
	controlPage = controlPage.split()

	# get the number of rows for this page
	numRows = int(controlPage[2])-int(controlPage[0])+1
	print('Number of rows:', numRows)

	for i in range(numRows):
		issn = browser.find_element_by_xpath(xpath_table+'['+str(i+1)+']/td[1]/span').text
		title = browser.find_element_by_xpath(xpath_table+'['+str(i+1)+']/td[2]').text
		area = browser.find_element_by_xpath(xpath_table+'['+str(i+1)+']/td[3]').text
		classf = browser.find_element_by_xpath(xpath_table+'['+str(i+1)+']/td[4]').text
		data.append((issn, title, area, classf))




# quit the browser
browser.quit()

print('\nScraping has finished.')

df = pd.DataFrame.from_records(data, columns=labels)


print('Dataframe sample:')
print(df.head())
print('\nDataframe dimension: ', df.shape)
print('A .csv file will be generated.')


# write ou a csv file of the dataframe
df.to_csv('qualisA1.csv', sep=' ', index=False)






