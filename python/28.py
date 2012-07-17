from itertools import islice

def grow_diagonal(start):
	n = start + 1
	increase_by = start
	while True:
		yield n
		increase_by += 8 
		n += increase_by

def sum_spiral_diagonals(spiral_size):
	diag_length = spiral_size / 2
	total = sum(islice(grow_diagonal(2),diag_length)) + sum(islice(grow_diagonal(4),diag_length)) + sum(islice(grow_diagonal(6),diag_length)) + sum(islice(grow_diagonal(8),diag_length)) + 1
	return total

print sum_spiral_diagonals(1001)
		