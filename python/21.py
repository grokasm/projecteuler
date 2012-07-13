def get_divisors(n):
	return set(reduce(list.__add__, ([i, n/i] for i in range(1, int(n ** 0.5 + 1)) if n % i == 0)))
	
def d(n):
	s = get_divisors(n)
	s.remove(n)
	return sum(s)

cache = {}
amicables = []
for x in xrange(2,10000):
	if x in cache:
		d_x = cache[x]
	else:
		d_x = d(x)
		cache[x] = d_x

	if d_x in cache:
		d_d_x = cache[d_x]
	else:
		d_d_x = d(d_x)
		cache[d_x] = d_d_x

	if x == d_d_x and x != d_x:
		amicables.append(x)
		if d_x < 10000:
			amicables.append(d_x)

print sum(set(amicables))