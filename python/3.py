def prime_factors(x):
    for i in xrange(2, int(x ** 0.5)):
        if x % i == 0:
            return [i] + prime_factors(x / i)
    return [x]

print max(prime_factors( 600851475143))