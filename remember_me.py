import json

def get_stored_username():
	filename='username.json'
	try:
		with open(filename) as file_object:
			username=json.load(file_object)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	username=input("what's your name:")
	filename='username.json'
	with open(filename,'w') as file_object:
		json.dump(username,file_object)
	return username

def greet_user():

	username=get_stored_username()
	a=input("are you "+username+"yes/no:")
	if a=='yes':
		print("welcome back,"+username)
	else:
		username=get_new_username()
		print("we'll remenber you "+username)
	
	

greet_user()

