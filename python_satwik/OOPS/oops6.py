class Employee:

	ra=1.04
	emps=0
	def __init__(self, first, last):
		self.first=first
		self.last=last
		Employee.emps+=1

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	@fullname.setter 
	def fullname(self, name):
		first, last= name.split(' ')
		self.first=first
		self.last=last

	@fullname.deleter
	def fullname(self):
		print('Delete Name')
		self.first=None
		self.last=None

emp1= Employee('John', 'Smith')
emp1.first='Jim'

emp1.fullname='Satwik Mohanty'
print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname