def seq(n):
	q = n
	yield q
	while q > 1:
		if q % 2:
			q = 3*q + 1
		else:
			q /= 2
		yield q

cache={}

max_len = 0
max_i = 0
for i in xrange(1,1000001):
	length = 0
	sequence = seq(i)
	for x in sequence:
		if x in cache:
			length += cache[x]
			break
		length += 1

	cache[i] = length
	if length > max_len:
		max_len = length
		max_i = i

print max_i		

		