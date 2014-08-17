def fib(max):
	a, b = 1, 1
	while a < max:
		yield a
		a, b = b, a+b

for n in fib(15):  
    print n  