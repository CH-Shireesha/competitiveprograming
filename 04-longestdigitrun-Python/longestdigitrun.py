# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	d = {}
	a = []
	n = abs(n)
	while(n > 0):
		a.append(n%10)
		n //= 10
	print(a)
	t = []
	temp = a[0]
	for i in (a[1:]):
		if (temp == i):
			t = t+1
		else:
			t = 1
	print(t)
	pass

longestdigitrun(-677886)