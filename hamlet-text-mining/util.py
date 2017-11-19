
# find an abbreviation and replace with character name of the play
def abbrev2names(text_ls):
	out = []
	for w in text_ls:
		if w == 'Mar':
			out.append('Marcellus')
		elif w == 'Ham':
			out.append('Hamlet')
		elif w == 'Pol':
			out.append('Polonius')
		elif w == 'Hor':
			out.append('Horatio')
		elif w == 'Laer':
			out.append('Laertes')
		elif w == 'Volt':
			out.append('Voltemand')
		elif w == 'Cor':
			out.append('Cornelius')
		elif w == 'Ros':
			out.append('Rosencrantz')
		elif w == 'Guil':
			out.append('Guildenstern')
		elif w == 'Osr':
			out.append('Osric')
		elif w == 'Gent':
			out.append('Gentleman')
		elif w == 'Ber':
			out.append('Bernardo')
		elif w == 'Fran':
			out.append('Francisco')
		elif w == 'Rey':
			out.append('Reynaldo')
		elif w == 'Fort':
			out.append('Fortinbras')
		elif w == 'Capt':
			out.append('Captain')
		elif w == 'Oph':
			out.append('Ophelia')
		elif w == 'Mess':
			out.append('Messenger')
		else:
			out.append(w)
	return out




# word counter function
def wordCount(text_ls):
# initialize dictionary with counts
	count = {}

# word counter loop
	for w in text_ls:
		count.setdefault(w.upper(), 0)
		count[w.upper()]+=1

	return count

