#!/usr/bin/python3

import pyperclip as pyclip    # install module via pip3 install pyperclip
import sys



# Directions to user: copy all text (ctr-A + ctrl-C) from 
# http://cdm266101.cdmhost.com/cdm/ref/collection/p266101coll7/id/25785
print('\nPhone and email scraper')
print('Copy all text (ctrl-A + ctrl-C) from:\n')
print("\thttp://cdm266101.cdmhost.com/cdm/ref/collection/p266101coll7/id/25785")


print('\nWhen done press <enter>.')
dummy = input()




# Check if input is the <Enter> key
if not dummy:
	print('\nCopying text to the clipboard ...')
	document = pyclip.paste()
else:
	print('You have not hit <Enter> key.')
	sys.exit()





