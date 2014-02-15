import random

filename = "words.txt"



with open (filename) as call_list:
	call_items = call_list.read().split("\n")

print "\nWelcome to the Bingo Caller!\nHit enter to call the next item.\nTo end the caller simply type 'quit' and hit enter.\n\nThe first word is:\n"

while len (call_items) > 0:
	random.shuffle(call_items)
	called_item = call_items.pop()
	print called_item
	command = raw_input ("")
	if command != "":
		break




