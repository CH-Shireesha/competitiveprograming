# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.


import statistics

def median(a):
	# your code goes here
	if a.isempty():
		return None
	n = len(a)
	if n % 2 == 0:
		start = a[n//2]
		end = a[n//2 - 1]
		median = (start + end )/2
		return median
	else:
		return a[n//2]
	pass