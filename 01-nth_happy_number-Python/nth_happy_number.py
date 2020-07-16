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
		while ishappynumber(n):
			num = n
			print(num)
	return n

def ishappynumber(n1):
	rem = sum = 0
	if n1 == 1:
		return n1
	while(n1 > 0):
		rem = n1 % 10
		sum = sum + (rem * rem)
		n1 //= 10
	result = sum
	if(result >= 10 and result !=1 and result != 4):
		result = ishappynumber(result)
	if (result == 1):
		return True
	else:
		return False

print(fun_nth_happy_number(2))