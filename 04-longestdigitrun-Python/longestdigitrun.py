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
	temp = a[0]
	returnval = a[0]
	c = 0
	tempc = 0
	t = (1,temp)
	for i in (a[1:]):
		if (temp == i):
			tempc += 1
		else:
			if(c < tempc):
				c = tempc
				returnval = temp
				tempc = 0
			elif(c == tempc):
				returnval = min(temp,i)
		temp = i
	print(returnval)
	pass

longestdigitrun(-6777886)