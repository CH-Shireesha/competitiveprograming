# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
	for i in range(len(l)):
		n = 1
		for j in range(len(l[i])):
			if l[i] in l [n]:
				return True
			else:
				n = n+1

			
	pass