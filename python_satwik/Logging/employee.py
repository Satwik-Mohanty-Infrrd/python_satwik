import logging
logger= logging.getLogger(__name__)
formatter= logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler= logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)

logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(levelname)s:%(message)s')

class Employee:

	def __init__(self, first, last):
		self.first= first
		self.last= last 

		logging.info('Created Employee: {}-{}'.format(self.fullname, self.email))

	@property 
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)

	@property 
	def fullname(self):
		return '{} {}'.format(self.first, self.last)


emp1= Employee('Satwik', 'Mohanty')
emp2= Employee('John', 'Smith')