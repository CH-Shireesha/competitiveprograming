# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def nthpowerfulnumber(n):
	# Your code goes here
	count = 0
	num = 1
	while (count <= n):
		if(ispowerful(num)):
			count += 1
		num += 1
	return num-1


def ispowerful(n):
	l = []
	lst = []
	count = 0
	if(n == 1):
		return n
	for i in range(n//2 + 1):
		n1 = 1
		c = 0
		while(i >= n1):
			if (i%n1 == 0):
				c += 1
			n1 += 1
		if(c == 1 or c == 2):
			lst.append(i)
			# print(lst)
	for i in range(len(lst)):
		if(n%lst[i] == 0):
			count += 1
			if(n%lst[i]**2 == 0):
				l.append(lst[i])
	# print(l)
	if (len(l) == count and len(l) > 1):
		return True
	return False
			
# print(ispowerful(13))
print(nthpowerfulnumber(10))