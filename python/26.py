from decimal import getcontext, Decimal

def dec(denominator):
	getcontext().prec = 3000
	return str(Decimal(1)/Decimal(denominator))[2:-1]

def get_repeating(string):
	found = False;
	length = 1
	strlen = len(string)
	start_at = 0

	while start_at < strlen and not found:
		tail = (strlen - start_at) % length
		patterns = [string[start : start + length] for start in xrange(start_at, strlen - tail - length + 1,length)]
		found = len(patterns) > 1
		for x in xrange(1,len(patterns)):
			found = found and patterns[x-1] == patterns[x]

		length += 1
		if len(patterns) == 1:
			start_at += 1
			length = 1

	return string[start_at:length+start_at-1]

max_len = 0
max_d = 0
for x in xrange(1,1001):
	expansion = dec(x)
	repeating = get_repeating(expansion)
	length = len(repeating)
	if length > max_len:
		max_len = length
		max_d = x

print max_d