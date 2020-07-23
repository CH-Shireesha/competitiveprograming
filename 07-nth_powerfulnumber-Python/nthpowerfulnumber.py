# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def nthpowerfulnumber(n):
	# Your code goes here
	l = []
	for i in range(50):
		if(ispowerful(i)):
			l.append(i)
	print(l)


def ispowerful(n):
	lst = []
	if(n == 1):
		return n
	for i in range(50):
		n1 = 1
		c = 0
		while(i >= n1):
			if (i%n1 == 0):
				c += 1
			n1 += 1
		if(c == 1 or c == 2):
			lst.append(n1)
			print(lst)
			if(n%i == 0 and (n**2)%i == 0):
				print(n,i)
				return True
			else:
				return False
	return False
			
print(ispowerful(9))
# print(nthpowerfulnumber(2))