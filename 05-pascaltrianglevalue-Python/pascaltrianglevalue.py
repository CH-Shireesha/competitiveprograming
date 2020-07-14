# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




def fun_pascaltrianglevalue(row, col):
	return (fact(row)/ (fact(col) * fact(row-col)))

def fact(n):
	s = 1
	for i in range(2, n + 1):
		s = s * i
	if type(s) != int:
		return 0
	return s