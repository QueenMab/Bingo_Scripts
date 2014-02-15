import random

filename = "b_word.txt"
num_sheet = 10

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
	
