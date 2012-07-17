def is_sum_n_powers(n,p):
	digits = []
	if n < 10:
		return False
	rest = n 
	while rest:
		d = rest % 10
		rest /= 10
		digits.append(d)

	total = sum(map(lambda x : x ** p, digits))

	return total == n

print sum(filter(lambda x : is_sum_n_powers(x,5),xrange(999999)))