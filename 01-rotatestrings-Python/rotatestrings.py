# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	if (n > 0):
		left = s
		for i in range(n):
			k = left[0:i]
			l = left[i:]
			left = l + k
			print(k,l,left)
		return left
	else:
		n = abs(n)
		k = s[0:-n]
		l = s[-n:]
		right = l + k
		print(k,l,right)
		return right

fun_rotatestrings("ac323", 8)