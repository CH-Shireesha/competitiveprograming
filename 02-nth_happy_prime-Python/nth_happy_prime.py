# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).



def fun_nth_happy_prime(n):
	c = 0
	num = 1
	while(c <= n):
		num += 1
		if(isprime(num)):
			if(ishappynumber(num)):
				c += 1
	return num

def isprime(n):
	i = 1
	c = 0
	while(i <= n):
		if(n%i == 0):
			c += 1
			if(c > 2):
				break
		i += 1
	if(c <= 2):
		return True
	return False

def ishappynumber(n):
	rem = sum = 0
	if(n == 1):
		return True
	while(n > 0):
		rem = n%10
		sum += rem**2
		n //= 10
	res = sum
	if(res != 1 and res != 4):
		res = ishappynumber(res)
	if(res == 1):
		return True
	else:
		return False