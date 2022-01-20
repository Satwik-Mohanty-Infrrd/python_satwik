import logging


logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')




def add(x,y):
	return x+y 

def subtract(x,y):
	return x-y 

def multiply(x,y):
	return x*y 

def divide(x,y):
	return x/y 

num1=20
num2=10
a = add(num1, num2) 
logging.debug('Add: {}+{}={}'.format(num1, num2, a))

b= subtract(num1, num2)
logging.debug('subtract: {}-{}={}'.format(num1, num2, b))

c= multiply(num1, num2)
logging.debug('multiply: {}*{}={}'.format(num1, num2, c))

d= divide(num1, num2) 
logging.debug('Add: {}/{}={}'.format(num1, num2, d))
