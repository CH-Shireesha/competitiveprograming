# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(l, newlist=None):
	if(newlist is None):
		newlist = []
	if(len(l) == 0):
		return newlist
	else:
		num = l[0]
		# print("l",l,"num",num,"even",isEven(num))
		newlist.append(isEven(num))
		fun_recursion_onlyevendigits(l[1:], newlist)
	return newlist
		
		

def isEven(num):
	if(num == 0):
		return 0
	if(num%2 == 0):
		return (num%10) + isEven(num//10)*10
	else:
		return isEven(num//10)

			


# print(isEven(5),"---")
# print(fun_recursion_onlyevendigits([43, 23265, 17, 58344]))