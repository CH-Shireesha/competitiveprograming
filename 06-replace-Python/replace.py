# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	if s2 in s3:
		substring = s1.find(s2)
		for i in range(substring,len(s2)):
			for j in range(0,len(s3)):
				s1[i] = s3[j]
	print(s1)
	return s1

