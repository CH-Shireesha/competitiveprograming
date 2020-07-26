# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def recursion_powersof3ton(n):
	# Your code goes here
	if(n < 1):
		return None
	return power([], n, 0)

def power(x,num,y):
	if(y > num):
		return x
	elif(3**y <= num):
		x.append(3**y)
	return(power(x,num,y+1))

# print(recursion_powersof3ton(100))
