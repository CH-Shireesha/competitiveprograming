# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

import math
from math import floor

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	# x1,y1,x2,y2,x3,y3 = abs(x1),abs(y1),abs(x2),abs(y2),abs(x3),abs(y3)
	print(x1,y1,x2,y2)
	a = distance(x1,y1,x2,y2)
	b = distance(x2,y2,x3,y3)
	c = distance(x3,y3,x1,y2)
	m = max(a,max(b,c))
	n = a+b+c-m
	if (math.isclose(m,n)):
		return True
	return False
	pass

def distance(x1,y1,x2,y2):
	dist = ((x2 - x1)**2) + ((y2 - y1)**2)
	return dist

isrighttriangle(-1, 7, 10, -4, 12, -2)