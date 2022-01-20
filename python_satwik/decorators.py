def outer_function(msg):
	message=msg

	def inner_function():
		print(message)
	return inner_function()

hi_func= outer_function('Hi')
bye_func= outer_function('Bye')

hi_func
bye_func

def decorator_function(original_function):
	def wrapper_function():
		print('Wrapper executed this before {}'.format(original_function.__name__))
		return original_function()
	return wrapper_function

def display():
	print('Display function ran')

decorated_display= decorator_function(display)
decorated_display()

class decorator_class(object):
	def __init__(self, original_function):
		self.original_function= original_function

	def __call__(self, *args, **kwargs):
		print('Call method executed this before {}'.format(self.original_function.__name__))
		return self.original_function(*args, **kwargs)

def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print('Wrapper executed this before {}'.format(original_function.__name__))
		return original_function(*args, **kwargs)
	return wrapper_function

@decorator_class
def display():
	print('Display function ran')

@decorator_class
def display_info(name, age):
	print('display info ran with arguments ({}, {})'.format(name, age))




display()
display_info('John', 25)
display_info('Travis', 30)
