first_name= 'Satwik'
last_name='Mohanty'

sen= 'My name is {} {}'.format(first_name, last_name)
print(sen)

sen= f'My name is {first_name} {last_name}'
print(sen)

person= {'name':'Satwik', 'age':23}

sen=f"My name is {person['name']} and my age is {person['age']}"
print(sen)

calc= f'4 times 11 is equal to {4*11}'
print(calc)

for n in range(1,11):
	sem= f'The value is {n: }'
	print(sem)

pi= 3.14159265
sen= f'P is equal to {pi: .4f}'
print(sen)


from datetime import datetime

birthday= datetime(1990, 1, 1)
sen= f'Jenn has a birthday on {birthday}'
print(sen)

sem= f'Jenn has a birthday on {birthday:%B %d, %Y}'
print(sem)