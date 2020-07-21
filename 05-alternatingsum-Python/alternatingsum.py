# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.




def fun_alternatingsum(a):
	sum = 0
	if (len(a) == 0):
		return 0
	elif(len(a) == 1):
		return a[0]
	else:
		for i in range(0,len(a)):
			if(i%2):
				sum -= a[i]
			else:
				sum += a[i]
		return sum



