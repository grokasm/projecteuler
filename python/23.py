def get_divisors(n):
	return set(reduce(list.__add__, ([i, n/i] for i in range(1, int(n ** 0.5 + 1)) if n % i == 0)))

def d(n):
	s = get_divisors(n)
	s.remove(n)
	return sum(s)	

def abundant_numbers():
	i = 12
	yield i
	while i < 28123:
		i += 1
		n = d(i)
		if n > i:
			yield i

abundant = [i for i in xrange(12,28124) if i<d(i)]

for x in abundant:
	print x

print len(abundant)