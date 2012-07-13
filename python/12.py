def get_factors(n):
	return set(reduce(list.__add__, ([i, n/i] for i in range(1, int(n ** 0.5 + 1)) if n % i == 0)))

def get_triangle_number():
	c = 1
	num = c
	while True:
		yield num
		c += 1
		num += c

		
triangle_numbers = get_triangle_number()	
while True:	
	num = triangle_numbers.next()
	if len(get_factors(num)) > 500:
		print num
		break