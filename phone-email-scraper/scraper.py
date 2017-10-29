#!/usr/bin/python3

import pyperclip as pyclip    # install module via pip3 install pyperclip
import sys
import re


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



# set phone number Regex
phoneRegex = re.compile(r'''  
	# phone number patterns to match:
	# 500-100-0000, (500)-100-0000, 100 0000 ext 12345, ext. 12345, x12345
	(
	((\d){3}|\((\d){3}\))?	# code area
	(-|\s)		# first dash separator/whitespace
	(\d){3}		# 3 digits
	(-|\s)		# second dash separator/whitespace
	(\d){4}		# 4 last digits
	((ext\.|x)(\s)?\d{2,5})?
	)
	''', re.VERBOSE)


# find all phone numbers according the pattern
allPhones = phoneRegex.findall(document)


# store in a list all phone numbers from query
phoneNumbers = [phone[0] for phone in allPhones]


# print(phoneNumbers)
print('Total phone numbers found: %d' % len(phoneNumbers))




# set an email adress Regex 
emailRegex = re.compile(r'''
	# email pattern  123saf._+@234asfas.com
	(
	([0-9a-zA-Z._+]+)		# email username 
	@			# 'at'@ 
	([0-9a-zA-Z._+]+)		# email domain
	)
	''', re.VERBOSE)



allEmails = emailRegex.findall(document)
# print(allEmails[0:10])


# store in a list all emails from query
foundEmails = [email[0] for email in allEmails]


# print(foundEmails)
print('Total emails found: %d' % len(foundEmails))



