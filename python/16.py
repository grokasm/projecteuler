def add(n1,n2):
	result = []
	carry = 0
	while n1 or n2 or carry > 0:
		num1 = 0
		num2 = 0
		
		if n1:
			num1 = n1.pop()
		if n2:
			num2 = n2.pop()
		
		added = num1 + num2 + carry
		
		ones = added % 10
		carry = added / 10
		
		result.insert(0,ones)

		# print num1, num2, carry, ones
	return result

def convert(string):
	return [int(x) for x in string]

def pow2(n):
	val = [ 2 ]
	for x in xrange(n-1):
		val = add(val,list(val))
	return val

print sum(pow2(1000))