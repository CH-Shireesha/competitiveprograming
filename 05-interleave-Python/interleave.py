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
	mi = min(len(s1),len(s2))
	if m:
		if m == len(s1):
			sub = s1[mi:]
		else:
			sub = s2[mi:]
		for i in range (0,mi):
			s.append(s1[i])
			s.append(s2[i])
		st = "".join(s)
		st = st + sub
		return st
