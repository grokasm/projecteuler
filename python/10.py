
import itertools
def generate_primes():
	D = {} 
	q = 2  
	while True:
		if q not in D:
			yield q
			D[q*q] = [q]
		else:
			for p in D[q]:
				D.setdefault(p+q,[]).append(p)
			del D[q]
		q += 1

print sum(itertools.takewhile(lambda x: x < 2000000,generate_primes()))

