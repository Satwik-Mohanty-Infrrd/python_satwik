#LEGB

'''
LEGB
Local, Enclosing, Global, Built_In
'''


#Understanding L(local) part: 

x='global x'

def test():
	y='local y'
	print(y)

test()

def test1():
	y='local y'
	print(x)

test1()

def test2():
	global x
	x='local x'
	print(x)

test2()


def test3(z):
	x='local x'
	print(z)

test3('local z')



m=min([5,4,2,3,9])
print(m)

import builtins
print(dir(builtins))


#Understanding E(enclosure): 


def outer():
	x='outer x'

	def inner():
		x='inner x'
		print(x)

	inner()
	print(x)

outer()

def outer1():
	x='outer x'

	def inner1():
		nonlocal x
		x='inner x'
		print(x)

	inner1()
	print(x)

outer1()


x='global x'

def outer2():

	def inner2():
		print(x)

	inner2()
	print(x)

outer2()
print(x)