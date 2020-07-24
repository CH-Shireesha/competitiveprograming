# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	# Your code goes here
	d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	m = 0
	s = 1
	while(m < n):
		res = str(s**5)
		flag = False
		for i in d:
			if i not in res:
				flag = True
				break
		if(not flag):
			m += 1
		s += 1
	print(s)


nthwithproperty309(0)