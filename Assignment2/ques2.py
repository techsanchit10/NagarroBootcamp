# 2. Write a program which takes a text file as input and does following operations sequentially over it:
# 	- Create a list of words present in file
# 	- Convert all words to uppercase (using map)
# 	- Remove the words from list which contain 'a' (using filter)
# 	- Generate a string by concatenating all the words in the final list (using reduce)

from functools import reduce
words = []

with open("new.txt",'r+') as f:
	words = f.read().split(' ')
	print("Words in file : \n{}".format(words))
	print()

	cap_words = map(lambda words : words.upper(), words )
	print("Capitalized words: \n{}".format(list(cap_words)))
	print()

	
	filtered = list(filter(lambda words : not words.__contains__('a'), words))
	print("List of strings without 'a':\n{}".format(filtered))
	print()

	finalString = reduce(lambda str1,str2 : str1+' '+str2, words)
	print(finalString)