import 9_3
class Admin(User):
	"""docstring for Admin"""
	def __init__(self, arg):
		super().__init__()
		self.privileges = ['can add post','can delete post','can ban user']
		