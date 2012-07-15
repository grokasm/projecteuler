from itertools import permutations,islice

print islice(permutations(range(10)),999999,1000000).next()