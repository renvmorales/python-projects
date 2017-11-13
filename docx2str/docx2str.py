#!/usr/bin/python3

import docx


def get_text(file_path):
	doc = docx.Document(file_path)
	text = []

	for pgraph in doc.paragraphs:
		text.append(pgraph.text)

	# join all paragraphs with newline breaks
	text = '\n'.join(text)
	return text




def main():
	text = get_text('teste.docx')
	print('\nReading .docx file ...')
	print('Output sample:\n')
	print(text)



if __name__ == '__main__':
	main()