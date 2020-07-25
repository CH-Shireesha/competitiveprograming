# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2




def fun_nth_palindromic_prime(n):
	num = 1
	c = 0
	while(c <= n):
		print(c,num)
		if(isprime(num)):
			if(ispalindrome(num)):
				c += 1
		num += 1
	return num-1

def isprime(num):
	i = 1
	c = 0
	while(i <= num):
		# print(i,num)
		if(num%i == 0):
			c += 1
			if(c > 2):
				break
		i += 1
	if(c == 2):
		return True
	else:
		return False

def ispalindrome(num):
	num = str(num)
	if(num == num[::-1]):
		return True
	return False
		
# print(fun_nth_palindromic_prime(0))