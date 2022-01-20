def prefix_decorator(prefix):
	def decorator_function(original_function):
		def wrapper_function(*args, **kwargs):
			print('Executed Before', original_function.__name__)
			res= original_function(*args, **kwargs)
			print('Executed After', original_function.__name__, '\n')
			return res
		return wrapper_function
	return decorator_function

@prefix_decorator('LOG:')
def display_info(name, age):
	print('display_info ran with arguments ({},{})'.format(name,age))

display_info('John', 25)
display_info('Travis', 30)