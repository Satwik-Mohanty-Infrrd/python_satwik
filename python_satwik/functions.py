def hello_func():
	print('Hello World')

hello_func()

def hello_satwik():
	return 'Hello Satwik'

print(hello_satwik().upper())


def hello(greeting):
	return '{} Function.'.format(greeting)

print(hello('Satwik'))


def satwik(greeting, name='You'):
	return '{}, {}'.format(greeting, name)


#Argument args is a tuple by default and kwargs is a dictionary
def student_info(*args, **kwargs):  
	print(args)
	print(kwargs)


student_info('Math', 'Art', name='John', age=22)


c=['Math', 'Art']
info= {'name': 'John', 'age':22}

student_info(c, info)

student_info(*c, **info)


month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
	return year%4==0 and (year %100!=0 or year%400==0)


def days_in_month(year, month):
	if not 1<=month<=12:
		return 'Invalid Month'
	if month==2 and is_leap(year):
		return 29

	return month_days[month]


print(days_in_month(2017, 2))