#!/usr/bin/python3


from selenium import webdriver
from time import sleep
from time import time
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




# get the total number of classes available (A1, A2, B1, ...)
xpath_class = '//*[@id="form:estrato"]/option'
numClass = browser.find_elements_by_xpath(xpath_class)
numClass = len(numClass)-1



# list to store all rows from table
data = []




# begin for class name loop
start = time()
for num in range(numClass):
	# select option: A1
	browser.find_element_by_xpath(xpath_class+'['+str(num+2)+']').click()
	className = browser.find_element_by_xpath(xpath_class+'['+str(num+2)+']').text


# left-click to generate the table
	browser.find_element_by_xpath('//*[@id="form:consultar"]').click()
	sleep(1)



	if className == 'A1':
# get web element of the column names
		colsName = browser.find_elements_by_xpath('//*[@id="form"]/div[7]/div/table/thead/tr/th')

# store in labels list the column names
		labels = []
		for name in colsName:
			labels.append(name.text)



# xpath that refers to the whole table structure for each page
	xpath_table = '//*[@id="form"]/div[7]/div/table/tbody/tr'

# xpath that refers to the whole page for data scraping
	xpath_page = '//*[@id="form:j_idt63:j_idt70"]/option'

# get the number of pages for the class
	numPages = browser.find_elements_by_xpath(xpath_page)
	numPages = len(numPages)



	# begin for loop for each page
	for pag in range(numPages):
		print('\nScraping %s at page %d ...' % (className, pag+1))
		browser.find_element_by_xpath(xpath_page+'['+str(pag+1)+']').click()
		sleep(1)
		controlPage = browser.find_element_by_xpath('//*[@id="form:j_idt63:div_paginacao"]/ul/li').text
		controlPage = controlPage.split()

		# get the number of rows for this page
		numRows = int(controlPage[2])-int(controlPage[0])+1
		print('Number of rows:', numRows)

		# get every row item and append to the list
		for i in range(numRows):
			issn = browser.find_element_by_xpath(xpath_table+'['+str(i+1)+']/td[1]/span').text
			title = browser.find_element_by_xpath(xpath_table+'['+str(i+1)+']/td[2]').text
			area = browser.find_element_by_xpath(xpath_table+'['+str(i+1)+']/td[3]').text
			classf = browser.find_element_by_xpath(xpath_table+'['+str(i+1)+']/td[4]').text
			data.append((issn, title, area, classf))



# quit the browser
browser.quit()


# print total elapsed time 
print('\nScraping has finished.')
print('Total elapsed scraping time: %.3f min' % ((time()-start)/60) )


# create a dataframe from 'data' list
df = pd.DataFrame.from_records(data, columns=labels)


# print some output info
print('\nDataframe sample:')
print(df.head())
print('\nDataframe dimension: ', df.shape)
print('A .csv file will be generated.')


# write dataframe output csv file
df.to_csv('qualisMtm.csv', sep=' ', index=False)






