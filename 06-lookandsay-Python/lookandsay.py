# First, you can read about look-and-say numbers here. Then, write the function lookAndSay(a) that takes a list of 
# numbers and returns a list of numbers that results from "reading off" the initial list using the look-and-say 
# method, using tuples for each (count, value) pair. For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
	# Your code goes here
	temp = a[0]
	tup = (1,temp)
	l = []
	res = []
	c = 0
	for i in a[1:]:
		if (temp == i):
			tup = (i+1,temp)
			temp = i
			l.append(tup)
		else:
			tup = (1,i)
	print(l)
	return l

lookandsay([3,3,8,3,3,3])