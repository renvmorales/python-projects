#!/usr/bin/python3
################################################################
# An useful function for text retrieval from .docx files.
# Simply provide the file path to the function and it will return
# a single string which can be used for text mining and/or 
# general text analysis purposes.
################################################################
import docx, sys


def get_text(file_path):
	try:
		doc = docx.Document(file_path)
	except docx.opc.exceptions.PackageNotFoundError:
		print('\nInexistent file.')
		print('\t"%s" was not found.' % file_path)
		sys.exit()

	text = []
	for pgraph in doc.paragraphs:
		text.append(pgraph.text) # list with all words from file
	# (Unable to include test within tables!)

	# join all paragraphs with newline breaks
	text = '\n'.join(text)
	return text  # single string 




def main():
	text = get_text('demo.docx')
	print("\nReading 'demo.docx' file ...")
	print('Output sample:\n')
	print(text[0:500])



if __name__ == '__main__':
	main()