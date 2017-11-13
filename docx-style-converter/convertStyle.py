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



# define the level of all changes
style = doc.styles['Normal']
font = style.font		# get a font attribute
font.size = Pt(8)		# specify font size
font.name = 'Arial'		# specify font style



# save a new version with modified styles
doc.save('new_tutorial.docx')

