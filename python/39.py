def pythagorean_triples(p):
	sols = list()

	for a in xrange(1, p/3):
		for b in xrange(a, 2 * p / 3):
			c = p - b - a
			if (a ** 2 + b ** 2) == c ** 2:
				sols.append((a,b,c))
	return sols

max_sols = 0
max_p = 0
for p in xrange(1,1001):
	sols = pythagorean_triples(p)
	if len(sols) > max_sols:
		max_sols = len(sols)
		max_p = p

print max_p	
