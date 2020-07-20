# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):
	for i in range(len(l)):
		for j in range(len(l[i])):
			n = l[i][j]
			n1 = 1
			count = 0
			while (n >= n1):
				if (n%n1 == 0):
					count += 1
			if(count <= 2):
				return False
	return True


