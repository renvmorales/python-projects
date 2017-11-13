#!/usr/bin/python3
################################################################
# An useful function for text retrieval from .docx files.
# Simply provide the file path to the function and it will return
# a single string which can be used for text mining and/or 
# general text analysis purposes.
################################################################
import docx


def get_text(file_path):
	doc = docx.Document(file_path)
	text = []

	for pgraph in doc.paragraphs:
		text.append(pgraph.text)

	# join all paragraphs with newline breaks
	text = '\n'.join(text)
	return text  # single string 




def main():
	text = get_text('teste.docx')
	print('\nReading .docx file ...')
	print('Output sample:\n')
	print(text[0:500])



if __name__ == '__main__':
	main()