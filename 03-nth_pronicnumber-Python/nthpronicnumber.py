# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def nthpronicnumber(n):
	# Your code goes here
	for i in range(1,n+1):
		if(ispronic(i)):
			print(i)
	return i


def ispronic(num):
	for x in range(1,num+1):
		if(x*(x+1) == num):
			return True
	return False


print(nthpronicnumber(2))