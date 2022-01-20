class Employee:

	ra=1.04
	emps=0
	def __init__(self, first, last, pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email= first+'.'+last+'@company.com'
		Employee.emps+=1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)
	def applyraise(self):
		self.pay=int(self.pay*self.ra)

	def __repr__(self):
		return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

	def __str__(self):
		return '{}-{}'.format(self.fullname(), self.email)

	def __add__(self, other):
		return self.pay+other.pay
	def __len__(self):
		return len(self.fullname())

emp1= Employee('Satwik', 'Mohanty', 50000)
emp2= Employee('Test', 'Employee', 60000)

print(emp1)
print(emp2)

print(repr(emp1))
print(str(emp1))

print(emp1+emp2)
print(len('test'))
print('tesst'.__len__())