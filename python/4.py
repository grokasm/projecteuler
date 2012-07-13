def is_palindrome(n):
	string = str(n)
	palindrome = True
	for i in xrange(len(string)/2):
		palindrome &= (string[i] == string[-1-i])
	return palindrome

print max((x * y for x in xrange(100,1000) for y in xrange(100,1000) if is_palindrome(x*y)))