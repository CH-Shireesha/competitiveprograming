# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	d = {}
	for ch in s:
		if ch not in d.keys():
			d[ch] = 1
		else:
			d[ch] += 1
	frequents = sorted(d.items(), key = lambda x:x[1])
	print(frequents)
	return frequents

fun_kth_occurrences("hello hyderabad a",1)
