# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	res = []
	k = ""
	if s2 in s1:
		substring = s1.find(s2)
		n = substring + (len(s2))
		sub = s1[n:]
		k = s3+sub 
	print(k)
	return ''.join(res)

fun_replace("helloworld123", "world", "345")