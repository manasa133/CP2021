# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s,n):
	freq = dict()
	for i in s.lower():
		if i not in freq:
			freq[i] = 1
		else:
			freq[i] += 1

	srtlist = sorted(set(freq.values()), reverse=True)
	res = ""
	for key, value in freq.items():
		if value == srtlist[n-1]:
			res = key
	return res

print(fun_kth_occurrences("asuszenphonemaxm1 aemnsh", 6,))
