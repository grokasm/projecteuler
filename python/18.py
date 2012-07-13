f = open('67.txt','r')

tree = []
for line in f:
	tree.append([int(x) for x in line.split(" ")])

for x in xrange(len(tree)-2, -1,-1):
	for y in xrange(len(tree[x])):
		tree[x][y] += max(tree[x+1][y],tree[x+1][y+1])

print tree[0][0]
