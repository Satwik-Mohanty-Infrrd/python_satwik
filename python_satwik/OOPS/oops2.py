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


emp1= Employee('Satwik', 'Mohanty', 50000)
emp2=Employee('Test', 'User', 60000)

print(Employee.ra)
print(emp1.ra)
print(emp2.ra)
print(emp1.pay)
print(emp1.first)
print(emp1.last)
print(emp1.fullname())
emp1.applyraise()
print(emp1.pay)
print(Employee.emps)
