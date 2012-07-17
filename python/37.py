from itertools import dropwhile,islice

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

def is_truncateable(p):
	prime_digits = list(int_to_digits(p))
	truncateable = True
	truncate_len = 1
	while truncateable and truncate_len < len(prime_digits):
		truncateable = prime(digits_to_int(prime_digits[truncate_len:])) and prime(digits_to_int(prime_digits[:-1 * truncate_len]))
		truncate_len += 1

	return truncateable

print sum(islice((p for p in dropwhile(lambda x: x < 10,generate_primes()) if is_truncateable(p)),11))

# print len(filter(lambda x: is_truncateable(x),takewhile(lambda x: x < 1000000,generate_primes())))