f = open('22.txt','r')

names = list()

for line in f:
	names.extend(line[1:-1].split('","'))

names.sort()
score = 0

for pos in xrange(1, len(names) + 1):
	score += pos * sum(map(lambda c: ord(c) - 64,names[pos-1]))

print score
