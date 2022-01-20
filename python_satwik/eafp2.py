person= {'name':'Jess', 'age':23, 'job':'Programmer'}
person1= {'name':'Jess', 'age':23}

if 'name' in person and 'age' in person and 'job' in person:
	print("I am {name}, I am {age} years old and I am a {job}".format(**person))

try:
	print("I am {name}, I am {age} years old and I am a {job}".format(**person1))
except KeyError as e:
	print('Missing {} key'.format(e))


my_list=[1,2,3,4,5,6]

if(len(my_list))>=6:
	print(my_list[5])
else:
	print("Index does not exist")

try:
	print(my_list[7])
except IndexError:
	print('Index does not exist')