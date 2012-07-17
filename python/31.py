# coding=utf-8

count = 0

for x_200 in xrange(2):
	r = 200 - x_200 * 200
	for x_100 in xrange(r / 100 + 1):
		r2 = r - x_100 * 100
		for x_50 in xrange(r2 / 50+ 1):
			r3 = r2 - x_50 * 50
			for x_20 in xrange(r3 / 20 + 1):
				r4 = r3 - x_20 * 20
				for x_10 in xrange(r4 / 10 + 1):
					r5 = r4 - x_10 * 10
					for x_5 in xrange(r5 / 5 + 1):
						r6 = r5 - x_5 * 5
						for x_2 in xrange(r6 / 2 + 1):
							r7 = r6 - x_2 * 2
							x_1 = r7
					
							total = 200 * x_200 + 100 * x_100 + 50 * x_50 + 20 * x_20 + 10 * x_10 + 5 * x_5 + 2 * x_2 + x_1
							if total == 200:
								count += 1


print count							
