# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def nthpowerfulnumber(n):
	# Your code goes here
	for i in range(n//2):
		n1 = 1
		c = 0
		while(i >= n1):
			if (i%n1 == 0):
				c += 1
			n1 += 1
		if(c <= 2):
			print(i)
			
nthpowerfulnumber(36)