# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.
def mostfrequentdigit(n):
	n = str(n)
	count1 = 0
	val = 100
	for i in n:
		cnt = n.count(i)
		if(cnt>= count1):
			if(cnt== count1):
				if(int(i)<int(val)):
					count1 = cnt
					val = i
			else:
				count1 = cnt
				val = i
	return int(val)

print(mostfrequentdigit(24))
