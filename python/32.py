# possible combinations:
# 1 x 4 = 4
# 2 x 3 = 4

# 2-9 x 4 digit permutations of 1-9 less first dig

from itertools import permutations

products = set()

digits = set(range(1,10))
for a in range(1,3):
	for x in permutations(digits,a):
		x_digits = digits.copy()
		x_digits -= set(x)
		x_val = int(''.join((str(d) for d in x)))
		for y in permutations(x_digits,5-a):
			z_digits = x_digits.copy()
			z_digits -= set(y)
			y_val = int(''.join((str(d) for d in y)))
			z = x_val * y_val
			result_digits = [int(d) for d in str(z)]
			if len(result_digits) == 4 and not z_digits ^ set(result_digits):
				products.add(z)

print sum(products)
