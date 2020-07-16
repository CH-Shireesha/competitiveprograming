# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)


def fun_nth_happy_number(n):
	for i in range(0,n):
		n1 = 1
		rem = sum = 0
		if n1 == 1:
			return n1
		while True:
			while(n1 > 0):
				rem = n1 % 10
				sum = sum + (rem * rem)
				n1 //= 10
			result = sum
			if(result >= 10 and result !=1 and result != 4):
				result = result
			if (result == 1):
				return result
			else:
				break
	return 0
