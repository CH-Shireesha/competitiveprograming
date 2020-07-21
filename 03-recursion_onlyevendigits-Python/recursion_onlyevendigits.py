# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(l):
	newlist = []
	if(len(l) == 0):
		return []
	else:
		num = l[0]
		if(isEven(num)):
			newlist.append(num)
			fun_recursion_onlyevendigits(l[1:])
			return newlist
		
		

def isEven(num):
	if(num%2 == 0):
		return num
	return isEven(num//10)

print(isEven(23265))
print(fun_recursion_onlyevendigits([43, 23265, 17, 58344]))