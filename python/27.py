from itertools import takewhile

def quadratic_sequence(a,b):
	n = 0
	while True:
		yield n * (n + a)  + b
		n += 1

#http://www.daniweb.com/software-development/python/code/216880/check-if-a-number-is-a-prime-number-python
prime_cache = {}

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


max_len = 0
length = 0
best_a = 0
best_b = 0
for a in xrange(-999,1000):
	for b in xrange(-999,1000):
		 seq = quadratic_sequence(a,b)
		 length = len(list(takewhile(lambda x: prime(x), seq)))
		 if length > max_len:
		 	max_len = length
		 	best_a = a
		 	best_b = b

print max_len, best_a, best_b, best_a * best_b		 	
