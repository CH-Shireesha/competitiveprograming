# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")

def leastfrequentletters(s):
	# Your code goes here
	d = {}
	Lfl = ""
	for ch in s:
		if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
			ch = ch.lower()
			if ch not in d:
				d[ch] = 1
			else:
				d[ch] += 1
	if(len(d) == 0):
		return ""
	v = min(d.values())
	for key in d:
		if(d[key] == v):
			Lfl += key
	# print(Lfl)
	return Lfl.sorted()
	pass

# leastfrequentletters("frequent")