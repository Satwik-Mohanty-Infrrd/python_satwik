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

	@classmethod
	def set_raise_amt(cls, amount):
		cls.ra= amount


	@classmethod
	def fromstring(cls, emp_str):
		first, last, pay= emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday()==5 or day.weekday()==6:
			return False
		return True



emp1= Employee('Satwik', 'Mohanty', 50000)
emp2=Employee('Test', 'User', 60000)

Employee.set_raise_amt(1.05)

print(Employee.ra)
print(emp1.ra)
print(emp2.ra)


empstr1='John-Doe-70000'
empstr2='Steve-Smith-30000'
empstr3='Jane-Doe-90000'

newemp1= Employee.fromstring(empstr1)
print(newemp1.email)
print(newemp1.pay)


import datetime
my_date= datetime.date(2016,7,10)
print(Employee.is_workday(my_date))