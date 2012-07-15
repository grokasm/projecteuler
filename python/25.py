import itertools

def fib():
	a = 0
	b = 1
	while True:
		yield b
		a,b = b, a + b
		

term = 0
for x in itertools.takewhile(lambda x: len(str(x)) < 1000 , fib()):
	term += 1

term += 1
print term