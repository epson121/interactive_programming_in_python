'''
q9.py
Turn the following English description into code:

Create a list with two numbers, 0 and 1, respectively.
For 40 times, add to the end of the list the sum of the last two numbers.
What is the last number in the list?
'''

l = [0, 1]
for i in range(2, 42):
	l.append(l[i-2] + l[i-1])
	print i

print l