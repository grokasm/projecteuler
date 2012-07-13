ones_arr = ("","one","two","three","four","five","six","seven","eight","nine")
teens_arr = ("ten", "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen")
tens_arr = ("","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety")

def read_number(n):
	thousands = n / 1000
	n = n % 1000
	hundreds = n / 100
	n = n % 100
	tens = n / 10
	ones = n % 10

	letters = list()
	if thousands:
		letters.append(ones_arr[thousands])
		letters.append("thousand")

	if hundreds:
		letters.append(ones_arr[hundreds])
		letters.append("hundred")

		if tens or ones:
			letters.append("and")

	if tens == 1 :
		letters.append(teens_arr[ones])
	else:
		if tens:
			letters.append(tens_arr[tens])
		if ones:
			letters.append(ones_arr[ones])

	return letters

def count_in_english(start, end):
	for x in xrange(start, end+1):
		yield read_number(x)

counter = count_in_english(1,1000)

print sum(map(lambda x : len("".join(x)), counter))
