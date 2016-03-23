#!/usr/bin/python
import random
import sys
file = open(sys.argv[1], 'r') 							# opens first argument, assigns to 'file' in read mode
for line in file:
	words = line.split()			  					#create list 'words' that contains all whitespace seperated values in 'file'
	for word in words:	
		if len(word) > 2: 								# seek scramblable words
			midword = list(word[1:-1]) 					# 'midword' is 'word' without the first and last letters +++NOTE THIS HANDLES PERIODS AT THE ENDS OF WORDS AS THE LAST CHAR
			#mixword = random.shuffle(midword) # this doesn't work
			random.shuffle(midword)
			print word[0] + ''.join(midword) + word[-1], # joins the first and last letter back onto the collapsed 'midword' list and prints it
		else: 											# prints one and two letter words
			print word, 
########## +++STILL DO TO: HANDLE PERIODS AND APOSTROPHIES+++ ##############