def dec_needdoc(func):
	if func.__doc__ == None:
		print func, 'has no __doc__, its a bad habit.' 
	else:
		print func, ':', func.__doc__, '.'
	return func

@dec_needdoc
def f():
	print 'f() do something'

@dec_needdoc
def g():
	'i have a __doc__'
	print 'g() do something'

f()
g()