# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	if (n > 0):
		k = s[n:]
		l = s[0:n]
		left = l + k
		# print(left)
		return left
	else:
		n = abs(n)
		right = fun_rotatestrings(s,len(s)-n)
		# print(k,l,right)
		return right

# fun_rotatestrings("abcd", -1)