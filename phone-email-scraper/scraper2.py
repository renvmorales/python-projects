#!/usr/bin/python3

# This is an improved version for the phone and email scraper
# It deals with 'broken' unicode-8 characters at the beginning and  
# end of some emails. It also correctly detects phone numbers even
# with misplaced whitespaces in the middle of the code area.

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
	(\s|\n) 		# starting whitespace 
	((\d){3}|\((\d){3}\))?	# code area
	(((\s)?-(\s)?)|(-)|(\s))	# first dash separator/whitespace
	(\d){3}		# 3 digits
	(-|\s)		# second dash separator/whitespace
	(\d){4}		# 4 last digits
	((ext\.|x)(\s)?\d{2,5})?	# external number
	)
	''', re.VERBOSE)


# find all phone numbers according the pattern
allPhones = phoneRegex.findall(document)


# store in a list all phone numbers from query
# (check this list, there are some extra spaces and unnecessary newlines...)
phoneNumbers = [phone[0] for phone in allPhones]



##################################################################
# Correcting phone numbers list
# Regex for correcting initial whitespaces
whitespaceRegex = re.compile(r'((\n|\s)(\d))')

# discarding these whitespaces
phoneNumbers = whitespaceRegex.sub(r'\3', '\n'.join(phoneNumbers))

print('Total phone numbers found: %d' % len(phoneNumbers.split('\n')))
###################################################################





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
# (there might be some unicode utf-8 issue: some emails start and/or end 
# with 'U')
foundEmails = [email[0] for email in allEmails]






######################################################################
# Correcting misplaced 'U' characters 
# Regex for reading errors with '.edU' ending adress
eduURegex = re.compile(r'(\.)eduU')

# find all '.eduU' patterns
errors = eduURegex.findall(' '.join(foundEmails))

# total number of matched patterns
print("\nTotal reading errors with '.eduU' ending: %d" % len(errors))

# substitute with '.edu'
foundEmails = eduURegex.sub('.edu', '\n'.join(foundEmails))




# Regex for reading errors a 'U' at the beginning of the adress
URegex = re.compile(r'((U)(\w))')

# find all 'U' patterns
errors = URegex.findall(foundEmails)


# total number of matched patterns
print("Total errors with a 'U' at the beginning: %d" % len(errors))


# Discard only the first ('U') character
foundEmails = URegex.sub(r'\3', foundEmails)
###################################################################



print('\nTotal emails found: %d' % len(foundEmails.split()))






# aggregate all resulting matches in a very long string
result = phoneNumbers + '\n' + foundEmails


print('\nCopying all matched expressions to clipboard ...')
print('You can now paste it on you favorite editor.')
pyclip.copy(result)
