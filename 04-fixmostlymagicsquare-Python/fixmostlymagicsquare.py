# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	l = []
	m = []
	p = 0
	temp = 0
	result = 0
	for i in L:
		sum = 0
		for j in i:
			sum += j
		l.append(sum)
	for i in range(len(l)):
		if(l.count(l[i]) == 1):
			temp = i
			result = l[i]
		if(l.count(l[i]) > 1):
			result1 =l[i]
	for k in range(len(L)):
		sum = 0
		for x in range(len(L)):
			sum = sum + L[x][k]
		m .append(sum)
	for y in range(len(m)):
		if(m.count(m[y]) == 1):
			p = 1
		res = result - result1
		if (result1 > 0):
			L[temp][p] = L[temp][p] - res
		else:
			L[temp][p] = L[temp][p] + res
	print(L)
	return L


fixmostlymagicsquare([[2, 7, 9], [9, 5, 1], [4, 3, 8]])

	# Your code goes here]