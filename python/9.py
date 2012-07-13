def pivots_for_total(n):
	third =  n/3
	for i in xrange(1,third):
		for j in xrange(2*i+1,n-third-1):
			yield (i,j-i, n-j)

itr = pivots_for_total(1000)
while True:
	triple =  itr.next()
	if triple[0]**2 + triple[1]**2 == triple[2]**2:
		print triple, reduce(lambda x,y:x*y,triple);
		break;