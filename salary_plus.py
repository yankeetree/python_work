
class Employee():
	def __init__(self,first_name,last_name,salary=0):
		self.first_name=first_name
		self.last_name=last_name
		self.salary=salary

	def give_raise(self,salary_plus=5000):
		self.salary+=salary_plus
		return (salary_plus)
