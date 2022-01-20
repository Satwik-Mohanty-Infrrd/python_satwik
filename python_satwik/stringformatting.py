person= {'name':'Satwik', 'age':23}

sen= 'My name is '+person['name']+ ' and I am '+ str(person['age'])+ ' years old.'
print(sen)

sen ='My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sen)

sen ='My name is {0[name]} and I am {1[age]} years old.'.format(person,person)
print(sen)

lis=['Satwik', 22]
sen= 'My name is {0[0]} and I am {0[1]} years old.'.format(lis)
print(sen)

tag='h1'
text='This is a headline'

sen='<{0}>{1}</{0}>'.format(tag, text)
print(sen)



class Person():
	def __init__(self, name, age):
		self.name=name
		self.age=age

p1=Person('Satwik', '23')
sen= 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sen)


sen= 'My name is {name} and I am {age} years old.'.format(name='Satwik', age='22')
print(sen)


for i in range(1,11):
	sen= 'The value is {:03}'.format(i)
	print(sen)


pi=3.1415435
sem= 'Pi is equal to {:.3f}'.format(pi)
print(sem)


sen= '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sen)


import datetime
my_date= datetime.datetime(2016,9,24,12,30,45)
print(my_date)


sen= '{:%B %d, %Y}'.format(my_date)
print(sen)

sen='{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sen)