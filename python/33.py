def check_funninness(n,d):
	ans = (1.0 * n)/d
	bad_ans = 0
	n_digits = [int(i) for i in str(n)]
	d_digits = [int(i) for i in str(d)]
	if n_digits[0] == d_digits[0] and 0 not in d_digits:
		bad_ans = (1.0 * n_digits[1])/d_digits[1]
	elif n_digits[0] == d_digits[1] and  0 not in d_digits:
		bad_ans = (1.0 * n_digits[1])/d_digits[0]
	elif n_digits[1] == d_digits[0] and  0 not in d_digits:
		bad_ans = (1.0 * n_digits[0])/d_digits[1]
	elif n_digits[1] == d_digits[1] and  0 not in d_digits:
		bad_ans = (1.0 * n_digits[0])/d_digits[0]
	return (ans, bad_ans)

def gcd(a, b):
	if b:
		return gcd(b, a % b)
	else:
		return a

def lowest_terms(n,d):
	x = gcd (d,n)
	return (n/x,d/x)

product = (1,1)
for n in xrange(10,100):
	for d in xrange(n + 1, 100):
		(ans,bad_ans) = check_funninness(n,d)
		if ans == bad_ans:
			product = (product[0] * n, product[1] * d)

(n1,d1) = lowest_terms(product[0],product[1])
print d1