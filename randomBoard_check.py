import numpy, sys, os


def boardGen(size, inVar):

	# invar is how many total 1by1 cells will be filled in
	# 3 randoms will be generated
	# 1st random to locate the small box
	# 2nd random to locate the small cell
	# 3rd random to fill in the number

	
	# 

	#checks for proper square
	if size not in [4,9,16]:
		print "Not proper square. Please enter 4, 9 or 16"
		return
	a = isinstance( inVar, (int, long) )
	
	#checks for integer
	if a is True:
		pass
	else:
		print "The initialized variable isn't an Integer. Please insert an integer."
		return

	# create list, as it maintains order, to hold all rows in CNF form
	rowSets = [set() for index in xrange(9)]
	colSets = [set() for index in xrange(9)]
	boardSets = [set() for index in xrange(9)]

	rowSets[0].add(7)

	print rowSets
	
	# for i in range(size):
	# 	boxList = [1,2,3,4,5,6,7,8,9]
	# 	cellList = [1,2,3,4,5,6,7,8,9]
	# 	numList = [1,2,3,4,5,6,7,8,9]

boardGen(9, 2)

