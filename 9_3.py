class User():
	def __init__(self,first_name,last_name):
		self.first_name=first_name
		self.last_name=last_name
		self.login_attempts=0

	def greet_user(self):
		print(self.first_name+" hello ")

	def describe_user(self):
		print(self.first_name)
		print(self.last_name)
		print(self.login_attempts)

	def increment_login_attempts(self):
		self.login_attempts+=1

	def reset_login_attempts(self):
		self.login_attempts=0

class Admin(User):
	"""docstring for Admin"""
	def __init__(self, first_name,last_name):
		super(Admin,self).__init__('yan','qiang')
		self.privileges=Privileges()

	

class Privileges():
	"""docstring for privileges"""
	def __init__(self):
		super(Privileges, self).__init__()
		self.privileges =  ['can add post','can delete post','can ban user']
	def show_pricileges(self):
		print(self.privileges)
		
the_user=User('yan','qiang')
the_user.describe_user()
the_user.greet_user()
the_user.increment_login_attempts()
the_user.increment_login_attempts()
the_user.increment_login_attempts()
the_user.describe_user()
the_user.reset_login_attempts()
the_user.describe_user()
admin=Admin('yan','qiang')
admin.privileges.show_pricileges()