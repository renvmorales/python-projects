# Some useful operations using comprehensive lists 


# 'flatened' list
a = [[1, 2, 3], [34, 54, 76]]
flat_a = [item for sublist in a for item in sublist]	


# creating a list of lists for frequency storage
freq = [[0]*14 for i in range(3)]




# checks if all elements are consecutive in a list
card_num = [1, 2, 3, 4, 5]
card_num = sorted(card_num) # ascending order 
all([t-s == 1 for s, t in zip(card_num, card_num[1:])])




# selects some sublist from a list
cards = [[8, 1, 10, 3, 2], [9, 10, 1, 3, 5], [4, 9, 10, 14, 1], [10, 2, 4, 13, 15]]
hand = [0, 1]
new_set = [cards[i] for i in hand]




# finding the position index for a selected value in a list
a = [2, 4, 6, 10, 1, 2, 10]
pos = [i for i, j in enumerate(a) if j == max(a)]




# adding one to all elements of a list
a = [1, 2, 3, 4]
[x+1 for x in a]



# applying a difference on the following with the actual element values
a = [1, 2, 4, 9]
diffs = [t-s for s, t in zip(a, a[1:])]