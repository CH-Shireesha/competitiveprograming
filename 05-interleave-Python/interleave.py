# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



import math as m

def fun_interleave(s1,s2):
	s = []
	st = ""
	m = max(len(s1),len(s2))
	if m:
		sub = s1[m:]
		for i in range (0,len(s2)):
			s.append(s1[i])
			s.append(s2[i])
		st = "".join(s)
		st = st + sub
		print(st)
		return st
	
fun_interleave('ptojl', 'yhn')