def gcd(a, b):
	if b:
		return gcd(b, a % b)
	else:
		return a

def lcm(a,b):
	return (a * b)/gcd(a,b)

def lcmm(multiples):
	if len(multiples) == 2:
		return lcm(multiples[0],multiples[1])
	return lcm(multiples.pop(),lcmm(multiples))

print lcmm([x for x in xrange(1,21)])
