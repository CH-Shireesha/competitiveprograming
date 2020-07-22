# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	a = []
	n = abs(n)
	while(n > 0):
		a.append(n%10)
		n //= 10
	# print(a)
	temp = a[0]
	returnval = a[0]
	c = 0
	tempc = 1
	for i in (a[1:]):
		if (temp == i):
			tempc += 1
			print(temp,tempc,i)
		else:
			if(c < tempc):
				c = tempc
				returnval = temp
				print("inif",c,tempc,returnval)
			elif(c == tempc):
				returnval = min(returnval, i)
				print("inelse",returnval,c,tempc,temp,i)
			tempc = 1
		temp = i
	print(returnval)
	return returnval
	pass

longestdigitrun(-677886)