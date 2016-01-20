# Personal-Projects

Python Knight's Tour

Version 1 Goals:
Implement a basic knight’s tour to prove that it can be done.

Version 1 Notes:
The first version works but isn't implemented well, in essence it is a basic proof of concept that the program could be written in python.
The program has the following problems. It runs once per command, will not currently test if the user has won, and revolves mostly on hard coding.

Version 2 Goals:
Change the program to instead run off a while loop that will read the user’s input and test if victory has been achieved.
The tiles of the chess board would be implemented as points of a graph. A move will be first tested for validity by checking to see that the difference
between both x and y coordinates is not 0. If the input is valid then sum of the absolute values of the differences between 
the two points will tested to be 3.

Pseudocode

The board will look like this:

A1 | A2 | A3
B1 | B2 | B3
C1 | C2 | C3
D1 | D2 | D3

Each point on the graph will be tied to a board tile e.g. A1.

if |(x2 -x1)| != 0 and |(y2-y1) != 0:
	if (|(x2 -x1)| + |(y2-y1)|) == 3:
		if(x2, y2) != 'BH': #check to make sure the point has not previously been input. Essentially, check to make sure the knight has not already been
							#to the square on the board or BH (Been Here)
			(x1,y1) == 'BH' #change the value of a point from CP (Current Position) to BH
			(x2,y2) == 'CP' #change from grids point to CP
	
else:
	print "Invalid move please select again"