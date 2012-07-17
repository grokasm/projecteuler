terms = set()
for a in xrange(2, 101):
	for b in xrange(2, 101):
		terms.add(a ** b)
		terms.add(b ** a)

print len(terms)