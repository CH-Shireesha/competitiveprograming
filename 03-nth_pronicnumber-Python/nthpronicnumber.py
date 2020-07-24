# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def nthpronicnumber(n):
	# Your code goes here
	i = 0
	x = 0
	while (i <= n):
		x = x*(x+1)
		i = i + 1
		x += 1
		print(x)
	return x-1


print(nthpronicnumber(1))