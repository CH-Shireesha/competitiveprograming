# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

import math
def distance(x1,y1,x2,y2):
	d =math.pow(x1-x2,2)+math.pow(y1-y2,2)
	return d
def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	
	t1=distance(x1,y1,x2,y2)
	t2=distance(x2,y2,x3,y3)
	t3=distance(x3,y3,x1,y1)
	m = max(t1,max(t2,t3))
	add = t1+t2+t3-m
	if(math.isclose(m,add)):
		return True
	
	else:
		return False		
	pass