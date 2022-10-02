#!/usr/bin/python3
import random

#Variables
LINES = 12212 # Number of lines in the text file
FILE = 'edited_texts/iliad.e' # Name of text file to read from
lineAmount = 10 # Number of lines to be printed
printline = random.randint(0, LINES - lineAmount) # Random line to begin printing at

lineCounter = 0
with open(FILE,'r') as f:
	with open('html/iliad.html', 'w') as t:
		t.write('<link href="txtstyle.css" rel="stylesheet" type="text/css" />\n')
		for line in f:
			lineCounter += 1
			if lineCounter == printline:
				t.write(line)
				t.write('<br>')
				print(line, end='')
			elif lineCounter > printline and lineCounter < printline + lineAmount:
				t.write(line)
				t.write('<br>')
				print(line, end='')
