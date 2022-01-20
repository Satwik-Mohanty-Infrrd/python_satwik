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

print(emp1.email)
print(emp2.email)


class Developer(Employee):
	ra=1.1

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang= prog_lang


class Manager(Employee):
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees=[]
		else:
			self.employees=employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp  in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('---->',emp.fullname())


dev1= Developer('Satwik', 'Mohanty', 50000, 'Python')
dev2= Developer('Rahul', 'Nair', 60000, 'Java')
dev3= Developer('Udesh', 'Kumar', 70000, 'C++')
print(dev1.email)
print(dev2.email)


print(dev1.pay)
dev1.applyraise()
print(dev1.pay)
print(dev1.prog_lang)

mgr1= Manager('Sue', 'Smith', 90000, [dev1])
print(mgr1.email)
mgr1.add_emp(dev2)
mgr1.add_emp(dev3)
mgr1.print_emps()
mgr1.remove_emp(dev3)
mgr1.print_emps()


print(isinstance(mgr1, Developer))
print(isinstance(dev1, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))