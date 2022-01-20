li= [9,1,8,2,7,3,6,4,5]

s_li= sorted(li)
print(s_li)
print(li)  
s_li= sorted(li, reverse=True)
print(s_li)

tup=(9,1,8,2,7,3,6,4,5)
stup= sorted(tup)
print(stup)

di={'name':'Satwik', 'job':'Coding', 'age':'22', 'os':'Mac'}
sdi=sorted(di)
print(sdi)

l=[-6,-4,-5,1,2,3,4]
sl= sorted(l, key=abs)
print(sl)

class Employee():
	def __init__(self, name, age, salary):
		self.name=name
		self.age=age
		self.salary=salary

	def __repr__(self):
		return '({},{},${})'.format(self.name, self.age, self.salary)


e1= Employee('Satwik', 22, 40000)
e2= Employee('Rahul', 22, 50000)
e3= Employee('Parth', 23, 30000)


def e_sort(emp):
	return emp.salary

employees=[e1,e2,e3]
se= sorted(employees, key=e_sort)
print(se)

from operator import attrgetter

se= sorted(employees, key=attrgetter('age'))
print(se)
