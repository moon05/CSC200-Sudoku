import numpy, sys, os


def boardGen(size, inVar):
	
	#checks for proper square
	if size is not 4 or 9 or 16:
		print "Not proper square. Please enter 4, 9 or 16"
		return
	a = isinstance( inVar, (int, long) )
	
	#checks for integer
	if a is True:
		pass
	else:
		print "The initialized variable isn't an Integer. Please insert an integer."
		return

