#!/usr/bin/python3
import random

#Variables
FILE = 'aeneid'	# Name of text file to read from
read_dir = 'edited_texts/'
write_dir = 'html/'
lineAmount = 10		# Number of lines to be printed

#print(LINES)

def bib(name):
	in_File = read_dir+name+'.e'
	out_File = write_dir+name+'.html'
	LINES = sum(1 for line in open(in_File))	# Count number of lines
	printline = random.randint(0, LINES - lineAmount) 	# Random line to begin printing at

	lineCounter = 0
	with open(in_File,'r') as f:
		with open(out_File, 'w') as t:
			t.write('<link href="txtstyle.css" rel="stylesheet" type="text/css" />\n')	#HTML at top
			for line in f:
				lineCounter += 1
				if lineCounter >= printline and lineCounter < printline + lineAmount:
					t.write(line)
					t.write('<br>')
					print(line, end='')
bib('aeneid')
#if lineCounter == printline:
#	t.write(line)
#	t.write('<br>')
#	print(line, end='')
