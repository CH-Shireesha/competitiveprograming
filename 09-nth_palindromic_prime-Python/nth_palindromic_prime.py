# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2




def fun_nth_palindromic_prime(n):
	num = 0
	c = 1
	while(i <= n):
		if(isprime(num)):
			if(ispalindrome(num)):
				c += 1
		num += 1
	return num