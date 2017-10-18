def file(filename):

	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print("the file is not exist")
	else:
		print(contents)

file('dogs.txt')
file('cats.txt')

