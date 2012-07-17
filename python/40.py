# 9 * 1
# 90 * 2
# 900 * 3
# 9000 * 4
# 90000 * 5
# 22 - 9 * 1
# 13 / 2 = 
# 1 * 10^1 + 6 - 1  = 15 
# 13 % 2 = 1 

# 10111213141516

def int_to_digits(n):
	return [int(d) for d in str(n)]

def digits_to_int(digits):
	return int(''.join(map(str,digits)))

def get_nth_digit(n,order):
	nums_with_order_digits =  9* 10 ** (order-1) * order
	if n > nums_with_order_digits:
		remaining_digits = n - nums_with_order_digits
		return get_nth_digit(remaining_digits, order + 1)
	else:
		nth_number = n / order
		nth_digit = n % order
		x = 10 ** (order - 1) + max(0,nth_number - 1)
		print "x: ", x, "n: ", n
		return int_to_digits(x)[nth_digit]

	
print get_nth_digit(10,1)		
