

# using a dictionary to convert characters
cards = 'TD 4C AH JS 7C 9S 1H 4D QS 4H' # string with a content

dict_cards = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,
'5':5,'4':4,'3':3,'2':2,'1':1}

# picking just the first char
card_nums = [card[0] for card in cards.split()] 

# using the 'translate' method with dictionary (python 3 version)
numbers = ' '.join(card_nums).translate({ord(k): str(v) for k, v in dict_cards.items()})

numbers = numbers.split()
numbers = [int(num) for num in numbers]
print('Original cards: ',cards)
print('Just the numbers: ', numbers)

kind = [dict_cards[digits[0]] for digits in cards.split()]