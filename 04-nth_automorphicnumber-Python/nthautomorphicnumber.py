# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def nthautomorphicnumbers(n):
	# Your code goes here
	for i in range(0,n+1):
		if(isautomorphic(i)):
			num = i
	return (num)


def isautomorphic(num):
	n = num**2
	n1 = len(str(num))
	last = n%pow(10,n)
	if(last == num):
		return True
	else:
		return False

print(nthautomorphicnumbers(3))
