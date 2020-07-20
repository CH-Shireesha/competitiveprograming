# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	frequents =  []
	for i in range(len(s)):
		for ch in s:
			if ch not in frequents:
				frequents.append(ch)
	return frequents[n-1]


