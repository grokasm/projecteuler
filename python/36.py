def is_palindrome(string):
	return string == string[::-1]

total = 0
for x in xrange(1,1000001,2):
	if is_palindrome(str(x)):
		if is_palindrome(str(bin(x))[2:]):
			total += x

print total

# uglier one-liner version
#print sum(map(lambda (x,y): int(x),filter(lambda (x,y): x == x[::-1] and y ==y[::-1], map(lambda x: (str(x),str(bin(x))[2:]),xrange(1,1000001)))))