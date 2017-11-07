#!/usr/bin/python3

import webbrowser, sys, pyperclip


# adress as optional external argument 
# >> googlemapit.py 192 Lisbon Av. USA
# where sys.argv = ['googlemapit.py', '192', 'Lisbon', 'Av.', 'USA']


if len(sys.argv)>1:
	# join all strings together
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()


# add address to the google maps
webbrowser.open('https://www.google.com/maps/place/' + address)
sys.exit()