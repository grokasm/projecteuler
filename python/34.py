from math import factorial

factorials = [factorial(x) for x in xrange(10)]

def sum_fact_digits(n):
	return sum((factorials[int(d)] for d in str(n)))


curious_numbers_sum = 0
for x in xrange(10,100000):
	if x == sum_fact_digits(x):
		curious_numbers_sum += x
		print x

print curious_numbers_sum		