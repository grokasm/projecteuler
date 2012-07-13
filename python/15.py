from itertools import izip

def n_choose_k(n,k):
	return reduce(lambda x, y: x * y[0] / y[1], izip(xrange(n - k + 1, n+1), xrange(1, k+1)), 1)

print n_choose_k(40,20)