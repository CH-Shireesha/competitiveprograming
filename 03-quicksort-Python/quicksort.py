"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	# Your code goes here
	arr1 = []
	arr2 = []
	arr3 = []
	if(len(array) > 1):
		n = array[0]
		for i in array:
			if (i < n):
				arr2.append(i)
			elif(i == n):
				arr1.append(i)
			else:
				arr3.append(i)
		sorted_lst = sorted(arr1) + arr2 + sorted(arr3)
		return sorted_lst
	
	pass