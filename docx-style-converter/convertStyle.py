#!/usr/bin/python3
################################################################
# An example of automating the process and conversion of font
# size and style for large .docx files using the docx python
# module.
##############################################################

import docx
from docx.shared import Pt




# read a large .docx file 
doc = docx.Document('tutorial.docx')



# define all changes at every level of the document body
style = doc.styles['Normal']
font = style.font		# get a font attribute
font.size = Pt(8)		# specify font size
font.name = 'Arial'		# specify font style

style2 = doc.styles['Heading 2']
font2 = style2.font		# get a font attribute
font2.size = Pt(16)		# specify font size
font2.bold = True
font2.name = 'Arial'	# specify font style

style3 = doc.styles['Heading 3']
font3 = style3.font		# get a font attribute
font3.size = Pt(12)		# specify font size
font3.name = 'Cambria'	# specify font style




# save a new version with modified styles
doc.save('new_tutorial.docx')

