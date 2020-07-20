# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	if (n > 0 and len(s) < n):
		for i in range(len(s)-1):
			k = s[0:i]
			l = s[i:]
			left = l + k
		return left
	elif(n < 0):
		n = abs(n)
		return fun_rotatestrings(s,len(s)-n)
	else:
		n = abs(n)
		k = s[0:n]
		l = s[n:]
		return l + k

