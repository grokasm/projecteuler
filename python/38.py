def int_to_digits(n):
	return [int(d) for d in str(n)]

def digits_to_int(digits):
	return int(''.join(map(str,digits)))

def cat_product(i,n):
	return reduce(lambda x,y:x + y, [int_to_digits(i*x) for x in range(1,n+1)])

max_num = 0

digits = set(range(1,10))

for x in xrange(10000):
	for y in xrange(2,9):
		cat = cat_product(x,y)
		val_cat = digits_to_int(cat)
		set_cat = set(cat)
		len_cat = len(cat)
		if len_cat == 9:
			diff = digits - set(set_cat)
			if not diff and val_cat > max_num:
				max_num = val_cat
		elif len_cat > 9:
			break

print max_num