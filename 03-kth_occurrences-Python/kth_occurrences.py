# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	frequents =  0
	for ch in s:
		while(n != 0):
			print((s.count(ch)))
			n = n-1
		print(ch)
	print(frequents)
	return frequents

fun_kth_occurrences("hello hyderabad a",1)
