# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	# Your code goes here
	x = str(x)
	y = str(y)
	z = x[::-1]
	if(len(x) == len(y)):
		if(y == z):
			return True
		s = x + y
		if(s.count(str(y)) > 0):
			return True
		return False
	else:
		return False

	pass