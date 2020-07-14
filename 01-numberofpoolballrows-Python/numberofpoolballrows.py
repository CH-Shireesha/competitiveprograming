# Pool balls are arranged in balls where the first row contains 1 pool ball and each row contains 1
# more pool ball than the previous row. 
# numberOfPoolBallRows(balls) that takes a non-negative int number of pool balls, and returns the 
# smallest int number of balls required for the given number of pool balls. Thus, numberOfPoolBallRows(6) 
# returns 3. Note that if any balls must be in a row, then you count that row, and so 
# numberOfPoolBallRows(7) returns 4 (since the 4th row must have a single ball in it).

def fun_numberofpoolballrows(balls):
	num = 1
	count = 0
	for i in range(0,num):
		for j in range(0, i+1):
			num += 1
		count += 1
	print(count)
	return count

fun_numberofpoolballrows(7)

