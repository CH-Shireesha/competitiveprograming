# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def nthautomorphicnumbers(n):
	# Your code goes here
	num = 0
	i = 1
	while(i <= n):
		if(isautomorphic(num)):
			i += 1
		num += 1
	print(num)
	return (num)


def isautomorphic(num):
	 n = num**2
	 num = str(num)
	 n1 = len(num)
	 s = str(n)
	 print(s[len(s)-n1:])




isautomorphic(76)