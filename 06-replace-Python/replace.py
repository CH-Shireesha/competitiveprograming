# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


import re

def fun_replace(s1, s2, s3):
	res = []
	k = ""
	i = 0
	while(i < len(s1)):
		if(s1[i:i+len(s2)] == s2):
			k = k + s3
			i += len(s2)
			print(k,i)
		else:
			k = k + s1[i]
			i += 1
	return k

fun_replace("hellrldowo23ufn348hf oincodnrld123", "rld", "     ",)