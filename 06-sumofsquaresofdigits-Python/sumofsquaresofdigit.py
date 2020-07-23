# Write the function sumOfSquaresOfDigits(n) which takes a non-negative integer and returns the 
# sum of the squares of its digits. Here are some test assertions for you:
# assert(sumOfSquaresOfDigits(5) == 25)   # 5**2 = 25
# assert(sumOfSquaresOfDigits(12) == 5)   # 1**2 + 2**2 = 1+4 = 5
# assert(sumOfSquaresOfDigits(234) == 29) # 2**2 + 3**2 + 4**2 = 4 + 9 + 16 = 29

def sumofsquaresofdigit(n):
	# Your code goes here
	sum = 0
	if (n <= 9):
		return n**2
	else:
		while(n > 0):
			temp = n % 10
			sum += temp**2
			n //= 10
		# print(sum)
		return sum

# sumofsquaresofdigit(234)

