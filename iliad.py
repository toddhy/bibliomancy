#!/usr/bin/python3
import random, sys, os, datetime

#Variables
today = datetime.datetime.today()
arguments = sys.argv
num_args = len(arguments)
#FILE = 'aeneid'	# Name of text file to read from
read_dir = 'edited_texts/'
write_dir = 'html/'
lineAmount = 20		# Number of lines to be printed
arr = os.listdir(read_dir)


def bib(name):
	"""
	Takes text name, reads file ending in .e from 'edited_texts/'
	Writes html into 'hmtml/'
	"""
	in_File = read_dir+name+'.e'
	out_File = write_dir+name+'.html'
	LINES = sum(1 for line in open(in_File)) # Count number of lines
	printline = random.randint(0, LINES - lineAmount) # Random line to begin printing at

	lineCounter = 0
	with open(in_File,'r') as f:
		with open(out_File, 'w') as t:
			t.write('<link href="txtstyle.css" rel="stylesheet" type="text/css" />')	#HTML at top
			t.write(today.strftime("%c")+'<p>')	#write date
			for line in f:
				lineCounter += 1
				if lineCounter >= printline and lineCounter < printline + lineAmount:
					t.write('<br>')
					t.write(line)
					#print(line, end='')

def bib_all():
	### Loop through texts directory, run bib on each file
	for text in arr:
		bib(text[0:-2])


def choice():
	if num_args not in range(1, 4):
	# argument out of range
		print("Too many arguments.")
	elif num_args == 1:
	#0 arguments
		print("Make a readout")
	elif num_args == 3:
	#2 arguments
		lineAmount = int(arguments[2])
		bib(arguments[1])
	else:
	# 1 argument
		if arguments[1] != 'all':
			bib(arguments[1])
		else:
			bib_all()

bib_all()
