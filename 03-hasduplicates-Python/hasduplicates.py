# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
	for i in range(len(L)):
		n = 1
		for j in range(len(L[i])-1):
			print(L[i][j],L[n])
			if L[i][j] in L[n]:
				return True
			else:
				n = n+1
	return False
			
	pass

print(hasduplicates([[2,7,6],[9,5,1],[4,3,8]]))