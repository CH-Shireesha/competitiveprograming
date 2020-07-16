# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	#Your code goes here
	n1 = len(str1)
	n2 = len(str2)
	temp = ""
	if n1 != n2:
		return False
	temp = str1 + str1
	if (temp.count(str2) > 0):
		return True
	return False
	pass