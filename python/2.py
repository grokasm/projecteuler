def fibonacci(a=1,b=1,upto=4000000):
	while a+b < upto:
		a,b = b, a + b
		yield b

print sum ((x for x in fibonacci() if not x % 2))

