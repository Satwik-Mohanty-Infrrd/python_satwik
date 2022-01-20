student= {'name':'John', 'age':25, 'courses':['English', 'Hindi']}
print(student['courses'])
print(student['name'])

student['phone']='555-5555'
print(student.get('phon','Not found'))
print(student.get('phone'))

print(student)
student['name']='Jane'
print(student)

student.update({'name':'Jane', 'age':26, 'phone':'3383-8800'})
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
	print(key,':' ,value)