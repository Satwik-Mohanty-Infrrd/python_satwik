language= 'Java'

if language =='Python':
	print('Conditional was True')
elif language =='Java':
	print('Language is Java')
else:
	print('No match')



user='Admin'
logged_in= True

if user =='Admin' and logged_in:
	print('Admin Page')
else:
	print('Bad credentials')



a=[1,2,3]
b=[1,2,3]

print(a==b)
print(a is b)

b=a  
print(a is b)

condition=None

if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')