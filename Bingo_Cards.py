### This script creates bingo cards in a .csv format from a input text file that has each item on a new line ###

import random

filename = "b_word.txt"
num_sheet = 10

### In the two lines above I have hard-coded the input file name and the desired number of bingo cards, which can easily be changed to match your bingo needs! ###

with open (filename) as bingo:
	bingo_words = bingo.read().split("\n")


for sheet in range(num_sheet):
	random.shuffle(bingo_words)
	with open ("{0}{1}.csv".format("Bingo_Card", sheet), "a") as bingo_sheet:

		for word, position in zip (bingo_words, range (25)):

			if position == 12:
				output = 'Free Space,'
			else:
				output = "{0},".format (word)
			if position in (4,9,14,19,24):
				output += "\n"

			bingo_sheet.write(output)
	
