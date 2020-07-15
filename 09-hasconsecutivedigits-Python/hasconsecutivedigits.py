# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	n = abs(n)
	count = 0
	prev = n % 10
	n //= 10
	while(n >= 0):
		temp = n % 10
		n //= 10
		if (temp == prev):
			return True
			break
		else:
			prev = n%10
			n //= 10
	return False
	
	pass