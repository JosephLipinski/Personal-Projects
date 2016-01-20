#!/usr/bin/python

import sys


#Writen by Joseph S. Lipinski
#Date Written: December 15, 2015
#Version 1.0

#The Knight's Tour is a classic puzzle in which a singular knight is placed onto a chess board. 
#The knight must then move to each square once and once alone.

#The program will be used as a command line utility and will store the board state in a text file.
#It is currently meant to be run on Tux a server at Drexel University.

line = sys.argv

#If a game has already been started then this code will execute
try:
	openFile = open('Board.txt', 'r+')
	
	print '\nThis is the current board position'
	
	BStack = []

	for line in openFile:
		BStack.append(line)
		print line,

	print '\n\nChoose a position to move the knight there.\n'
	print '\nIf the knight is unable to move to a previously unvisited square, \npress Control + D and then remove the file containing the board.\n'
	
	nLine = str(BStack)
	nLine = nLine.replace('[','')
	nLine = nLine.replace(']','')
	nLine = nLine.replace('\'', '')
	nLine = nLine.replace('\\n','')
	nLine = nLine.replace(',','')
	nLine = nLine.replace('|','')
	
	a = nLine.split()
	pA1 = a.pop(0)
	pA2 = a.pop(0)
	pA3 = a.pop(0)
	pB1 = a.pop(0)
	pB2 = a.pop(0)
	pB3 = a.pop(0)
	pC1 = a.pop(0)
	pC2 = a.pop(0)
	pC3 = a.pop(0)
	pD1 = a.pop(0)
	pD2 = a.pop(0)
	pD3 = a.pop(0)

	l = '| '
	i = ' | '
	r = ' |'
	
	try:
		gInput = ''
		while	gInput == '':
			uIn = raw_input()
			
			if pA1 == 'CP':
				pA1 = 'BH'
				if uIn == 'B3':
					if pB3 == 'BH':
						exit()
					pB3 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'C2':
					if pC2 == 'BH':
						exit()
					pC2 = 'CP'
					gInput = 'Valid move'
			
			elif pA2 == 'CP':
				pA2 = 'BH'
				if uIn == 'C1':
					if pC1 == 'BH':
						exit()
					pC1 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'C3':
					if pC3 == 'BH':
						exit()
					pC3 = 'CP'
					gInput = 'Valid move'

			elif pA3 == 'CP':
				pA3 = 'BH'
				if uIn == 'C2':
					if pC2 == 'BH':
						exit()
					pC2 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'B1':
					if pB1 == 'BH':
						exit()
					pB1 = 'CP'
					gInput = 'Valid move'

			elif pB1 == 'CP':
				pB1 = 'BH'
				if uIn == 'A3':
					if pA3 == 'BH':
						exit()
					pA3 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'C3':
					if pC3 == 'BH':
						exit()
					pC3 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'D2':
					if pD2 == 'BH':
						exit()
					pD2 = 'CP'
					gInput = 'Valid move'
		
			elif pB2 == 'CP':
				pB2 = 'BH'
				if uIn == 'D3':
					if pD3 == 'BH':
						exit()
					pD3 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'D1':
					if pD1 == 'BH':
						exit()
					pD1 = 'CP'
					gInput = 'Valid move'

			elif pB3 == 'CP':
				pB3 = 'BH'
				if uIn == 'A1':
					if pA1 == 'BH':
						exit()
					pA1 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'C1':
					if pC1 == 'BH':
						exit()
					pC1 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'D2':
					if pD2 == 'BH':
						exit()
					pD2 = 'CP'
					gInput = 'Valid move'

			elif pC1 == 'CP':
				pC1 = 'BH'
				if uIn == 'A2':
					if pA2 == 'BH':
						exit()
					pA2 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'B3':
					if pB3 == 'BH':
						exit()
					pB3 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'D3':
					if pD3 == 'BH':
						exit()
					pD3 = 'CP'
					gInput = 'Valid move'

			elif pC2 == 'CP':
				pC2 = 'BH'
				if uIn == 'A1':
					if pA1 == 'BH':
						exit()
					pA1 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'A3':
					if pA3 == 'BH':
						exit()
					pA3 = 'CP'
					gInput = 'Valid move'

			elif pC3 == 'CP':
				pC3 = 'BH'
				if uIn == 'A2':
					if pA2 == 'BH':
						exit()
					pA2 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'B1':
					if pB1 == 'BH':
						exit()
					pB1 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'D1':
					if pD1 == 'BH':
						exit()
					pD1 = 'CP'
					gInput = 'Valid move'
			
			elif pD1 == 'CP':
				pD1 = 'BH'
				if uIn == 'B2':
					if pB2 == 'BH':
						exit()
					pB2 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'C3':
					if pC3 == 'BH':
						exit()
					pC3 = 'CP'
					gInput = 'Valid move'

			elif pD2 == 'CP':
				pD2 = 'BH'
				if uIn == 'B1':
					if pB1 == 'BH':
						exit()
					pB1 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'B3':
					if pB3 == 'BH':
						exit()
					pB3 = 'CP'
					gInput = 'Valid move'

			elif pD3 == 'CP':
				pD3 = 'BH'
				if uIn == 'B2':
					if pB2 == 'BH':
						exit()
					pB2 = 'CP'
					gInput = 'Valid move'
				elif uIn == 'C1':
					if pC1 == 'BH':
						exit()
					pC1 = 'CP'
					gInput = 'Valid move'

			else:
				print '\nInvalid board. Remove the board file and begin again.'	
	except EOFError:
		exit()

	line1 = '\n' + l + pA1 + i + pA2 + i + pA3 + r
	line2 = '\n' + l + pB1 + i + pB2 + i + pB3 + r
	line3 = '\n' + l + pC1 + i + pC2 + i + pC3 + r
	line4 = '\n' + l + pD1 + i + pD2 + i + pD3 + r

	BoardState = line1 + line2 + line3 + line4			
	print BoardState + '\n'
		
	openFile = open('Board.txt', 'w')
	openFile.write(BoardState)	
	openFile.close()	


#If a previous game was not started then this code will execute
except IOError:
	print '\nMove the knight to every square only once\n' 
	print 'This is the current board:\n'

	BoardState = '| A1 | A2 | A3 |\n| B1 | B2 | B3 |\n| C1 | C2 | C3 |\n| D1 | D2 | D3 |\n'
	print BoardState

	print 'Choose a starting position'

	gInput = ''
	while	gInput == '':
		uIn = raw_input()
		if uIn == 'A1': 
			BoardState = '\n| CP | A2 | A3 |\n| B1 | B2 | B3 |\n| C1 | C2 | C3 |\n| D1 | D2 | D3 |'
			gInput = 'exit'
		
		elif uIn == 'A2': 
			BoardState = '\n| A1 | CP | A3 |\n| B1 | B2 | B3 |\n| C1 | C2 | C3 |\n| D1 | D2 | D3 |'
			gInput = 'exit'
	
		elif uIn == 'A3':
			BoardState = '\n| A1 | A2 | CP |\n| B1 | B2 | B3 |\n| C1 | C2 | C3 |\n| D1 | D2 | D3 |'
			gInput = 'exit'			
		
		elif uIn == 'B1':
			BoardState = '\n| A1 | A2 | A3 |\n| CP | B2 | B3 |\n| C1 | C2 | C3 |\n| D1 | D2 | D3 |'
			gInput = 'exit'
		
		elif uIn == 'B2':
			BoardState = '\n| A1 | A2 | A3 |\n| B1 | CP | B3 |\n| C1 | C2 | C3 |\n| D1 | D2 | D3 |'
			gInput = 'exit'
	
		elif uIn == 'B3':
			BoardState = '\n| A1 | A2 | A3 |\n| B1 | B2 | CP |\n| C1 | C2 | C3 |\n| D1 | D2 | D3 |'
			gInput = 'exit'

		elif uIn == 'C1':
			BoardState = '\n| A1 | A2 | A3 |\n| B1 | B2 | B3 |\n| CP | C2 | C3 |\n| D1 | D2 | D3 |'
			gInput = 'exit'

		elif uIn == 'C2':
			BoardState = '\n| A1 | A2 | A3 |\n| B1 | B2 | B3 |\n| C1 | CP | C3 |\n| D1 | D2 | D3 |'
			gInput = 'exit'

		elif uIn == 'C3':
			BoardState = '\n| A1 | A2 | A3 |\n| B1 | B2 | B3 |\n| C1 | C2 | CP |\n| D1 | D2 | D3 |'
			gInput = 'exit'
	
		elif uIn == 'D1':
			BoardState = '\n| A1 | A2 | A3 |\n| B1 | B2 | B3 |\n| C1 | C2 | C3 |\n| CP | D2 | D3 |'
			gInput = 'exit'
		
		elif uIn == 'D2':
			BoardState = '\n| A1 | A2 | A3 |\n| B1 | B2 | B3 |\n| C1 | C2 | C3 |\n| D1 | CP | D3 |'
			gInput = 'exit'
		
		elif uIn == 'D3':
			BoardState = '\n| A1 | A2 | A3 |\n| B1 | B2 | B3 |\n| C1 | C2 | C3 |\n| D1 | D2 | CP |'
			gInput = 'exit'
	
	print BoardState + '\n'

	openFile = open('Board.txt', 'w')
	openFile.write(BoardState)	
	openFile.close()
