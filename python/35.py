from collections import deque
from itertools import takewhile

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

prime_cache = {}

def int_to_digits(n):
	return (int(d) for d in str(n))

def digits_to_int(digits):
	return int(''.join(map(str,digits)))

def prime(n):
	if n in prime_cache:
		return prime_cache[n]
	else:
		is_prime_num = is_prime(n)
		prime_cache[n] = is_prime_num
		return is_prime_num

def is_prime(n):
	n = abs(int(n))
	if n < 2:
		return False
	if n == 2:
		return True
	# Evens > 2 aren't prime
	if not n & 1:
		return False
	for x in xrange(3, int(n**0.5) +1, 2):
		if n % x == 0:
			return False
	return True

def is_circular(p):
	prime_digits = deque(int_to_digits(p))
	circular = True
	for x in range(len(prime_digits)):
		prime_digits.rotate(1)
		circular = circular and prime(digits_to_int(prime_digits))

	return circular

print len(filter(lambda x: is_circular(x),takewhile(lambda x: x < 1000000,generate_primes())))