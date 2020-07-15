# Write the function fun_threelines_area(d1, d2, d3) 
# that takes length of 3 sides
# find the area of a triangle(return an int) given its side lengths.

import math
from math import sqrt

def fun_threelines_area(a, b, c):
	p = round((a + b + c)/2)
	area = floor(sqrt(p*(p-a)*(p-b)*(p-c)))
	return area

