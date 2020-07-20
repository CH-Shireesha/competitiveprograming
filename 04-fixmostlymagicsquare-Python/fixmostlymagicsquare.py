# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	l = []
	n = []
	m = []
	for i in range(len(L)):
		for j in range(len(L[0])):
			l.append(L[i][j])
		row = sum(l)
		for k in range(len(L)):
			n.append(L[k][0])
		col = sum(n)
		if (row == col):
			m = L
		else:
			num = 1
			for x in range(len(L)):
				for y in range(len(L[0])):
					L[x][y] = L[x][y] + num
					fixmostlymagicsquare(L)
			n = n + 1
	print(m)
	return m


fixmostlymagicsquare([[2, 7, 9], [9, 5, 1], [4, 3, 8]])

	# Your code goes here]